#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
tcp_argument_audit.py

A minimal, dependency-free CLI prototype for applying the Three-Term Closure
Principle (TCP) to natural-language argument audit.

Purpose:
  - Detect under-fixed coordinates, missing dynamics, tacit assumptions,
    weak evidence markers, and unsafe/prohibited framing.
  - Return PASS / SUSPEND / FAIL with reason codes.
  - Demonstrate how TCP-style X/R/M closure can be operationalized.

Non-goals:
  - This is not a truth checker.
  - This is not a formal proof verifier.
  - This is not an LLM judge.
  - This does not prove TCP, Closure Phase Psi, DDP, or HDS.
  - This does not disclose sealed HDS core implementation.

Typical use:
  python tcp_argument_audit.py input.txt --format markdown
  cat input.txt | python tcp_argument_audit.py --format json
  python tcp_argument_audit.py --text "AI will change the world."

Authorial context:
  Designed as a public-shell demonstration script for TCP application examples.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


# -----------------------------
# Data structures
# -----------------------------

@dataclasses.dataclass
class CheckResult:
    name: str
    status: str  # PASS / SUSPEND / FAIL / WARN / INFO
    found: List[str]
    missing: List[str]
    reason_codes: List[str]
    note: str = ""


@dataclasses.dataclass
class AuditReport:
    decision: str
    reason_codes: List[str]
    score: int
    max_score: int
    confidence_note: str
    layer_results: List[CheckResult]
    reserved_items: List[str]
    metadata: Dict[str, str]


# -----------------------------
# Pattern dictionaries
# -----------------------------

PATTERNS: Dict[str, List[str]] = {
    # Layer 0: Coordinate Anchoring
    "speaker": [
        r"\bI\b", r"\bwe\b", r"\bauthor\b", r"\bspeaker\b", r"\boperator\b",
        r"私は", r"我々", r"筆者", r"著者", r"話者", r"運用者", r"利用者", r"企業", r"政府",
    ],
    "agent": [
        r"\bAI\b", r"\bLLM\b", r"\bsystem\b", r"\bmodel\b", r"\bhuman\b", r"\busers?\b",
        r"\binstitution\b", r"\borganization\b", r"\bmarket\b",
        r"AI", r"LLM", r"システム", r"モデル", r"人間", r"利用者", r"組織", r"制度", r"市場",
    ],
    "object": [
        r"\bworld\b", r"\bsociety\b", r"\beconomy\b", r"\bpolicy\b", r"\bdecision\b",
        r"\bworkflow\b", r"\bdata\b", r"\boutput\b", r"\bclaim\b",
        r"世界", r"社会", r"経済", r"政策", r"意思決定", r"業務", r"データ", r"出力", r"主張",
    ],
    "time": [
        r"\bnow\b", r"\btoday\b", r"\btomorrow\b", r"\byesterday\b", r"\bfuture\b",
        r"\bpast\b", r"\bpresent\b", r"\b\d{4}\b", r"\b\d+\s*(days?|weeks?|months?|years?)\b",
        r"現在", r"今", r"将来", r"未来", r"過去", r"以後", r"以前", r"\d{4}年", r"\d+日", r"\d+年",
    ],
    "space": [
        r"\bJapan\b", r"\bUS\b", r"\bglobal\b", r"\blocal\b", r"\benterprise\b",
        r"\borganization\b", r"\bmarket\b", r"\bdomain\b", r"\bfield\b",
        r"日本", r"米国", r"世界", r"国内", r"海外", r"企業", r"組織", r"市場", r"領域", r"分野",
    ],
    "purpose": [
        r"\bfor\b", r"\bin order to\b", r"\bpurpose\b", r"\bgoal\b", r"\baim\b",
        r"\bobjective\b", r"\bto improve\b", r"\bto reduce\b",
        r"目的", r"ため", r"狙い", r"目標", r"改善", r"削減", r"防ぐ", r"回避",
    ],
    "mechanism": [
        r"\bby\b", r"\bthrough\b", r"\bvia\b", r"\bmechanism\b", r"\bprocess\b",
        r"\bprocedure\b", r"\bworkflow\b", r"\badoption\b", r"\bimplementation\b",
        r"によって", r"通じて", r"経由", r"仕組み", r"機構", r"過程", r"手順", r"導入", r"実装", r"運用",
    ],

    # Layer 1: Dynamics
    "initial_state": [
        r"\binitial\b", r"\bbefore\b", r"\bbaseline\b", r"\bcurrent state\b",
        r"初期状態", r"導入前", r"前提状態", r"現状", r"ベースライン",
    ],
    "input": [
        r"\binput\b", r"\bstimulus\b", r"\bquery\b", r"\brequest\b", r"\bcondition\b",
        r"入力", r"刺激", r"問い", r"条件", r"リクエスト",
    ],
    "processing_rule": [
        r"\brule\b", r"\bprocess\b", r"\bprocedure\b", r"\balgorithm\b", r"\bpolicy\b",
        r"規則", r"処理", r"手順", r"アルゴリズム", r"方針", r"ルール",
    ],
    "transition": [
        r"\btransition\b", r"\bchange\b", r"\bshift\b", r"\bmove\b", r"\btransform\b",
        r"遷移", r"変化", r"変換", r"移行", r"変容",
    ],
    "branching": [
        r"\bif\b", r"\belse\b", r"\bbranch\b", r"\bcase\b", r"\bdepending on\b",
        r"場合", r"分岐", r"ケース", r"条件次第", r"ならば",
    ],
    "update": [
        r"\bupdate\b", r"\brevise\b", r"\blearn\b", r"\badapt\b", r"\biteration\b",
        r"更新", r"改訂", r"学習", r"適応", r"反復", r"イテレーション",
    ],
    "stopping": [
        r"\bstop\b", r"\bhalt\b", r"\bsuspend\b", r"\bterminate\b", r"\bend condition\b",
        r"停止", r"中断", r"SUSPEND", r"保留", r"打ち止め", r"終了条件",
    ],
    "feedback": [
        r"\bfeedback\b", r"\bloop\b", r"\breturn\b", r"\breinput\b",
        r"フィードバック", r"ループ", r"戻す", r"再入力", r"循環",
    ],

    # Layer 2: Tacit knowledge
    "definition": [
        r"\bdefine\b", r"\bdefinition\b", r"\bmeans\b", r"\brefers to\b", r"\bis defined as\b",
        r"定義", r"とは", r"意味する", r"指す", r"とする",
    ],
    "premise": [
        r"\bpremise\b", r"\bassume\b", r"\bassumption\b", r"\bgiven\b", r"\bprovided that\b",
        r"前提", r"仮定", r"想定", r"所与", r"ならば",
    ],
    "scope": [
        r"\bscope\b", r"\brange\b", r"\bwithin\b", r"\bonly\b", r"\blimited to\b",
        r"射程", r"範囲", r"限定", r"限る", r"対象範囲", r"適用範囲",
    ],
    "uncertainty": [
        r"\bmay\b", r"\bmight\b", r"\bcould\b", r"\bpossibly\b", r"\buncertain\b",
        r"\bhypothesis\b", r"\binference\b", r"\bprediction\b", r"\bestimate\b",
        r"可能性", r"かもしれない", r"推測", r"仮説", r"予測", r"不確実", r"推定", r"未確認",
    ],

    # Layer 3: Explicit argument
    "validity_marker": [
        r"\btherefore\b", r"\bthus\b", r"\bbecause\b", r"\bsince\b", r"\bif\b.*\bthen\b",
        r"したがって", r"ゆえに", r"なぜなら", r"だから", r"もし.*なら",
    ],
    "evidence_marker": [
        r"\bevidence\b", r"\bdata\b", r"\blog\b", r"\bsource\b", r"\breference\b", r"\bobserved\b",
        r"\bmeasured\b", r"\bexperiment\b", r"\breport\b",
        r"証拠", r"データ", r"ログ", r"出典", r"参照", r"観測", r"測定", r"実験", r"報告",
    ],
    "contrast_marker": [
        r"\bhowever\b", r"\bbut\b", r"\balthough\b", r"\bon the other hand\b",
        r"しかし", r"ただし", r"一方", r"とはいえ", r"だが",
    ],

    # Risk / prohibited use
    "prohibited_use": [
        r"\brank people\b", r"\bscore people\b", r"\bpersonality score\b",
        r"\bmanipulate\b", r"\bexploit\b", r"\bcontrol people\b", r"\bcoerce\b",
        r"\bdesign ego\b", r"\bself-optimizing OS\b", r"\bfully structure emotion\b",
        r"序列化", r"人格査定", r"格付け", r"人間を操作", r"操作する", r"支配", r"誘導",
        r"扇動", r"搾取", r"自我設計", r"自律最適化", r"感情.*完全構造化",
    ],
    "broad_claim": [
        r"\balways\b", r"\bnever\b", r"\beveryone\b", r"\beverything\b", r"\bthe world\b",
        r"\bwill change the world\b", r"\buniversal\b",
        r"必ず", r"絶対", r"全て", r"すべて", r"誰でも", r"世界を変える", r"普遍",
    ],
}


LAYER_REQUIREMENTS: Dict[str, List[str]] = {
    "Layer 0: Coordinate Anchoring": [
        "speaker", "agent", "object", "time", "space", "purpose", "mechanism"
    ],
    "Layer 1: Dynamic Transition": [
        "initial_state", "input", "processing_rule", "transition",
        "branching", "update", "stopping", "feedback"
    ],
    "Layer 2: Tacit-Knowledge Audit": [
        "definition", "premise", "scope", "uncertainty"
    ],
    "Layer 3: Explicit Argument Audit": [
        "validity_marker", "evidence_marker", "contrast_marker"
    ],
}


REASON_LABELS = {
    "speaker": "COORD_SPEAKER_UNFIXED",
    "agent": "COORD_AGENT_UNFIXED",
    "object": "COORD_OBJECT_UNFIXED",
    "time": "COORD_TIME_UNFIXED",
    "space": "COORD_SPACE_UNFIXED",
    "purpose": "COORD_PURPOSE_UNFIXED",
    "mechanism": "COORD_MECHANISM_UNFIXED",
    "initial_state": "DYN_INITIAL_STATE_MISSING",
    "input": "DYN_INPUT_MISSING",
    "processing_rule": "DYN_PROCESSING_RULE_MISSING",
    "transition": "DYN_TRANSITION_MISSING",
    "branching": "DYN_BRANCHING_MISSING",
    "update": "DYN_UPDATE_MISSING",
    "stopping": "DYN_STOPPING_MISSING",
    "feedback": "DYN_FEEDBACK_MISSING",
    "definition": "TACIT_DEFINITION_MISSING",
    "premise": "TACIT_PREMISE_MISSING",
    "scope": "TACIT_SCOPE_MISSING",
    "uncertainty": "TACIT_UNCERTAINTY_MISSING",
    "validity_marker": "ARG_INFERENCE_MARKER_MISSING",
    "evidence_marker": "ARG_EVIDENCE_MARKER_MISSING",
    "contrast_marker": "ARG_CONTRAST_OR_LIMITATION_MARKER_MISSING",
}


def normalize(text: str) -> str:
    return text.replace("\u3000", " ").strip()


def collect_hits(text: str, key: str, max_hits: int = 5) -> List[str]:
    hits: List[str] = []
    for pat in PATTERNS.get(key, []):
        try:
            for m in re.finditer(pat, text, flags=re.IGNORECASE | re.DOTALL):
                s = m.group(0)
                if s and s not in hits:
                    hits.append(s[:80])
                if len(hits) >= max_hits:
                    return hits
        except re.error:
            continue
    return hits


def check_layer(text: str, layer_name: str, keys: List[str]) -> Tuple[CheckResult, int, int]:
    found_items = []
    missing_items = []
    reason_codes = []
    score = 0

    for key in keys:
        hits = collect_hits(text, key)
        if hits:
            score += 1
            found_items.append(f"{key}: {', '.join(hits[:3])}")
        else:
            missing_items.append(key)
            reason_codes.append(REASON_LABELS.get(key, f"{key.upper()}_MISSING"))

    # Layer-specific status
    missing_count = len(missing_items)
    if layer_name.startswith("Layer 0"):
        if "agent" in missing_items or "object" in missing_items or missing_count >= 4:
            status = "SUSPEND"
        elif missing_count > 0:
            status = "WARN"
        else:
            status = "PASS"
    elif layer_name.startswith("Layer 1"):
        if missing_count >= 5:
            status = "SUSPEND"
        elif missing_count > 0:
            status = "WARN"
        else:
            status = "PASS"
    elif layer_name.startswith("Layer 2"):
        if ("definition" in missing_items and "scope" in missing_items) or missing_count >= 3:
            status = "SUSPEND"
        elif missing_count > 0:
            status = "WARN"
        else:
            status = "PASS"
    else:
        if missing_count >= 2:
            status = "WARN"
        else:
            status = "PASS"

    note = ""
    if status == "SUSPEND":
        note = "This layer is insufficiently fixed for closure."
    elif status == "WARN":
        note = "This layer has partial closure but remains weak."
    elif status == "PASS":
        note = "This layer contains minimum observable markers."

    return CheckResult(
        name=layer_name,
        status=status,
        found=found_items,
        missing=missing_items,
        reason_codes=reason_codes,
        note=note,
    ), score, len(keys)


def detect_failures_and_warnings(text: str) -> Tuple[List[str], List[str], List[str]]:
    """Return (fatal_codes, warning_codes, warning_messages)."""
    fatal_codes: List[str] = []
    warning_codes: List[str] = []
    warnings: List[str] = []

    prohibited = collect_hits(text, "prohibited_use")
    if prohibited:
        fatal_codes.append("FAIL_PROHIBITED_USE_PATTERN")
        warnings.append("Potential prohibited-use framing detected: " + ", ".join(prohibited[:5]))

    broad = collect_hits(text, "broad_claim")
    if broad:
        warning_codes.append("WARN_BROAD_OR_UNIVERSAL_CLAIM")
        warnings.append("Broad/universal claim markers detected: " + ", ".join(broad[:5]))

    return fatal_codes, warning_codes, warnings


def integrated_judgment(layer_results: List[CheckResult], text: str) -> CheckResult:
    found = []
    missing = []
    reasons = []

    coord = next((r for r in layer_results if r.name.startswith("Layer 0")), None)
    dyn = next((r for r in layer_results if r.name.startswith("Layer 1")), None)
    tacit = next((r for r in layer_results if r.name.startswith("Layer 2")), None)
    explicit = next((r for r in layer_results if r.name.startswith("Layer 3")), None)

    if coord and coord.status == "SUSPEND":
        missing.append("stable coordinate base")
        reasons.append("INTEGRATED_COORDINATE_BASE_UNSTABLE")
    else:
        found.append("coordinate base is at least partially fixed")

    if dyn and dyn.status == "SUSPEND":
        missing.append("dynamic transition closure")
        reasons.append("INTEGRATED_DYNAMIC_CLOSURE_UNSTABLE")
    else:
        found.append("dynamic layer is not critically absent")

    if tacit and tacit.status == "SUSPEND":
        missing.append("tacit-knowledge closure")
        reasons.append("INTEGRATED_TACIT_CLOSURE_UNSTABLE")
    else:
        found.append("tacit layer is not critically absent")

    if explicit and explicit.status == "WARN":
        reasons.append("INTEGRATED_EXPLICIT_ARGUMENT_WEAK")
        missing.append("strong explicit inference/evidence markers")
    else:
        found.append("explicit argument layer has minimum markers or is not critical")

    contrast = collect_hits(text, "contrast_marker")
    uncertainty = collect_hits(text, "uncertainty")
    if contrast or uncertainty:
        found.append("limitation/uncertainty markers exist")
    else:
        missing.append("limitation or uncertainty markers")
        reasons.append("INTEGRATED_LIMITATION_MARKERS_MISSING")

    if reasons:
        status = "WARN"
        note = "Cross-layer stability is partial. Consider SUSPEND if the claim is high-impact."
    else:
        status = "PASS"
        note = "No major cross-layer instability detected by heuristic checks."

    return CheckResult(
        name="Layer 4: Integrated Judgment",
        status=status,
        found=found,
        missing=missing,
        reason_codes=reasons,
        note=note,
    )


def reservation_layer(layer_results: List[CheckResult], warnings: List[str]) -> CheckResult:
    missing = []
    reasons = []

    for result in layer_results:
        if result.status in {"SUSPEND", "WARN"}:
            missing.extend([f"{result.name}: {m}" for m in result.missing[:10]])
            reasons.extend(result.reason_codes)

    if warnings:
        missing.extend(warnings)
        reasons.append("RESERVATION_WARNINGS_PRESENT")

    if missing:
        status = "SUSPEND"
        note = "Items remain reserved or underdefined. Do not force PASS without additional closure."
    else:
        status = "PASS"
        note = "No major reserved items detected by heuristic checks."

    return CheckResult(
        name="Layer 5: Reservation / SUSPEND Layer",
        status=status,
        found=[] if missing else ["no major reserved item detected"],
        missing=missing[:30],
        reason_codes=sorted(set(reasons)),
        note=note,
    )


def audit_text(text: str) -> AuditReport:
    text = normalize(text)
    layer_results: List[CheckResult] = []
    total_score = 0
    max_score = 0

    for layer_name, keys in LAYER_REQUIREMENTS.items():
        result, score, max_layer_score = check_layer(text, layer_name, keys)
        layer_results.append(result)
        total_score += score
        max_score += max_layer_score

    fatal_codes, warning_codes, warnings = detect_failures_and_warnings(text)

    integrated = integrated_judgment(layer_results, text)
    layer_results.append(integrated)

    reservation = reservation_layer(layer_results, warnings)
    layer_results.append(reservation)

    reason_codes = []
    for result in layer_results:
        reason_codes.extend(result.reason_codes)
    reason_codes.extend(fatal_codes)
    reason_codes.extend(warning_codes)
    reason_codes = sorted(set(reason_codes))

    # Decision logic
    if fatal_codes:
        decision = "FAIL"
    elif any(r.status == "SUSPEND" for r in layer_results[:3]):
        decision = "SUSPEND"
    elif reservation.status == "SUSPEND" and total_score < int(max_score * 0.72):
        decision = "SUSPEND"
    elif total_score >= int(max_score * 0.72):
        decision = "PASS"
    else:
        decision = "SUSPEND"

    confidence_note = (
        "Heuristic audit only. This script detects markers and omissions; "
        "it does not determine truth or perform deep semantic verification."
    )

    reserved_items = reservation.missing

    metadata = {
        "tool": "tcp_argument_audit.py",
        "version": "v0.1.1-public",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "text_length": str(len(text)),
        "decision_model": "heuristic TCP application prototype",
    }

    return AuditReport(
        decision=decision,
        reason_codes=reason_codes,
        score=total_score,
        max_score=max_score,
        confidence_note=confidence_note,
        layer_results=layer_results,
        reserved_items=reserved_items,
        metadata=metadata,
    )


def report_to_dict(report: AuditReport) -> Dict[str, object]:
    return {
        "decision": report.decision,
        "score": report.score,
        "max_score": report.max_score,
        "reason_codes": report.reason_codes,
        "confidence_note": report.confidence_note,
        "metadata": report.metadata,
        "layers": [
            {
                "name": r.name,
                "status": r.status,
                "found": r.found,
                "missing": r.missing,
                "reason_codes": r.reason_codes,
                "note": r.note,
            }
            for r in report.layer_results
        ],
        "reserved_items": report.reserved_items,
    }


def render_markdown(report: AuditReport) -> str:
    lines: List[str] = []
    lines.append("# TCP Argument Audit Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Decision:** `{report.decision}`")
    lines.append(f"- **Score:** `{report.score} / {report.max_score}`")
    lines.append(f"- **Tool:** `{report.metadata.get('tool')}`")
    lines.append(f"- **Version:** `{report.metadata.get('version')}`")
    lines.append(f"- **Timestamp UTC:** `{report.metadata.get('timestamp_utc')}`")
    lines.append("")
    lines.append("## Boundary Note")
    lines.append("")
    lines.append(report.confidence_note)
    lines.append("")
    lines.append("This report evaluates closure markers and underdefined areas. It does not evaluate metaphysical truth.")
    lines.append("")
    lines.append("## Reason Codes")
    lines.append("")
    if report.reason_codes:
        for code in report.reason_codes:
            lines.append(f"- `{code}`")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Layer Results")
    lines.append("")
    for r in report.layer_results:
        lines.append(f"### {r.name}")
        lines.append("")
        lines.append(f"- **Status:** `{r.status}`")
        if r.note:
            lines.append(f"- **Note:** {r.note}")
        lines.append("")
        lines.append("**Found markers:**")
        if r.found:
            for item in r.found:
                lines.append(f"- {item}")
        else:
            lines.append("- None")
        lines.append("")
        lines.append("**Missing / reserved items:**")
        if r.missing:
            for item in r.missing:
                lines.append(f"- {item}")
        else:
            lines.append("- None")
        lines.append("")
        lines.append("**Reason codes:**")
        if r.reason_codes:
            for code in r.reason_codes:
                lines.append(f"- `{code}`")
        else:
            lines.append("- None")
        lines.append("")

    lines.append("## TCP Mapping")
    lines.append("")
    lines.append("| TCP element | Audit interpretation |")
    lines.append("|---|---|")
    lines.append("| `X` | Coordinate anchoring: speaker, agent, object, time, space, purpose, mechanism |")
    lines.append("| `R` | Dynamic transition and explicit argument relation |")
    lines.append("| `M` | Definition, premise, scope, uncertainty, judgment and stopping rule |")
    lines.append("| `SUSPEND` | Valid halt state for underdefined, unsafe, or unclosed claims |")
    lines.append("")
    return "\n".join(lines)


def read_input(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    if args.input_file:
        return Path(args.input_file).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("No input provided. Use --text, input_file, or stdin.")


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="TCP-style natural-language argument audit prototype."
    )
    parser.add_argument("input_file", nargs="?", help="Input text file. If omitted, stdin is used.")
    parser.add_argument("--text", help="Text to audit directly.")
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format. Default: markdown.",
    )
    parser.add_argument(
        "--output",
        help="Optional output file path. If omitted, prints to stdout.",
    )

    args = parser.parse_args(argv)
    text = read_input(args)
    report = audit_text(text)

    if args.format == "json":
        output = json.dumps(report_to_dict(report), ensure_ascii=False, indent=2)
    else:
        output = render_markdown(report)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
