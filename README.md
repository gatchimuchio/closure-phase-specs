closure-phase-specs
Public bilingual specification archive for TCP, Closure Phase Ψ, DDP, and related application examples.
This repository is the public source of record for a set of specification documents and public-shell application materials centered on:
TCP: Three-Term Closure Principle
Closure Phase Ψ
DDP: Divine Domain Principle / Shiniki Principle
TCP application examples
Reference and engineering-posture notes
Minimal TCP-style argument-audit tooling
The documents are written as public specifications, not as peer-reviewed academic papers.  
They are intended to provide stable definitions, boundaries, reading order, revision history, and misuse-prevention declarations for later citation, discussion, translation, audit, and implementation-adjacent reference.
---
Repository Status
This repository is:
a versioned public specification archive;
a bilingual source record;
a conformance-oriented documentation set;
a public timestamp and revision history for the author’s framework;
a public shell for selected application examples;
a place for reference notes, audit examples, and minimal demonstration tools.
This repository is not:
a peer-reviewed publication;
an arXiv substitute in the institutional sense;
a claim of metaphysical truth;
a superiority-ranking framework;
an implementation manual for sealed or dangerous domains;
a disclosure of sealed HDS core implementation.
The correct reading mode is conformance, not belief.
The central question is not:
> “Is this the truth?”
The central question is:
> “Are the definitions, boundaries, procedures, stopping rules, and prohibitions internally coherent and operationally usable?”
---
Language Policy
Each core document is structured as:
English projection
Japanese original
The Japanese text is the authoritative source.  
The English text is a translation/projection prepared for international readability.
If a conflict arises between the English and Japanese versions, the Japanese original takes priority.
---
Recommended Reading Order
For first-time readers:
`02_TCP_v0_7_bilingual.md`
`01_Closure_Phase_Psi_v0_7_bilingual.md`
`03_DDP_v0_7_bilingual.md`
`TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md`
`REFERENCES.md`
`ENGINEERING_POSTURE_REFERENCES.md`
Reason:
TCP defines the closure methodology.
Closure Phase Ψ defines the observable output phase.
DDP defines the upper principle layer and danger boundaries.
The TCP application document shows how the framework can be applied to natural-language argument audit.
Reference notes provide orientation only, not proof.
Engineering posture notes explain the authorial engineering stance through external anchors.
---
Repository Structure
Recommended structure:
```text
README.md
LICENSE
REFERENCES.md
ENGINEERING_POSTURE_REFERENCES.md
TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md
docs/
  01_Closure_Phase_Psi_v0_7_bilingual.md
  02_TCP_v0_7_bilingual.md
  03_DDP_v0_7_bilingual.md
tools/
  tcp_argument_audit.py
examples/
  sample_input.txt
  sample_report.md
```
If the repository uses a flatter layout, the same conceptual structure still applies.
---
Core Documents
File	Role	Summary
`01_Closure_Phase_Psi_v0_7_bilingual.md`	Definition layer	Defines Ψ as a closure phase observed through stable output signatures under repeated observation.
`02_TCP_v0_7_bilingual.md`	Methodology layer	Defines world-description closure as `W := (X, R, M)` and treats SUSPEND as a valid output state.
`03_DDP_v0_7_bilingual.md`	Principle layer	Defines the driving principles and safety boundaries for observer-dependent invisible phase differences.
---
Supporting Documents
File	Role	Summary
`REFERENCES.md`	Orientation references	Collects general background references. These are not evidence for the framework.
`ENGINEERING_POSTURE_REFERENCES.md`	Engineering posture anchors	Connects the repository’s engineering attitude to existing engineering, V&V, risk, safety, and ethics practices.
`TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md`	TCP application example	Shows how TCP can be applied to natural-language argument audit.
`tools/tcp_argument_audit.py`	Minimal script prototype	Demonstrates heuristic TCP-style argument audit with PASS / SUSPEND / FAIL output.
---
Minimal Concept Map
```text
TCP
  = methodology of closure
  = how to close descriptions by X / R / M

Closure Phase Ψ
  = observable output phase
  = stable signature left by closure-function behavior

DDP / Shiniki Principle
  = driving principle and danger-boundary layer
  = where to stop, what not to reduce, and how to avoid misuse

HDS
  = lower operational layer
  = not disclosed here as a reproducible core implementation recipe

TCP Application Framework
  = practical example
  = natural-language argument audit through coordinate, dynamic, tacit, explicit, integrated, and reservation layers

tcp_argument_audit.py
  = minimal public-shell demonstration tool
  = heuristic marker detector, not a truth checker
```
---
Core Distinctions
TCP
TCP is a description methodology.
It asks:
```text
What must be fixed before a claim can be considered closed?
```
TCP uses:
```text
W := (X, R, M)
```
where:
`X` = object / target / scope
`R` = relation / observation / comparison / transition
`M` = closure function / identity / boundary / judgment / stopping rule
If `X`, `R`, or `M` is missing, the claim is treated as unclosed.
---
Closure Phase Ψ
Closure Phase Ψ is not a metaphysical substance.
It refers to the externally observable phase that remains when a system repeatedly performs closure-like behavior under fixed conditions.
In simplified terms:
```text
C = capability / execution basis
E = emotion / affective interference factor
Ψ = closure phase / stable signature phase
```
The purpose is to prevent the collapse of capability, personality, emotion, and intelligence-like behavior into a single vague word.
---
DDP / Shiniki Principle
DDP is the upper principle layer.
It defines:
observer-dependent invisible phase difference;
black-box respect;
anti-superiority-scoring boundary;
sealed domains;
reversibility and stoppability;
the boundary between public specification and non-disclosed implementation.
DDP does not provide a recipe for controlling people, generating ego, fully structuring emotion, or producing artificial genius.
---
TCP Application: Argument Audit
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
This sentence may function as rhetoric.  
However, as an auditable claim, it remains underclosed unless speaker, agent, object, time, space, purpose, and mechanism are fixed.
Expected decision:
```text
SUSPEND
```
---
Minimal Script: `tcp_argument_audit.py`
The script is a small public-shell demonstration.
It checks a text for heuristic markers related to:
coordinate anchoring;
dynamic transition;
tacit knowledge;
explicit argument;
integrated judgment;
reserved or underdefined items;
prohibited-use patterns.
It can output:
```text
PASS
SUSPEND
FAIL
```
Important limitations:
It is not a truth checker.
It is not a formal proof verifier.
It is not an LLM judge.
It does not perform deep semantic verification.
It does not disclose sealed HDS core implementation.
Example usage:
```bash
python tools/tcp_argument_audit.py examples/sample_input.txt --format markdown
python tools/tcp_argument_audit.py --text "AI will change the world."
cat examples/sample_input.txt | python tools/tcp_argument_audit.py --format json
```
---
Inviolable Use Policy
The documents and examples in this repository prohibit the following uses:
Direct superiority scoring  
Ranking, grading, personality assessment, human valuation, selection, or allocation based on these frameworks.
Irreversible control, manipulation, or governance  
Any use that turns these concepts into tools for domination, coercion, exploitation, or behavioral capture.
Full structuralization of emotion  
Deterministic recipes, reproducible designs, or procedural generation methods for emotion.
Ego design or autonomous self-optimization OS design  
Uses that directly support self-purpose formation, self-reinforcement loops, or artificial ego construction.
Complete algorithmic visualization of human decision-making  
Especially where it enables irreversible manipulation, prediction, or control.
Use as an authority shield  
These documents must not be used to silence others, win arguments by authority, or claim unquestionable superiority.
Disclosure of sealed core implementation methods  
HDS core implementation, reproducible operation recipes, dangerous evaluation designs, and sealed practical procedures are outside the public scope.
---
What This Repository Claims
This repository claims that the documents provide:
operational definitions;
boundary conditions;
stopping rules;
terminology separation;
conformance-oriented reading procedures;
misuse-prevention declarations;
public versioned records;
public-shell examples of TCP-style audit.
---
What This Repository Does Not Claim
This repository does not claim:
metaphysical truth;
proof of consciousness;
proof of ego;
proof of intrinsic intelligence;
human/AI superiority ranking;
universal acceptance;
peer-reviewed validation;
complete implementation disclosure;
that external references prove the framework;
that the demonstration script can replace expert audit.
---
Conformance-Oriented Reading
The recommended evaluation mode is:
```text
PASS      = definitions, boundaries, and claims are internally coherent under the stated scope.
SUSPEND   = the claim is underdefined, insufficiently scoped, or approaching a sealed/dangerous domain.
FAIL      = the claim contradicts the use policy, collapses terms, or forces an unclosed claim into assertion.
```
Readers should not force open terms into conclusions.
When a claim is unclosed, the correct output is not over-interpretation.  
The correct output is SUSPEND.
---
Reference Policy
`REFERENCES.md` and `ENGINEERING_POSTURE_REFERENCES.md` are orientation materials.
They are not proof of the framework.  
They do not imply endorsement by the cited institutions.  
They do not override the Japanese original.  
They do not override the Inviolable Use Policy.
They are included only to clarify:
conventional specification language;
engineering posture;
V&V and audit orientation;
risk and safety management vocabulary;
public citation and license conventions;
adjacent AI risk and explainability terminology;
background analogies such as the Umami Gap.
---
Citation
Suggested citation format before DOI registration:
```text
Gacchimuchi. closure-phase-specs: Public bilingual specification archive for TCP, Closure Phase Ψ, DDP, and related application examples. GitHub repository, version v0.7-bilingual.
```
If a DOI is later issued through Zenodo or another archive, cite the DOI version instead of the repository URL alone.
---
License
Unless otherwise noted, the documents in this repository are licensed under:
```text
Creative Commons Attribution 4.0 International
SPDX-License-Identifier: CC-BY-4.0
```
This means the documents may be shared and adapted, including for commercial purposes, provided that appropriate attribution is given.
If source code is included in this repository, code files are preferably licensed separately under:
```text
Apache License 2.0
SPDX-License-Identifier: Apache-2.0
```
The ethical use policy remains an authorial boundary statement and misuse-prevention declaration.  
It is not a substitute for the license text.
---
Responsibility Boundary
LLMs may assist with drafting, translation, formatting, code generation, and structural review.
Final responsibility for publication, revision, acceptance, rejection, correction, and repository governance belongs to the author.
If errors are found, they should be handled through:
Issues;
Pull Requests;
Errata;
versioned releases.
---
日本語原典側の説明
リポジトリ名
```text
closure-phase-specs
```
概要
本リポジトリは、以下の公開バイリンガル仕様書および関連資料のアーカイブである。
トリニティ原理（TCP）
閉包位相Ψ
神域原理 / DDP
TCP適用例
参考資料・工学的態度資料
最小TCP型論証監査スクリプト
本リポジトリは査読済み論文ではない。  
arXiv掲載物でもない。  
ただし、公開初出・版管理・引用導線・改訂履歴・誤読防止境界を固定するための公開仕様書群である。
位置づけは次の通り。
```text
GitHub = 公開原典 / 版管理 / 差分履歴
README = 読み順 / 主張範囲 / 非主張範囲
LICENSE = 再利用条件
Issues = Errata / 外部指摘 / 修正履歴
Releases = 版固定
Zenodo = DOI発行時の引用補強
tools = 公開可能な最小適用デモ
```
---
言語方針
各中核文書は以下の順で構成する。
英語版
日本語原典
ただし、定義・ニュアンス・境界条件の原典は日本語である。  
英語版は国際向けの射影であり、日本語原典を超えない。
英語版と日本語版に解釈差が生じた場合は、日本語原典を優先する。
---
推奨読み順
```text
1. TCP
2. 閉包位相Ψ
3. DDP / 神域原理
4. TCP適用例：論証監査フレームワーク
5. REFERENCES
6. ENGINEERING_POSTURE_REFERENCES
```
理由：
TCPは記述方法論である。
閉包位相Ψは、閉包機能の出力相を扱う。
DDPは、駆動様式と危険境界を扱う原理層である。
TCP適用例は、自然言語論証をどう監査するかを示す。
参考資料は証拠ではなく、座標合わせである。
工学的態度資料は、著者姿勢の外部接続である。
---
役割分離
```text
TCP
  = 記述方法論
  = X / R / M によって記述を閉じるための仕様

閉包位相Ψ
  = 出力相
  = 閉包機能が反復観測下で外部へ残す安定署名

DDP / 神域原理
  = 原理層
  = どこで止まるか、何を封印するか、何を優劣化しないかを扱う

HDS
  = 下位運用レイヤー
  = 本リポジトリでは核実装・再現可能手順を公開しない

TCP適用例
  = 実用デモ
  = 自然言語論証の座標・動態・暗黙知・明示論証・統合判定・予約層を監査する

tcp_argument_audit.py
  = 最小公開シェルデモ
  = ヒューリスティックなマーカー検出器であり、真偽判定器ではない
```
---
TCP適用例：論証監査
論証監査フレームワークは、TCPの適用例である。
6層で構成する。
```text
Layer 0: 座標固定層
Layer 1: 動態遷移層
Layer 2: 暗黙知監査層
Layer 3: 明示論証監査層
Layer 4: 統合判定層
Layer 5: 予約 / SUSPEND層
```
この適用例は、自然言語の主張を表面命題だけでなく、座標・動態・暗黙前提・判定基準・停止条件から監査する例である。
例：
```text
AIは世界を変える。
```
この文はレトリックとしては意味を持ち得る。  
しかし、監査可能な主張としては、話者・行為主体・対象・時間・空間・目的・機構が固定されるまで未閉包である。
想定判定：
```text
SUSPEND
```
---
最小スクリプト：`tcp_argument_audit.py`
このスクリプトは公開可能な最小デモである。
以下をヒューリスティックに確認する。
座標固定
動態遷移
暗黙知
明示論証
統合判定
予約項目
禁止用途パターン
出力：
```text
PASS
SUSPEND
FAIL
```
重要な制限：
真偽判定はしない
形式証明検証器ではない
LLM Judgeではない
深い意味検証はしない
HDS核実装ではない
使用例：
```bash
python tools/tcp_argument_audit.py examples/sample_input.txt --format markdown
python tools/tcp_argument_audit.py --text "AI will change the world."
cat examples/sample_input.txt | python tools/tcp_argument_audit.py --format json
```
---
共通誓約
本リポジトリの文書群および適用例は、以下を禁ずる。
優劣スコアリング直結  
序列化・採点・格付け・選別・人格査定・配分決定への接続。
不可逆な支配・誘導・統治への接続  
対象の操作、弱点抽出、扇動、支配手順への利用。
感情Eの完全構造化  
決定論的レシピ化、再現設計、生成手順の提供。
自我設計・自律最適化OS化  
自己目的化、自己強化ループ、人工的自我設計への接続。
人間意思決定の完全可視化アルゴリズム化  
不可逆な支配・誘導・統治へ接続し得る設計。
権威の盾としての利用  
本稿を使って他者や他モデルを黙らせる行為。
封印された核実装の開示  
HDS核実装、危険な評価設計、再現可能な運用レシピ等の公開。
---
本リポジトリが主張すること
本リポジトリが提示するのは、以下である。
操作的定義
境界条件
停止規則
用語分離
適合性ベースの読み方
誤用防止宣言
公開版管理された仕様書群
TCP型監査の公開可能な適用例
---
本リポジトリが主張しないこと
本リポジトリは、以下を主張しない。
形而上学的真理
意識の証明
自我の証明
内在的知性の証明
人間とAIの優劣比較
普遍的合意
査読済み妥当性
完全実装手順の公開
外部参考文献による本理論の証明
デモスクリプトによる専門監査の代替
---
適合性ベースの読み方
本リポジトリでは、評価軸を「真偽」ではなく「適合性」に置く。
```text
PASS
  定義・境界・主張が、指定された射程内で内部整合している。

SUSPEND
  未定義・未観測・未閉包・危険領域接近により、断定を止めるべき状態。

FAIL
  共通誓約に違反している、用語を混線している、未閉包の主張を断定している状態。
```
未閉包の問いに対して、無理に答えを出してはならない。  
正しい出力は SUSPEND である。
---
参考資料方針
`REFERENCES.md` と `ENGINEERING_POSTURE_REFERENCES.md` は参考資料である。
それらは本フレームワークの証明ではない。  
引用元機関による支持を意味しない。  
日本語原典を上書きしない。  
共通誓約を上書きしない。
目的は以下に限定される。
仕様書的言語の一般用法
工学的態度
V&V・監査の一般座標
リスク管理・安全工学の語彙
公開リポジトリ・引用・ライセンス運用
AIリスク・説明可能性の隣接語彙
Umami Gapなどの背景比喩
---
引用
DOI登録前の暫定引用例：
```text
Gacchimuchi. closure-phase-specs: Public bilingual specification archive for TCP, Closure Phase Ψ, DDP, and related application examples. GitHub repository, version v0.7-bilingual.
```
Zenodo等でDOIを発行した後は、GitHub URL単体ではなくDOI付きの版を引用する。
---
ライセンス
特記がない限り、本リポジトリの文書は以下で公開する。
```text
Creative Commons Attribution 4.0 International
SPDX-License-Identifier: CC-BY-4.0
```
コードを含む場合、コード部分は原則として以下を推奨する。
```text
Apache License 2.0
SPDX-License-Identifier: Apache-2.0
```
倫理的利用方針は、著者の境界宣言であり、ライセンス本文の代替ではない。
---
責任境界
LLMは文章生成、翻訳、整形、コード生成、構造レビューを支援し得る。  
ただし、公開・採否・修正・版管理・最終責任は著者に属する。
誤りが見つかった場合は、Issue、Pull Request、Errata、Releaseによって記録・修正する。
