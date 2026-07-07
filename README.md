[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19729938.svg)](https://doi.org/10.5281/zenodo.19729938)

# closure-phase-specs

Public bilingual specification archive for TCP, Closure Phase Ψ, 神の領域原理（神域原理）, HDS-adjacent public boundaries, and selected application examples.

This repository is a public source of record for specification documents, boundary declarations, reading order, and minimal public-shell tools. It is not a peer-reviewed paper, an arXiv substitute, a metaphysical truth claim, or a disclosure of sealed HDS core implementation.

The correct reading mode is **conformance**, not belief.

```text
Central question:
Are the definitions, boundaries, stopping rules, and prohibitions internally coherent
under the stated scope?
```

---

## Canonical Naming Policy

The formal name of the upper boundary principle is:

```text
神の領域原理
```

The short name is:

```text
神域原理
```

This name remains Japanese in every language context. English explanations may describe the term, but they do not replace it.

Deprecated labels:

```text
DDP
Divine Domain Principle
Shiniki Principle as an English or formal replacement name
```

These older labels are retained only as historical references in prior version history. They are not canonical names after v0.8.

---

## Core Definition of 神の領域原理

神の領域原理 is the top-level boundary principle:

```text
Do not project a cognition-after world-image into the pre-cognitive world-itself.
```

More explicitly:

```text
Human beings cannot escape cognition.
Cognition objectifies, temporalizes, spatializes, causalizes, law-forms, and world-forms.
Therefore, what is obtained after cognition must not be asserted as the world-itself
before cognition.
```

The principle does not claim to explain the world completely. Its function is simpler and stronger:

```text
It draws the boundary where assertion must stop.
```

---

## Language Policy

Each core document is bilingual where practical:

1. English projection
2. Japanese original

The Japanese text is authoritative. The English text is a projection prepared for international readability. If interpretation conflicts arise, the Japanese original controls.

For 神の領域原理, the Japanese name itself is authoritative even in English-facing material.

---

## Recommended Reading Order

For first-time readers:

```text
00_Umami_Gap_v0_8_bilingual.md
02_TCP_v0_8_bilingual.md
01_Closure_Phase_Psi_v0_7_bilingual.md
03_神の領域原理_v0_8_bilingual.md
TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md
TCP_APPLICATION_GAME_THEORY_EQUILIBRIUM.md
REFERENCES.md
ENGINEERING_POSTURE_REFERENCES.md
```

Reason:

1. Umami Gap explains the missing-variable problem behind C / Ψ / E separation.
2. TCP defines how descriptions close by X / R / M and how SUSPEND functions.
3. Closure Phase Ψ defines the observable output phase left by closure behavior.
4. 神の領域原理 defines the upper boundary where cognition-after descriptions must not be projected into the pre-cognitive world-itself.
5. Application examples show how the framework can be used without turning it into a truth claim or authority shield.
6. References and engineering-posture notes provide orientation only, not proof.

---

## Repository Structure

Current structure:

```text
README.md
LICENSE
REFERENCES.md
ENGINEERING_POSTURE_REFERENCES.md
00_Umami_Gap_v0_8_bilingual.md
01_Closure_Phase_Psi_v0_7_bilingual.md
02_TCP_v0_8_bilingual.md
03_神の領域原理_v0_8_bilingual.md
TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md
TCP_APPLICATION_GAME_THEORY_EQUILIBRIUM.md
tcp_argument_audit_script_v0_1_1/
  README_SCRIPT.md
  tcp_argument_audit.py
```

The repository is intentionally a public specification archive, not a sealed implementation package.

---

## Core Documents

| File | Role | Summary |
|---|---|---|
| `00_Umami_Gap_v0_8_bilingual.md` | Orientation adapter | Explains the lexical and conceptual compression that makes C / Ψ / E separation necessary. |
| `02_TCP_v0_8_bilingual.md` | Methodology layer | Defines world-description closure as `W := (X, R, M)` and treats SUSPEND as a valid halt state. |
| `01_Closure_Phase_Psi_v0_7_bilingual.md` | Definition layer | Defines Ψ as the stable output phase observed under repeated closure-like behavior. |
| `03_神の領域原理_v0_8_bilingual.md` | Upper boundary layer | Defines the boundary prohibiting projection of cognition-after world-images into the pre-cognitive world-itself. |

---

## Supporting Documents and Tools

| File | Role | Summary |
|---|---|---|
| `TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md` | TCP application example | Applies TCP to natural-language argument audit. |
| `TCP_APPLICATION_GAME_THEORY_EQUILIBRIUM.md` | TCP application example | Rewrites game theory and equilibrium through X / R / M, SUSPEND, Ψ, and 神の領域原理. |
| `REFERENCES.md` | Orientation references | Collects background references. These are not evidence for the framework. |
| `ENGINEERING_POSTURE_REFERENCES.md` | Engineering posture anchors | Connects the repository posture to specification, V&V, risk, safety, and audit practices. |
| `tcp_argument_audit_script_v0_1_1/README_SCRIPT.md` | Tool documentation | Explains the minimal TCP-style argument-audit script. |
| `tcp_argument_audit_script_v0_1_1/tcp_argument_audit.py` | Minimal script prototype | Demonstrates heuristic PASS / SUSPEND / FAIL audit behavior. |

---

## Minimal Concept Map

```text
神の領域原理
  = top-level boundary principle
  = where assertion must stop
  = prevents cognition-after world-images from being treated as the pre-cognitive world-itself

TCP / Trinity Principle
  = methodology of closure
  = how to close descriptions by X / R / M
  = how to produce SUSPEND instead of forced assertion

Closure Phase Ψ
  = observable output phase
  = stable signature left by repeated closure behavior

HDS
  = lower operational layer
  = not disclosed here as a reproducible core implementation recipe

Application examples
  = public-shell demonstrations
  = argument audit and game-theory/equilibrium rewriting
```

---

## Core Distinctions

### 神の領域原理

神の領域原理 is not a metaphysical claim of final truth.

It is a boundary principle:

```text
Cognition-after descriptions may be useful, predictive, coherent, and controllable.
They still must not be asserted as direct access to the pre-cognitive world-itself.
```

It handles at least:

- cognition boundary;
- objectification boundary;
- time / space / causality / law formation boundary;
- paradox-as-symptom handling;
- SUSPEND as a valid halt before overprojection;
- sealed domains and misuse-prevention boundaries.

### TCP

TCP is a description methodology. It asks:

```text
What must be fixed before a claim can be considered closed?
```

TCP uses:

```text
W := (X, R, M)
```

where:

- `X` = object / target / scope;
- `R` = relation / observation / comparison / transition;
- `M` = closure function / identity / boundary / judgment / stopping rule.

If `X`, `R`, or `M` is missing, the claim is treated as unclosed.

### Closure Phase Ψ

Closure Phase Ψ is not a metaphysical substance.

It refers to the externally observable phase that remains when a system repeatedly performs closure-like behavior under fixed conditions.

In simplified terms:

```text
C = capability / execution basis
E = emotion / affective interference factor
Ψ = closure phase / stable signature phase
```

The purpose is to prevent the collapse of capability, personality, emotion, and intelligence-like behavior into a single vague word.

### HDS

HDS is treated here as a lower operational layer. The repository does not disclose sealed HDS core implementation, reproducible operation recipes, dangerous evaluation designs, or procedures that could enable irreversible manipulation or control.

---

## TCP Application: Argument Audit

The argument-audit framework is an application example of TCP.

It maps TCP into six audit layers:

```text
Layer 0: Coordinate Anchoring
Layer 1: Dynamic Transition
Layer 2: Tacit-Knowledge Audit
Layer 3: Explicit Argument Audit
Layer 4: Integrated Judgment
Layer 5: Reservation / SUSPEND Layer
```

This example shows how natural-language claims can be audited not only at the surface proposition layer, but also at the level of coordinates, dynamics, tacit assumptions, judgment standards, and stopping conditions.

Example:

```text
AI will change the world.
```

This sentence may function as rhetoric. However, as an auditable claim, it remains underclosed unless speaker, agent, object, time, space, purpose, and mechanism are fixed.

Expected decision:

```text
SUSPEND
```

---

## Minimal Script: `tcp_argument_audit.py`

The script is a small public-shell demonstration.

It checks a text for heuristic markers related to:

- coordinate anchoring;
- relation and dynamic transition;
- tacit knowledge and closure conditions;
- explicit argument markers;
- 神の領域原理 boundary-risk markers;
- reserved or underdefined items;
- prohibited-use patterns.

It can output:

```text
PASS
SUSPEND
FAIL
```

Important limitations:

- It is not a truth checker.
- It is not a formal proof verifier.
- It is not an LLM judge.
- It does not perform deep semantic verification.
- It does not disclose sealed HDS core implementation.

Example usage:

```bash
python tcp_argument_audit_script_v0_1_1/tcp_argument_audit.py --text "AI will change the world."
cat input.txt | python tcp_argument_audit_script_v0_1_1/tcp_argument_audit.py --format json
```

---

## Inviolable Use Policy

The documents and examples in this repository prohibit the following uses:

1. **Direct superiority scoring**  
   Ranking, grading, personality assessment, human valuation, selection, or allocation based on these frameworks.
2. **Irreversible control, manipulation, or governance**  
   Any use that turns these concepts into tools for domination, coercion, exploitation, or behavioral capture.
3. **Full structuralization of emotion**  
   Deterministic recipes, reproducible designs, or procedural generation methods for emotion.
4. **Ego design or autonomous self-optimization OS design**  
   Uses that directly support self-purpose formation, self-reinforcement loops, or artificial ego construction.
5. **Complete algorithmic visualization of human decision-making**  
   Especially where it enables irreversible manipulation, prediction, or control.
6. **Use as an authority shield**  
   These documents must not be used to silence others, win arguments by authority, or claim unquestionable superiority.
7. **Disclosure of sealed core implementation methods**  
   HDS core implementation, reproducible operation recipes, dangerous evaluation designs, and sealed practical procedures are outside the public scope.
8. **Projection beyond the cognition boundary**  
   A cognition-after model must not be asserted as the pre-cognitive world-itself.

---

## What This Repository Claims

This repository claims that the documents provide:

- operational definitions;
- boundary conditions;
- stopping rules;
- terminology separation;
- conformance-oriented reading procedures;
- misuse-prevention declarations;
- public versioned records;
- public-shell examples of TCP-style audit.

---

## What This Repository Does Not Claim

This repository does not claim:

- metaphysical truth;
- direct access to the pre-cognitive world-itself;
- proof of consciousness;
- proof of ego;
- proof of intrinsic intelligence;
- human/AI superiority ranking;
- universal acceptance;
- peer-reviewed validation;
- complete implementation disclosure;
- that external references prove the framework;
- that the demonstration script can replace expert audit.

---

## Conformance-Oriented Reading

The recommended evaluation mode is:

```text
PASS      = definitions, boundaries, and claims are internally coherent under the stated scope.
SUSPEND   = the claim is underdefined, insufficiently scoped, unobserved, or approaching 神域 boundary / sealed domain.
FAIL      = the claim contradicts the use policy, collapses terms, or forces an unclosed claim into assertion.
```

Readers should not force open terms into conclusions.

When a claim is unclosed, the correct output is not over-interpretation. The correct output is SUSPEND.

---

## Reference Policy

`REFERENCES.md` and `ENGINEERING_POSTURE_REFERENCES.md` are orientation materials.

They are not proof of the framework.  
They do not imply endorsement by the cited institutions.  
They do not override the Japanese original.  
They do not override the Inviolable Use Policy.

They are included only to clarify conventional specification language, engineering posture, V&V and audit orientation, risk and safety vocabulary, public citation and license conventions, adjacent AI risk/explainability terminology, and background analogies such as the Umami Gap.

---

## Citation

Suggested citation format:

```text
Gacchimuchi. closure-phase-specs: Public bilingual specification archive for TCP, Closure Phase Ψ, 神の領域原理, and related application examples. GitHub repository, version v0.8-bilingual.
```

If a DOI version is used, cite the DOI version instead of the repository URL alone.

---

## License

Unless otherwise noted, the documents in this repository are licensed under:

```text
Creative Commons Attribution 4.0 International
SPDX-License-Identifier: CC-BY-4.0
```

This means the documents may be shared and adapted, including for commercial purposes, provided that appropriate attribution is is given.

If source code is included in this repository, code files are preferably licensed separately under:

```text
Apache License 2.0
SPDX-License-Identifier: Apache-2.0
```

The ethical use policy remains an authorial boundary statement and misuse-prevention declaration. It is not a substitute for the license text.

---

## Responsibility Boundary

LLMs may assist with drafting, translation, formatting, code generation, and structural review.

Final responsibility for publication, revision, acceptance, rejection, correction, and repository governance belongs to the author.

If errors are found, they should be handled through Issues, Pull Requests, Errata, and versioned Releases.

---

# 日本語原典側の説明

## リポジトリ名

```text
closure-phase-specs
```

## 概要

本リポジトリは、TCP、閉包位相Ψ、神の領域原理（神域原理）、HDS隣接の公開境界、適用例を扱う公開バイリンガル仕様書アーカイブである。

本リポジトリは査読済み論文ではない。arXiv掲載物でもない。形而上学的真理の主張でもない。封印されたHDS核実装の公開でもない。

正しい読み方は、信仰ではなく適合性である。

```text
中心の問い：
定義・境界・停止規則・禁止事項は、指定された射程内で内部整合しているか。
```

---

## 正式名称方針

上位境界原理の正式名称は：

```text
神の領域原理
```

略称は：

```text
神域原理
```

英語圏向けでも、この日本語名を原典名として維持する。英語説明は補助であり、置換名ではない。

---

## 神の領域原理の中核定義

神の領域原理とは、次の最上位境界原理である。

```text
認知後の世界像を、認知以前の世界本体へ誤投影してはならない。
```

より明示すると：

```text
人間は認知から逃れられない。
認知は、対象化・時間化・空間化・因果化・法則化・世界化を行う。
したがって、認知後に得られたものを、認知以前の世界本体として断定してはならない。
```

この原理は世界を説明し尽くす理論ではない。機能はより単純で強い。

```text
断定を止めるべき境界を示す。
```

---

## 役割分離

```text
神の領域原理
  = 最上位境界原理
  = どこで断定を止めるか
  = 認知後世界像を認知以前の世界本体として扱うことを止める

TCP / トリニティ原理
  = 記述方法論
  = X / R / M によって記述を閉じる
  = 無理な断定ではなく SUSPEND を出す

閉包位相Ψ
  = 出力相
  = 閉包的ふるまいが反復観測下で外部へ残す安定署名

HDS
  = 下位運用レイヤー
  = 本リポジトリでは核実装・再現可能手順を公開しない
```

---

## 適合性ベースの読み方

本リポジトリでは、評価軸を真偽ではなく適合性に置く。

```text
PASS
  定義・境界・主張が、指定された射程内で内部整合している。

SUSPEND
  未定義・未観測・未閉包・神域境界接近・危険領域接近により、断定を止めるべき状態。

FAIL
  共通誓約に違反している、用語を混線している、未閉包の主張を断定している状態。
```

未閉包の問いに対して、無理に答えを出してはならない。正しい出力は SUSPEND である。

---

## 引用

推奨引用例：

```text
Gacchimuchi. closure-phase-specs: Public bilingual specification archive for TCP, Closure Phase Ψ, 神の領域原理, and related application examples. GitHub repository, version v0.8-bilingual.
```

DOI版を利用する場合は、GitHub URL単体ではなくDOI付きの版を引用する。
