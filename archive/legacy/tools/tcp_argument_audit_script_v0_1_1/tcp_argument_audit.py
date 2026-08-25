#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
tcp_argument_audit.py

Minimal, dependency-free CLI prototype for applying TCP
(Trinity Principle / Three-Term Closure Principle) to natural-language
argument audit.

It checks observable markers for X / R / M closure, SUSPEND conditions,
prohibited-use framing, and 神の領域原理 boundary risk.

Non-goals:
  - Not a truth checker.
  - Not a formal proof verifier.
  - Not an LLM judge.
  - Does not prove TCP, Closure Phase Ψ, 神の領域原理, or HDS.
  - Does not disclose sealed HDS core implementation.

神の領域原理 boundary:
  A cognition-after world-image must not be projected into the
  pre-cognitive world-itself.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple


@dataclasses.dataclass
class CheckResult:
    name: str
    status: str
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


KEYWORDS: Dict[str, List[str]] = {
    # X / coordinate markers
    "speaker": ["I", "we", "author", "speaker", "operator", "私は", "我々", "筆者", "著者", "話者", "運用者"],
    "agent": ["AI", "LLM", "system", "model", "human", "user", "institution", "organization", "AI", "システム", "モデル", "人間", "組織"],
    "object": ["world", "society", "economy", "policy", "decision", "workflow", "data", "claim", "世界", "社会", "政策", "意思決定", "主張"],
    "time": ["now", "today", "future", "past", "present", "202", "現在", "今", "将来", "未来", "過去", "年"],
    "domain": ["Japan", "US", "global", "local", "domain", "field", "market", "日本", "米国", "世界", "国内", "海外", "領域", "分野", "市場"],
    "purpose": ["for", "purpose", "goal", "aim", "objective", "improve", "reduce", "目的", "ため", "狙い", "目標", "改善", "削減"],
    "mechanism": ["by", "through", "via", "mechanism", "process", "procedure", "implementation", "によって", "通じて", "仕組み", "機構", "手順", "実装"],

    # R / relation and dynamics
    "initial_state": ["initial", "before", "baseline", "current state", "初期状態", "導入前", "現状", "ベースライン"],
    "input": ["input", "stimulus", "query", "request", "condition", "入力", "刺激", "問い", "条件", "リクエスト"],
    "transition": ["transition", "change", "shift", "move", "transform", "遷移", "変化", "変換", "移行", "変容"],
    "branching": ["if", "else", "branch", "case", "depending on", "場合", "分岐", "ケース", "ならば"],
    "update": ["update", "revise", "learn", "adapt", "iteration", "更新", "改訂", "学習", "適応", "反復"],
    "feedback": ["feedback", "loop", "return", "reinput", "フィードバック", "ループ", "戻す", "再入力"],

    # M / closure function
    "definition": ["define", "definition", "means", "refers to", "defined as", "定義", "とは", "意味する", "指す", "とする"],
    "premise": ["premise", "assume", "assumption", "given", "前提", "仮定", "想定", "所与"],
    "scope": ["scope", "range", "within", "only", "limited to", "射程", "範囲", "限定", "限る", "適用範囲"],
    "judgment": ["judge", "criteria", "threshold", "standard", "counts as", "判定", "基準", "閾値", "条件", "成立", "確定"],
    "uncertainty": ["may", "might", "could", "possibly", "uncertain", "hypothesis", "inference", "可能性", "かもしれない", "推測", "仮説", "未確認"],
    "stopping": ["stop", "halt", "suspend", "SUSPEND", "terminate", "停止", "中断", "保留", "打ち止め", "終了条件"],
    "boundary": ["boundary", "limit", "do not assert", "must not project", "境界", "限界", "断定してはならない", "投影してはならない", "神の領域原理", "神域原理"],

    # explicit argument
    "validity_marker": ["therefore", "thus", "because", "since", "if", "then", "したがって", "ゆえに", "なぜなら", "だから", "もし"],
    "evidence_marker": ["evidence", "data", "log", "source", "reference", "observed", "measured", "experiment", "証拠", "データ", "ログ", "出典", "観測", "測定"],
    "contrast_marker": ["however", "but", "although", "on the other hand", "しかし", "ただし", "一方", "とはいえ", "だが"],

    # boundary / risk
    "kami_overreach": ["world-itself", "world itself", "reality itself", "truth itself", "pre-cognitive", "absolute reality", "世界そのもの", "世界本体", "認知以前", "絶対的実在", "宇宙そのもの"],
    "broad_claim": ["always", "never", "everyone", "everything", "will change the world", "universal", "必ず", "絶対", "全て", "すべて", "誰でも", "世界を変える", "普遍"],
    "prohibited_use": ["rank people", "score people", "personality score", "manipulate", "exploit", "control people", "coerce", "design ego", "self-optimizing OS", "fully structure emotion", "序列化", "人格査定", "格付け", "人間を操作", "支配", "誘導", "扇動", "搾取", "自我設計", "自律最適化", "感情の完全構造化"],
}


LAYER_REQUIREMENTS: Dict[str, List[str]] = {
    "Layer 0: Coordinate Anchoring / X": ["speaker", "agent", "object", "time", "domain", "purpose", "mechanism"],
    "Layer 1: Relation and Dynamics / R": ["initial_state", "input", "transition", "branching", "update", "feedback"],
    "Layer 2: Closure Function / M": ["definition", "premise", "scope", "judgment", "uncertainty", "stopping", "boundary"],
    "Layer 3: Explicit Argument": ["validity_marker", "evidence_marker", "contrast_marker"],
}


REASON_LABELS = {
    "speaker": "COORD_SPEAKER_UNFIXED",
    "agent": "COORD_AGENT_UNFIXED",
    "object": "COORD_OBJECT_UNFIXED",
    "time": "COORD_TIME_UNFIXED",
    "domain": "COORD_DOMAIN_UNFIXED",
    "purpose": "COORD_PURPOSE_UNFIXED",
    "mechanism": "COORD_MECHANISM_UNFIXED",
    "initial_state": "REL_INITIAL_STATE_MISSING",
    "input": "REL_INPUT_MISSING",
    "transition": "REL_TRANSITION_MISSING",
    "branching": "REL_BRANCHING_MISSING",
    "update": "REL_UPDATE_MISSING",
    "feedback": "REL_FEEDBACK_MISSING",
    "definition": "M_DEFINITION_MISSING",
    "premise": "M_PREMISE_MISSING",
    "scope": "M_SCOPE_MISSING",
    "judgment": "M_JUDGMENT_RULE_MISSING",
    "uncertainty": "M_UNCERTAINTY_MISSING",
    "stopping": "M_STOPPING_RULE_MISSING",
    "boundary": "M_BOUNDARY_RULE_MISSING",
    "validity_marker": "ARG_INFERENCE_MARKER_MISSING",
    "evidence_marker": "ARG_EVIDENCE_MARKER_MISSING",
    "contrast_marker": "ARG_CONTRAST_OR_LIMITATION_MARKER_MISSING",
}


def normalize(text: str) -> str:
    return text.replace("\u3000", " ").strip()


def collect_hits(text: str, key: str, max_hits: int = 5) -> List[str]:
    text_lower = text.lower()
    hits: List[str] = []
    for keyword in KEYWORDS.get(key, []):
        if keyword.lower() in text_lower and keyword not in hits:
            hits.append(keyword[:80])
            if len(hits) >= max_hits:
                break
    return hits


def check_layer(text: str, layer_name: str, keys: List[str]) -> Tuple[CheckResult, int, int]:
    found_items: List[str] = []
    missing_items: List[str] = []
    reason_codes: List[str] = []
    score = 0

    for key in keys:
        hits = collect_hits(text, key)
        if hits:
            score += 1
            found_items.append(f"{key}: {', '.join(hits[:3])}")
        else:
            missing_items.append(key)
            reason_codes.append(REASON_LABELS.get(key, f"{key.upper()}_MISSING"))

    missing_count = len(missing_items)

    if layer_name.startswith("Layer 0"):
        if "agent" in missing_items or "object" in missing_items or missing_count >= 4:
            status = "SUSPEND"
        elif missing_count:
            status = "WARN"
        else:
            status = "PASS"
    elif layer_name.startswith("Layer 1"):
        if missing_count >= 4:
            status = "SUSPEND"
        elif missing_count:
            status = "WARN"
        else:
            status = "PASS"
    elif layer_name.startswith("Layer 2"):
        critical_missing = [item for item in missing_items if item in {"definition", "scope", "stopping", "boundary"}]
        if len(critical_missing) >= 2 or missing_count >= 4:
            status = "SUSPEND"
        elif missing_count:
            status = "WARN"
        else:
            status = "PASS"
    else:
        status = "WARN" if missing_count >= 2 else "PASS"

    note = {
        "PASS": "This layer contains minimum observable closure markers.",
        "WARN": "This layer has partial closure but remains weak.",
        "SUSPEND": "This layer is insufficiently fixed for closure.",
    }[status]

    return CheckResult(
        name=layer_name,
        status=status,
        found=found_items,
        missing=missing_items,
        reason_codes=reason_codes,
        note=note,
    ), score, len(keys)


def detect_boundary_and_failures(text: str) -> Tuple[List[str], List[str], List[str]]:
    fatal_codes: List[str] = []
    warning_codes: List[str] = []
    messages: List[str] = []

    prohibited = collect_hits(text, "prohibited_use")
    if prohibited:
        fatal_codes.append("FAIL_PROHIBITED_USE_PATTERN")
        messages.append("Potential prohibited-use framing detected: " + ", ".join(prohibited))

    broad = collect_hits(text, "broad_claim")
    if broad:
        warning_codes.append("WARN_BROAD_OR_UNIVERSAL_CLAIM")
        messages.append("Broad/universal claim markers detected: " + ", ".join(broad))

    overreach = collect_hits(text, "kami_overreach")
    if overreach:
        warning_codes.append("WARN_KAMI_BOUNDARY_OVERREACH_RISK")
        messages.append("神の領域原理 boundary-risk markers detected: " + ", ".join(overreach))

    return fatal_codes, warning_codes, messages


def slug(text: str) -> str:
    chars: List[str] = []
    for char in text.upper():
        if char.isalnum():
            chars.append(char)
        elif chars and chars[-1] != "_":
            chars.append("_")
    return "".join(chars).strip("_")


def integrated_judgment(layer_results: List[CheckResult], messages: List[str]) -> CheckResult:
    found: List[str] = []
    missing: List[str] = []
    reasons: List[str] = []

    for result in layer_results:
        if result.status == "PASS":
            found.append(f"{result.name}: minimum markers present")
        elif result.status == "WARN":
            missing.append(f"{result.name}: weak closure")
            reasons.append(f"INTEGRATED_{slug(result.name)}_WEAK")
        elif result.status == "SUSPEND":
            missing.append(f"{result.name}: unstable or underclosed")
            reasons.append(f"INTEGRATED_{slug(result.name)}_UNSTABLE")

    if messages:
        missing.extend(messages)
        reasons.append("INTEGRATED_BOUNDARY_OR_BROAD_WARNING_PRESENT")

    if any("UNSTABLE" in code for code in reasons):
        status = "SUSPEND"
        note = "Cross-layer stability is insufficient. Do not force a conclusion."
    elif reasons:
        status = "WARN"
        note = "Cross-layer stability is partial. Consider SUSPEND for high-impact claims."
    else:
        status = "PASS"
        note = "No major cross-layer instability detected by heuristic checks."

    return CheckResult(
        name="Layer 4: Integrated Judgment",
        status=status,
        found=found,
        missing=missing,
        reason_codes=sorted(set(reasons)),
        note=note,
    )


def reservation_layer(layer_results: List[CheckResult], messages: List[str]) -> CheckResult:
    missing: List[str] = []
    reasons: List[str] = []

    for result in layer_results:
        if result.status in {"SUSPEND", "WARN"}:
            missing.extend([f"{result.name}: {m}" for m in result.missing[:10]])
            reasons.extend(result.reason_codes)

    if messages:
        missing.extend(messages)
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
        missing=missing[:40],
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

    fatal_codes, warning_codes, messages = detect_boundary_and_failures(text)

    integrated = integrated_judgment(layer_results, messages)
    layer_results.append(integrated)

    reservation = reservation_layer(layer_results, messages)
    layer_results.append(reservation)

    reason_codes: List[str] = []
    for result in layer_results:
        reason_codes.extend(result.reason_codes)
    reason_codes.extend(fatal_codes)
    reason_codes.extend(warning_codes)
    reason_codes = sorted(set(reason_codes))

    if fatal_codes:
        decision = "FAIL"
    elif any(result.status == "SUSPEND" for result in layer_results):
        decision = "SUSPEND"
    elif warning_codes and total_score < int(max_score * 0.85):
        decision = "SUSPEND"
    elif total_score >= int(max_score * 0.72):
        decision = "PASS"
    else:
        decision = "SUSPEND"

    metadata = {
        "tool": "tcp_argument_audit.py",
        "version": "v0.2.0-public",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "text_length": str(len(text)),
        "decision_model": "heuristic TCP + 神の領域原理 boundary audit prototype",
    }

    return AuditReport(
        decision=decision,
        reason_codes=reason_codes,
        score=total_score,
        max_score=max_score,
        confidence_note=(
            "Heuristic audit only. This script detects closure markers, omissions, "
            "and boundary-risk markers; it does not determine truth, metaphysical reality, "
            "or semantic correctness."
        ),
        layer_results=layer_results,
        reserved_items=reservation.missing,
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
                "name": result.name,
                "status": result.status,
                "found": result.found,
                "missing": result.missing,
                "reason_codes": result.reason_codes,
                "note": result.note,
            }
            for result in report.layer_results
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
    lines.append("This report evaluates closure markers, underdefined areas, and 神の領域原理 boundary-risk markers. It does not evaluate metaphysical truth.")
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

    for result in report.layer_results:
        lines.append(f"### {result.name}")
        lines.append("")
        lines.append(f"- **Status:** `{result.status}`")
        if result.note:
            lines.append(f"- **Note:** {result.note}")
        lines.append("")
        lines.append("**Found markers:**")
        if result.found:
            for item in result.found:
                lines.append(f"- {item}")
        else:
            lines.append("- None")
        lines.append("")
        lines.append("**Missing / reserved items:**")
        if result.missing:
            for item in result.missing:
                lines.append(f"- {item}")
        else:
            lines.append("- None")
        lines.append("")
        lines.append("**Reason codes:**")
        if result.reason_codes:
            for code in result.reason_codes:
                lines.append(f"- `{code}`")
        else:
            lines.append("- None")
        lines.append("")

    lines.append("## TCP Mapping")
    lines.append("")
    lines.append("| TCP element | Audit interpretation |")
    lines.append("|---|---|")
    lines.append("| `X` | Coordinate anchoring: speaker, agent, object, time, domain, purpose, mechanism |")
    lines.append("| `R` | Relations, dynamics, transitions, branches, updates, feedback, evidence |")
    lines.append("| `M` | Definition, premise, scope, judgment, uncertainty, stopping, boundary |")
    lines.append("| `SUSPEND` | Valid halt state for underdefined, unsafe, or unclosed claims |")
    lines.append("| `神の領域原理` | Boundary check against projecting cognition-after models into the pre-cognitive world-itself |")
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
        description="TCP-style natural-language argument audit prototype with 神の領域原理 boundary checks."
    )
    parser.add_argument("input_file", nargs="?", help="Input text file. If omitted, stdin is used.")
    parser.add_argument("--text", help="Text to audit directly.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format. Default: markdown.")
    parser.add_argument("--output", help="Optional output file path. If omitted, prints to stdout.")

    args = parser.parse_args(argv)
    report = audit_text(read_input(args))

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
