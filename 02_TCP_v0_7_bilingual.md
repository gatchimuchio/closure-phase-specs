# Trinity Principle (TCP: Three-Term Closure Principle)
## Minimum Closure Principle for World Description and Closure Function M

**One-line definition**

The Trinity Principle (TCP) is a methodology of premise fixation and stopping rules for closing a world description as **X / R / M** and treating **SUSPEND** as a valid output for unclosed, unobserved, or danger-boundary-adjacent cases.

**Author**: Gacchimuchi♂  
**Writing assistance**: LLM (Large Language Model)  
**Version**: v0.7-bilingual  
**Date**: 2026-04-24

**Language note**: This English text is a public-facing projection. The Japanese original appears in Part II and remains the authoritative source.

---

## Part I. English

## Common Pledge / Use Boundary

This document explicitly prohibits the following:

1. **Direct superiority scoring**: connection to ranking, scoring, grading, selection, personality assessment, or allocation decisions.
2. **Designs that may connect to irreversible domination, manipulation, or governance**: connection to weakness extraction, manipulation, agitation, or domination procedures.
3. **Authority capture**: use of this document as an “authority shield” to silence other people or other models.

What this document permits for public disclosure is operational definitions, observation procedures, stopping rules, logging specifications, and misuse-prevention boundaries. This document does not prove truth. It addresses **conformance, reproducibility, and operability**.

---

## Status of this Memo

This document is a **methodological specification** for avoiding unclosure and cross-talk in world description. It defines the minimum closure form for world description and the procedure for stopping when no conclusion can be validly produced.

The evaluation axis is not truth/falsity, but:

- conformance to specification
- reproducibility of unclosure detection
- implementability of stopping rules (stoppability / operability)
- reduction of descriptive cross-talk

**Category**: Principle / Protocol Specification  
**Scope**: Logic / World Description / Closure  
**Dependencies**: None  
**Conformance**: See Section 8

---

## Starting from Common Usage

The words and terms used in this document refer, at the starting point, to their socially common meanings. This is because the problem addressed here originates in the discomfort, cross-talk, and unclosed assumptions extracted from the ordinary use of such terms.

However, the purpose of this document is not to repeat or endorse common usage. It separates cross-talk, insufficient definition, and implicit judgment conditions contained in common usage, and reconstructs them into **operational definitions** that can handle observation, stopping, and conformance.

Common usage is therefore the entrance. The definitions in this document are the body.

---

## Normative Language

The following words indicate requirement levels in this specification:

- **MUST**: required. Violation constitutes non-conformance.
- **MUST NOT**: prohibited. Violation constitutes non-conformance.
- **SHOULD**: recommended. Deviation requires stated rationale.
- **MAY**: optional. Left to the implementer or reader.

This document is not an IETF RFC. It adopts an RFC-like structure only for readability as a specification document.

---

## Non-goals

This document does not aim to:

- determine the truth, reality, or metaphysical validity of the world
- provide value judgments such as good/evil or superiority/inferiority
- fully explain the world
- persuade or enlighten humans
- exhaustively define the general meaning of “meta”
- disclose detailed implementations of Closure Phase Ψ, DDP, or HDS

This document only fixes **what must be fixed for a discussion or description to close**.

---

## Abstract

The Trinity Principle (TCP) defines “why three” not as numerology or symbolism, but as the **minimum closure form of description**. This document adopts neither true objectivity nor true subjectivity, and it does not hide the rules that necessarily intervene in observation and description.

As a result, it adopts the following three terms as the minimum form for closing a world description:

```text
W := (X, R, M)
```

X is the target, R is the relation, and M is the Closure Function. M is not merely an additional rule layer. M is the **coordinate of the observer role** that fixes what is treated as identical, where the boundary is drawn, what counts as judgment, and where assertion stops.

This document rereads many contradictions and paradoxes not as “failures of the world,” but as unclosed description, layer cross-talk, or insufficient premise fixation. It also positions **SUSPEND**, rather than forced conclusion generation, as a valid output for unclosed, unobserved, or danger-boundary-adjacent cases.

---

## 1. Problem Statement: Why Do World Descriptions Break?

World descriptions often break for the following reasons:

1. The target is ambiguous.
2. Relations can be read in multiple ways.
3. Judgment conditions are implicit.
4. The observer role is hidden.
5. Assertions are forced even when no conclusion can validly be produced.

What is happening is not necessarily an error in the object itself. In many cases, the failure is **unclosure of the descriptive form**.

This document treats the problem not as a debate about the contents of the world, but as the problem of **how the world must be written in order to close**.

---

## 2. Basic Position

### 2.1 True objectivity is not adopted

This document does not adopt a viewpoint from which the observer is completely removed, because every description involves target selection, comparison method, and judgment conditions.

### 2.2 True subjectivity is not adopted

This document also does not adopt subjectivity as a pure internal substance. It adopts only what is observed, described, and preserved as logs.

### 2.3 What remains is the observation frame and rules

Therefore, this document separates world description into:

- what is targeted
- how targets are related
- what counts as identity, boundary, judgment, and stopping

### 2.4 M is the Closure Function

M is not “an additional rule layer placed on top of R.” M is the function itself by which a world description is closed.

M handles at least:

- **Identity**: what is treated as the same
- **Boundary**: what is included in the target
- **Judgment**: what counts as fixed or established
- **Stopping**: where assertion must stop

If necessary, M may be described as close to the ordinary word “meta.” However, to avoid the ambiguity of common usage, this document calls it **Closure Function M**.

---

## 3. Definitions

### 3.1 World Model W

This document defines the world model W as:

```text
W := (X, R, M)
```

### 3.2 X: Target

X is the target specification that defines what is handled. It may include at least:

- target set
- identifier
- version
- settings
- observation range
- log range
- operational state

### 3.3 R: Relation

R is the relation specification that defines how the target relates or is observed. It may include at least:

- input-output correspondence
- comparison procedure
- transition rules
- constraints
- falsification procedure
- perturbation conditions

### 3.4 M: Closure Function

M is the function that defines how R is read and where the description closes. This document treats M as the coordinate that fixes the observer role.

It may include at least:

- identity rules
- boundary conditions
- judgment conditions
- falsification conditions
- logging rules
- application of pledges
- stopping rules

### 3.5 Closure

Closure is the state in which the evaluation of a claim can be determined only from inside W, namely X, R, M, and logs.

### 3.6 Unclosure

Unclosure is the state in which any of X, R, or M is missing and conclusions may diverge. A state in which assertion proceeds without a fixed observer role is also treated as unclosed.

---

## 4. Why Three Terms Are Necessary

### 4.1 One term does not close

With only target X, it is not determined what to compare it with, how to read it, or what counts as established. Therefore one term does not close.

### 4.2 Two terms still do not close

Even if X and R are given, the following remain:

- what is treated as identical
- what is included in the target
- what counts as established
- where assertion stops

These belong to M. Therefore, with two terms, the reading of the conclusion still branches.

### 4.3 Three terms are the minimum closure

When X, R, and M are all present, the target, relation, and judgment rule are explicit, and the description can finally close. Therefore, three terms are the minimum unit of closure.

### 4.4 Four or more terms are derivative

Designs with four or more terms can be described as divisions, extensions, or multiplexing of the three terms. The qualitative jump occurs at three terms.

### 4.5 Contradiction is not a property of the world, but a judgment term after fixation

The mere coexistence of A and B is not immediately called contradiction. It may simply be that matters remain side by side without fixation.

Contradiction is a judgment term applied to a description after M has intervened and the description has been fixed.

Therefore, in many cases the problem lies in:

- ambiguity about which description has been fixed
- unfixed observer role
- layer cross-talk
- implicit M

---

## 5. SUSPEND: Stopping Is Not Failure

### 5.1 Definition of SUSPEND

SUSPEND is a valid output state in which assertion is withheld for unclosed, unobserved, or danger-boundary-adjacent cases.

### 5.2 Why stopping is necessary

If a description is asserted while unclosed, the reader’s convenience enters the result instead of the contents of the world. The only way to prevent this is to stop.

### 5.3 Stopping is not a cognitive defect

This document does not treat stopping as weakness or lack of knowledge. Rather, a description that cannot stop where it should is dangerous.

### 5.4 Meaning of SUSPEND in TCP

SUSPEND is a procedure for making visible that a world description is incomplete. Therefore SUSPEND is not evasion, but a core function for preserving closure conditions.

### 5.5 Typical reasons for SUSPEND

SUSPEND may fire when, for example:

- X is unspecified
- R is unspecified
- M is unspecified
- logs are insufficient
- the observation range is exceeded
- a danger boundary or prohibited domain is being approached
- the description begins to connect to superiority assessment or irreversible domination

---

## 6. Relationship Between TCP and Other Documents

### 6.1 TCP is methodology

TCP defines how a world description should close. It therefore provides not the content itself, but a **methodology of description**.

### 6.2 Relationship to Closure Phase Ψ

Closure Phase Ψ handles the phase that appears externally as a result of Closure Function M operating internally. TCP handles how that phase is described in closed form.

- **TCP**: methodology of closure description
- **Closure Phase Ψ**: output phase of Closure Function M

### 6.3 Relationship to DDP

DDP handles the operating mode of the world and its danger boundaries. TCP handles how that operating world is described and where it stops.

- **TCP**: how to write so that it closes
- **DDP**: on what coordinates it runs and what counts as a danger boundary

### 6.4 Relationship to HDS

HDS is a lower operational layer under DDP and a practical framework for real-world decision-making. TCP functions as the methodology for closing targets, relations, judgments, and stopping conditions handled by HDS.

### 6.5 Relationship to paradoxes

Many paradoxes are not proof that “the world is broken.” Rather, they function as bug detectors indicating:

- insufficient fixation of description
- layer cross-talk
- implicit M
- assertion where stopping was required

---

## 7. Minimum Protocol

When describing the world in conformance with TCP, at least the following SHOULD be fixed:

```text
1. X: what is being targeted
2. R: how the targets are related and observed
3. M: what counts as identity, boundary, judgment, and stopping condition
4. Log: what is recorded and how it can be inspected later
5. Suspend: under what conditions assertion stops
```

An assertion that does not fix these five points is treated as unclosed under TCP.

---

## 8. Conformance Conditions

A world description conforming to this document MUST at least:

1. specify X, R, and M
2. not settle for two terms or make M implicit
3. allow SUSPEND when unclosed
4. include identity, boundary, judgment, and stopping
5. not shortcut to superiority assessment
6. not fill log insufficiency with assertion

The following are non-conformant:

- asserting from X alone
- fixing a conclusion from X/R alone
- pushing M into implicit common sense
- failing to stop when stopping is required
- turning a descriptive methodology into a weapon for superiority assessment
- crossing danger boundaries without procedure

---

## 9. Scope and Limits

### 9.1 Scope

This document handles how world descriptions can close and how they can become stoppable.

### 9.2 Out of scope

The following are outside the scope of this document:

- the real existence of the world itself
- final proof of objectivity itself
- the formation mechanism of subjectivity
- internal structure of emotion
- ontology of consciousness
- HDS core implementation

### 9.3 Limits

This document does not guarantee the contents of the world. It only provides how to detect unclosure in writing and how to stop in order to avoid false assertion.

---

## 10. Conclusion

This document redefines the Trinity Principle (TCP) as the minimum closure principle for world description.

The core consists of four points:

1. The minimum closure form of world description is `W := (X, R, M)`.
2. M is not an additional rule layer, but a Closure Function that handles identity, boundary, judgment, and stopping.
3. Contradiction is not a property of the world itself, but a judgment term applied to a fixed description.
4. SUSPEND is a valid output for unclosed, unobserved, or danger-boundary-adjacent cases.

Therefore, TCP is not a universal theory that directly gives the answer to the world. TCP is a methodology of premise fixation and stopping rules: it shows what must be fixed for a discussion to close and where to stop if it cannot be fixed.

---

## Revision Notes

- v0.7-bilingual: Added English-first structure and preserved the Japanese original as Part II.
- v0.6-public: reorganized as a methodology specification for GitHub publication.
- Unified M not as “meta-rule” but as “Closure Function.”
- Re-fixed dependencies among DDP / Ψ / HDS.
- Added typical conditions corresponding to SUSPEND reason codes.

---

## Part II. Japanese Original

# トリニティ原理（TCP: Three-Term Closure Principle）
## 世界記述の最小閉包原理と閉包機能M

**One-line definition**

トリニティ原理（TCP）とは、世界記述を **X / R / M** で閉じ、未閉包・未観測・危険領域接近に対して **SUSPEND** を正当な出力として扱うための、前提固定と停止規則の方法論である。

**著者**：がっちむち♂  
**文章生成支援**：LLM（大規模言語モデル）  
**版**：v0.6-public  
**日付**：2026-04-24

---

## 共通誓約（Use Boundary）

本稿は、以下を明示的に禁ずる。

1. **優劣スコアリング直結**：序列化・採点・格付け・選別・人格査定・配分決定への接続
2. **不可逆な支配・誘導・統治へ接続し得る設計**：対象の弱点抽出、操作、扇動、支配手順への接続
3. **権威化利用**：本稿を「権威の盾」として用い、他者または他モデルを黙らせる行為

本稿が公開可能とするのは、操作的定義、観測手続き、停止規則、ログ仕様、誤用防止境界である。
本稿は真理証明ではなく、**適合性・再現可能性・運用可能性**を扱う。


## Status of this Memo

本稿は、世界記述における未閉包と混線を避けるための**方法論仕様**である。
本稿が定義するのは、世界記述の最小閉包形式、および結論不能時に停止するための手続きである。

評価軸は真偽ではなく、以下である。

- 仕様への適合性（Conformance）
- 未閉包検出の再現可能性（Reproducibility）
- 停止規則の実装可能性（Stoppability / Operability）
- 記述混線の減少（Error Reduction）

**Category**: Principle / Protocol Specification  
**Scope**: Logic / World Description / Closure  
**Dependencies**: None  
**Conformance**: See Section 8

---

## 一般用法からの出発について

本稿で用いる語句・語彙は、出発点として社会通念上の一般的解釈を参照する。
これは、本稿の問題意識が、社会通念上流通している語の一般用法から生じる違和感・混線・未閉包の抽出に由来するためである。

ただし本稿の目的は、一般用法を反復・追認することではない。
本稿は、一般用法に含まれる混線、定義不足、判定条件の暗黙化を切り分け、観測・停止・適合性を扱える**操作的定義**へ再構成する。

したがって、一般用法は入口であり、本文定義が本体である。


## 規格語（Normative Language）

本稿では、以下の語を仕様上の要請レベルとして用いる。

- **MUST**：必須。違反は適合性違反となる。
- **MUST NOT**：禁止。違反は非適合となる。
- **SHOULD**：推奨。逸脱には理由の明示が必要である。
- **MAY**：任意。実装者または読者の判断に委ねる。

本稿は IETF RFC ではない。ただし、仕様文書としての読みやすさのため RFC 風の構成を採用する。


## 非目標（Non-goals）

本稿は、以下を目的としない。

- 世界の真理性・実在性・形而上学的妥当性の決定
- 価値判断（善悪・優劣）の提供
- 完全な世界説明
- 人間向けの説得・啓蒙
- 「メタとは何か」という一般語義の網羅
- 閉包位相Ψ、神域原理DDP、HDSの詳細実装

本稿は、**何を固定しないと議論が閉じないか**を固定することのみを目的とする。

---

## Abstract

トリニティ原理（TCP）は、「なぜ三か」を数秘や象徴ではなく、**記述の最小閉包形式**として定義する。
本稿は、真の客観性も真の主観性も採用せず、観測と記述に必ず介在する規則を隠蔽しない。

その結果、世界記述を閉じる最小形式として、三項を採用する。

```text
W := (X, R, M)
```

Xは対象、Rは関係、Mは閉包機能である。
Mは単なる追加ルール層ではない。
Mは、何を同一とし、どこまでを境界とし、何をもって判定し、どこで停止するかを固定する**観測者ロールの座標**である。

本稿では、矛盾やパラドックスの多くを「世界の破綻」ではなく、記述の未閉包、階層混線、前提固定不足として読み直す。
また、未閉包・未観測・危険領域接近に対して、結論生成ではなく **SUSPEND** を正当な出力として位置づける。

---

## 1. 問題設定：なぜ世界記述は壊れるのか

世界記述は、しばしば次の理由で壊れる。

1. 対象が曖昧である。
2. 関係の読み方が複数ある。
3. 判定条件が暗黙である。
4. 観測者ロールが隠れている。
5. 結論不能時にも無理に断定する。

このとき起きているのは、対象そのものの誤りとは限らない。
多くの場合、起きているのは**記述形式の未閉包**である。

本稿は、この問題を、世界の中身の議論ではなく、**世界をどう書けば閉じるか**の問題として扱う。

---

## 2. 本稿の基本立場

### 2.1 真の客観性は採用しない

本稿は、観測者を完全に除いた視点を採用しない。
どの記述にも、対象選択、比較方法、判定条件が介在するからである。

### 2.2 真の主観性も採用しない

本稿は、純粋な内面実体としての主観も採用しない。
採用するのは、観測され、記述され、ログとして残されたものだけである。

### 2.3 残るものは観測枠と規則である

したがって、本稿では世界記述を以下に分ける。

- 何を対象とするか。
- どう関係づけるか。
- 何をもって同一・境界・判定・停止とするか。

### 2.4 Mは閉包機能である

Mは「Rの上にさらに足される追加規則層」ではない。
Mとは、世界記述を閉包させるための機能そのものである。

Mは少なくとも以下を扱う。

- **同一性**：何を同じとみなすか。
- **境界**：どこまでを対象に含めるか。
- **判定**：何をもって確定・成立とするか。
- **停止**：どこで断定を止めるか。

必要なら既存語で「メタ」に近いと言ってよい。
ただし本稿では一般語義の曖昧さを避け、**閉包機能M**と呼ぶ。

---

## 3. 定義

### 3.1 世界モデルW

本稿では、世界モデルWを次の三項で定義する。

```text
W := (X, R, M)
```

### 3.2 X：対象

Xとは、何を扱うかを定める対象指定である。
少なくとも以下を含みうる。

- 対象集合
- 識別子
- 版
- 設定
- 観測範囲
- ログ範囲
- 運用状態

### 3.3 R：関係

Rとは、対象がどう関係するか、どう観測されるかを定める関係指定である。
少なくとも以下を含みうる。

- 入力から出力への対応
- 比較手続き
- 遷移規則
- 制約条件
- 反証手続き
- 摂動条件

### 3.4 M：閉包機能

Mとは、Rをどう読み、どこで閉じるかを定める機能である。
本稿ではMを、観測者ロールを固定する座標として扱う。

少なくとも以下を含みうる。

- 同一性規則
- 境界条件
- 判定条件
- 反証条件
- ログ規約
- 誓約の適用
- 停止規則

### 3.5 閉包

閉包とは、主張の評価がWの内部、すなわちX・R・Mおよびログだけで決定できる状態をいう。

### 3.6 未閉包

未閉包とは、X・R・Mのいずれかが欠落し、結論が分岐しうる状態をいう。
また、観測者ロールが固定されないまま断定が走っている状態も未閉包として扱う。

---

## 4. なぜ三項が必要か

### 4.1 一項では閉じない

対象Xだけでは、何と比べるか、どう読むか、何をもって成立とするかが決まらない。
よって一項では閉じない。

### 4.2 二項でも閉じない

XとRが与えられても、なお次が残る。

- 何を同じとみなすか。
- どこまでを対象に含めるか。
- 何をもって成立とするか。
- どこで停止するか。

これらはMに属する。
したがって二項では、結論の読み方が分岐する。

### 4.3 三項が最小閉包である

X・R・Mがそろったとき、対象・関係・判定規則が明示され、ようやく記述が閉じる。
よって三項は、最小の閉包単位である。

### 4.4 四項以上は派生である

四項以上の設計は、三項の分割、拡張、多重化として記述できる。
質的飛躍は三項で起きる。

### 4.5 矛盾は世界の属性ではなく、確定後の判定語である

AとBが併存しうること自体を、直ちに矛盾とは呼ばない。
それは、事柄が未確定のまま並んでいるだけかもしれない。

矛盾とは、Mが介入して記述が確定した後に、その記述に対して下される判定語である。

したがって多くの場合、問題は次にある。

- どの記述で確定したのかが曖昧。
- 観測者ロールが未固定。
- 階層が混線している。
- Mが暗黙化している。

---

## 5. SUSPEND：停止は失敗ではない

### 5.1 SUSPENDの定義

SUSPENDとは、未閉包・未観測・危険領域接近に対して、断定を生成せず保留する正当な出力状態である。

### 5.2 なぜ停止が必要か

記述が閉じていないのに断定すると、世界の中身ではなく読み手の都合が混入する。
これを防ぐには、止まるしかない。

### 5.3 停止は認識の欠陥ではない

本稿では、停止を弱さや知識不足とは扱わない。
むしろ、止まるべき場面で止まれない記述こそ危険である。

### 5.4 TCPにおけるSUSPENDの意味

SUSPENDは、世界記述が未完であることを可視化するための手続きである。
よってSUSPENDは逃避ではなく、閉包条件を守るための中核機能である。

### 5.5 SUSPENDの典型理由

SUSPENDは、たとえば以下で発火する。

- Xが未指定である。
- Rが未指定である。
- Mが未指定である。
- ログが不足している。
- 観測範囲を超えている。
- 危険境界または禁止領域へ接近している。
- 優劣査定や不可逆支配へ接続し始めている。

---

## 6. TCPと他文書の関係

### 6.1 TCPは方法論である

TCPは、世界記述をどう閉じればよいかを定める。
したがってTCPは、内容そのものではなく**記述の方法論**を与える。

### 6.2 閉包位相Ψとの関係

閉包位相Ψが扱うのは、閉包機能Mが自己内部で駆動した結果として外部へ現れる位相である。
TCPが扱うのは、その位相をどう閉包記述するかである。

- **TCP**：閉包記述の方法論
- **閉包位相Ψ**：閉包機能Mの出力相

### 6.3 神域原理DDPとの関係

神域原理DDPが扱うのは、世界の駆動様式と危険境界である。
TCPが扱うのは、その駆動世界をどう記述し、どこで停止するかという方法論である。

- **TCP**：どう書けば閉じるか
- **DDP**：どの座標で走らせ、何を危険境界とするか

### 6.4 HDSとの関係

HDSは、DDPの下位運用レイヤーであり、現実の意思決定へ落とす実務フレームである。
TCPは、HDSが扱う対象・関係・判定・停止を閉包するための記述方法論として機能する。

### 6.5 パラドックスとの関係

パラドックスの多くは、「世界が壊れている」ことの証明ではない。
むしろ、以下を知らせる記述バグ検出器として機能する。

- 記述の固定が足りない。
- 階層が混線している。
- Mが暗黙化している。
- 停止すべき場面で断定している。

---

## 7. 最小プロトコル

TCP準拠で世界記述を行う場合、少なくとも以下を固定する SHOULD。

```text
1. X: 何を対象にしているか
2. R: それらをどう関係づけ、どう観測するか
3. M: 何を同一・境界・判定・停止条件にするか
4. Log: 何を記録し、後からどう検査できるようにするか
5. Suspend: どの条件で断定を止めるか
```

この五点を固定しない断定は、TCP上は未閉包として扱う。

---

## 8. 適合性条件（Conformance）

本稿に適合する世界記述は、少なくとも以下を満たす MUST。

1. X・R・Mを明示する。
2. 二項で済ませず、Mを暗黙化しない。
3. 未閉包時にはSUSPENDを許容する。
4. 同一性・境界・判定・停止を含む。
5. 優劣査定へ短絡しない。
6. ログ不足を断定で補完しない。

以下はいずれも非適合である。

- Xだけで断定する。
- X/Rのみで結論を固定する。
- Mを暗黙の常識へ押し込む。
- 止まるべき場面で止まらない。
- 記述方法論を優劣査定の武器に変える。
- 危険境界への接近を、手続きなしに突破する。

---

## 9. 射程と限界

### 9.1 射程

本稿が扱うのは、世界記述がどうすれば閉包し、どうすれば停止可能になるかである。

### 9.2 射程外

以下は本稿の射程外である。

- 世界の本当の実在性
- 客観そのものの最終証明
- 主観の成立機序
- 感情の内部構造
- 意識の存在論
- HDS核実装

### 9.3 限界

本稿は、世界の中身を保証しない。
保証するのは、どう書けば未閉包を見抜けるか、どう止まれば誤断定を避けられるかである。

---

## 10. 結論

本稿は、トリニティ原理（TCP）を、世界記述の最小閉包原理として再定義した。

中核は次の四点である。

1. 世界記述の最小閉包形式は `W := (X, R, M)` である。
2. Mは追加的な規則層ではなく、同一性・境界・判定・停止を扱う閉包機能である。
3. 矛盾は世界そのものの属性ではなく、確定後の記述に対する判定語である。
4. 未閉包・未観測・危険領域接近に対して、SUSPENDは正当な出力である。

したがってTCPは、世界の答えを直接与える万能理論ではない。
TCPは、何を固定しないと議論が閉じないか、固定できないならどこで止まるべきかを示す、前提固定と停止規則の方法論である。

---

## Revision Notes

- v0.6-public: GitHub公開用に方法論仕様として再整理。
- Mを「メタ規則」ではなく「閉包機能」として統一。
- DDP/Ψ/HDSとの依存関係を再固定。
- SUSPENDの理由コードに相当する典型条件を追加。
