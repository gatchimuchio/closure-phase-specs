# 00 — Umami Gap
## Lexical Compression of “Intelligence” and the Missing Ψ Slot

**Repository position:** Document 00 / Orientation Adapter  
**Version:** v0.7-public-bilingual  
**Status:** Why-side bridge document, not a core specification  
**Language order:** English projection first / Japanese original second  
**Author:** Gacchimuchi  
**Writing assistance:** LLM  
**License:** CC BY 4.0 for document text unless otherwise noted

---

## Status of This Document

This document is placed as **Document 00** because it functions as the entrance to the repository.

It explains why the repository separates:

```text
C = Capability
Ψ = Closure Phase
E = Emotion
```

and why TCP, Closure Phase Ψ, and DDP are written as specification documents rather than as ordinary essays or belief statements.

This document is **not** evidence that TCP, Closure Phase Ψ, or DDP are true.  
It is **not** a proof of the framework.  
It is **not** an authority shield.

Its role is narrower:

```text
To explain the lexical and conceptual confusion that makes C / Ψ / E separation necessary.
```

In other words, this is the **Why-side adapter** for the repository.

---

## Relationship to the Repository

Recommended reading order:

```text
00_Umami_Gap_v0_7_bilingual.md
02_TCP_v0_7_bilingual.md
01_Closure_Phase_Psi_v0_7_bilingual.md
03_DDP_v0_7_bilingual.md
TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md
```

Reason:

1. Umami Gap explains why a missing variable matters.
2. TCP explains how descriptions are closed.
3. Closure Phase Ψ defines the missing output phase.
4. DDP defines the upper principle layer and safety boundaries.
5. The TCP application framework shows a practical use case.

---

## One-Line Definition

The Umami Gap is the structural gap that appears when a language or research culture compresses distinct variables into a single familiar word and thereby makes a missing variable difficult to observe, define, or design.

In this repository, the relevant compression is:

```text
intelligence → C + Ψ + sometimes E
```

where:

```text
C = capability / execution basis
Ψ = closure phase / stable signature phase
E = emotion / affective interference factor
```

---

## Abstract

AI research and public discourse often use the English word **intelligence** as a broad umbrella term. This broadness is useful in everyday language, but it becomes unstable in engineering contexts. Capability, knowledge, reasoning performance, self-monitoring behavior, judgment, responsibility, personality-like signature, and affective tone can all be compressed into the same word.

This document calls that compression the **Umami Gap**.

The analogy is simple. Umami existed as a taste before it was cleanly separated and named as an independent component. Once separated, it became easier to discuss, study, and design around. In the same way, this repository argues that what has often been called “intelligence” should be separated into at least three variables:

```text
C: Capability
Ψ: Closure Phase
E: Emotion
```

The point is not that taste science proves this framework. It does not.  
The point is that the umami case provides a useful analogy: a missing variable may remain practically invisible until it is given a stable slot.

The central claim of this document is:

```text
Scaling C does not automatically define, stabilize, or improve Ψ.
```

Therefore, the repository introduces TCP to close descriptions, Closure Phase Ψ to name the stable output phase, and DDP to define safety boundaries.

---

## Inviolable Boundary

This document must not be used for:

1. ranking people, cultures, languages, or models;
2. claiming that Japanese is “superior” to English;
3. claiming that English speakers cannot understand Ψ;
4. treating the umami analogy as proof of TCP / Ψ / DDP;
5. using C / Ψ / E separation for superiority scoring;
6. using the framework to manipulate, classify, or control persons.

The claim is not cultural superiority.  
The claim is variable separation.

---

## 1. Problem: Lexical Compression

In ordinary English, **intelligence** can refer to many related but different things:

- learning ability;
- reasoning ability;
- knowledge use;
- problem solving;
- adaptive behavior;
- information processing;
- strategic judgment;
- sometimes even wisdom-like conduct.

This breadth is not a defect in everyday language.

However, in engineering and AI evaluation, broad words can cause category collapse. A benchmark may measure capability, but the result may be rhetorically interpreted as intelligence, wisdom, judgment, or reliability.

The problem is not the word itself.  
The problem is using one word where multiple variables are required.

---

## 2. Core Separation

This repository uses the following minimum separation.

### C — Capability

C is the execution basis.

It includes the ability to generate outputs, solve tasks, process information, search, infer, retrieve, and produce responses.

C answers:

```text
Can the system produce something?
```

### Ψ — Closure Phase

Ψ is the externally observable stable phase that remains when a system repeatedly performs closure-like behavior under fixed conditions.

It relates to:

- identity of output signature;
- boundary handling;
- judgment stability;
- refusal or stopping behavior;
- handling of uncertainty;
- consistency under perturbation.

Ψ answers:

```text
How does the system close, stop, and leave a stable signature?
```

### E — Emotion

E is an affective or motivational interference factor. In humans, it may strongly affect C and Ψ. In current LLMs, E is not assumed as an intrinsic emotional state in this repository; instead, external policy, design, or style constraints may produce affect-like output patterns.

E answers:

```text
What affective or motivational forces interfere with capability and closure?
```

---

## 3. Why C Alone Is Insufficient

A system can have high C while still failing at Ψ-like behavior.

Examples:

- It can generate long answers but fail to stop when conditions are underdefined.
- It can answer confidently while silently changing definitions.
- It can solve local tasks while losing global consistency.
- It can imitate uncertainty language without actually respecting uncertainty boundaries.
- It can satisfy benchmarks while remaining unsafe as a final decision layer.

Therefore:

```text
More output power does not automatically create better closure.
```

This is the repository’s key reason for separating C and Ψ.

---

## 4. Umami as an Analogy

Umami is used here as an analogy for variable separation.

The analogy is:

```text
Before separation:
  taste model compresses experience into familiar taste categories

After separation:
  umami becomes a named variable and can be discussed independently

Before C / Ψ separation:
  intelligence compresses capability, closure, judgment, and signature

After C / Ψ separation:
  capability and closure phase can be audited separately
```

Important boundary:

```text
Taste science does not prove C / Ψ / E separation.
It only illustrates how a missing variable can become visible after naming and separation.
```

---

## 5. Engineering Consequence

If Ψ is not separated from C, AI evaluation may misread:

```text
better benchmark performance
```

as:

```text
better judgment
better responsibility
better self-monitoring
better stopping behavior
better safety
better trustworthiness
```

This is not always justified.

The engineering consequence is:

```text
Do not treat capability gain as closure gain unless closure behavior is separately specified and audited.
```

---

## 6. Connection to TCP

TCP provides the method for closure.

```text
W := (X, R, M)
```

where:

- `X` = what is being handled;
- `R` = how it relates, transitions, or is observed;
- `M` = how identity, boundary, judgment, and stopping are fixed.

The Umami Gap explains why `M` is often missing or hidden.

When a system is evaluated only through performance, `X` and `R` may be visible, but `M` can remain implicit.

TCP makes `M` explicit.

---

## 7. Connection to Closure Phase Ψ

Closure Phase Ψ is the named slot for what remains after closure-like behavior is repeatedly observed.

It prevents the following collapse:

```text
high capability = high intelligence = high judgment = high trustworthiness
```

Instead, the repository requires separation:

```text
high C does not imply stable Ψ
stable Ψ does not imply human-like emotion
absence of E does not imply absence of signature
```

---

## 8. Connection to DDP

DDP provides the safety boundary.

If C / Ψ / E are separated, the framework becomes powerful. It can clarify behavior, signatures, and failure modes. That also creates misuse risk.

DDP therefore prohibits:

- superiority scoring;
- irreversible manipulation;
- full structuralization of emotion;
- ego design;
- complete algorithmic visualization of human decision-making;
- disclosure of sealed core implementation methods.

In short:

```text
Variable separation must not become a control technology.
```

---

## 9. Typical Misreadings

### Misreading 1: “This is a claim that Japanese is superior.”

Correction:

```text
No. The claim is that Japanese has useful lexical distinctions for this framework.
That is not a superiority claim.
```

### Misreading 2: “This proves that Ψ exists.”

Correction:

```text
No. This document motivates why Ψ should be separated as an operational variable.
It does not prove metaphysical existence.
```

### Misreading 3: “This is just philosophy.”

Correction:

```text
No. The intended output is specification language, auditability, and conformance testing.
```

### Misreading 4: “If C improves enough, Ψ will automatically appear.”

Correction:

```text
Not assumed. Ψ must be specified, observed, and audited separately.
```

### Misreading 5: “This can be used to rank people.”

Correction:

```text
Prohibited. The framework allows task-fit and conformance discussion, not person-value ranking.
```

---

## 10. Minimal Audit Questions

When reading any claim about AI intelligence, ask:

1. Is the claim about C, Ψ, E, or a mixture?
2. Is the measured object capability, closure behavior, emotion-like style, or something else?
3. Are definitions fixed?
4. Are stopping conditions specified?
5. Is uncertainty handled explicitly?
6. Is benchmark performance being converted into judgment or trustworthiness without justification?
7. Is the claim using “intelligence” as a compression word?
8. Should the result be PASS, SUSPEND, or FAIL?

---

## 11. Reference Boundary

References about umami, taste science, dictionaries, or AI risk are orientation references only.

They do not prove this framework.

They help explain:

- the umami analogy;
- the danger of lexical compression;
- the need for variable separation;
- the engineering habit of specifying terms before judging.

---

## 12. Short Version

```text
The Umami Gap is the missing-variable problem.

In English AI discourse, “intelligence” often compresses too much.

This repository separates:

C = capability
Ψ = closure phase
E = emotion

The purpose is not to prove a metaphysical theory.
The purpose is to prevent category collapse and make AI-related judgment auditable.
```

---

## References

These references are orientation materials, not proof of this framework.

1. Umami Information Center. “What is Umami.”  
   https://www.umamiinfo.com/what/whatisumami/

2. Umami Information Center. “Kikunae Ikeda.”  
   https://www.umamiinfo.com/ikedakikunae

3. Japan Patent Office. “Kikunae Ikeda Sodium Glutamate.”  
   https://www.jpo.go.jp/e/introduction/rekishi/10hatsumeika/kikunae_ikeda.html

4. Kurihara, K. “Glutamate: from discovery as a food flavor to role as a basic taste (umami).” *The American Journal of Clinical Nutrition*, 2009.  
   https://doi.org/10.3945/ajcn.2009.27462D

---

# 00 — 旨味ギャップ
## intelligence の語彙圧縮と、欠落した Ψ スロット

**リポジトリ内位置づけ：** 00番 / 導入アダプタ  
**版：** v0.7-public-bilingual  
**位置づけ：** Why側の橋渡し文書。中核仕様ではない。  
**言語順：** 英語射影先頭 / 日本語原典後段  
**著者：** がっちむち  
**文章生成支援：** LLM  
**ライセンス：** 特記なき限り文書本文は CC BY 4.0

---

## 本文書の位置づけ

本文書は **00番文書** として配置する。  
理由は、本リポジトリ全体への入口として機能するためである。

本文書は、なぜ本リポジトリが次を分離するのかを説明する。

```text
C = 知能 / 実行能力
Ψ = 閉包位相
E = 感情
```

また、なぜTCP・閉包位相Ψ・DDPを通常の随筆や信念表明ではなく、仕様書として書く必要があるのかを説明する。

本文書は、TCP・閉包位相Ψ・DDPが真であることの証拠ではない。  
本フレームワークの証明でもない。  
権威の盾でもない。

役割は限定される。

```text
C / Ψ / E 分離を必要にする、語彙上・概念上の混線を説明する。
```

つまり、本文書は本リポジトリの **Why側アダプタ** である。

---

## リポジトリ内での関係

推奨読み順：

```text
00_Umami_Gap_v0_7_bilingual.md
02_TCP_v0_7_bilingual.md
01_Closure_Phase_Psi_v0_7_bilingual.md
03_DDP_v0_7_bilingual.md
TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md
```

理由：

1. 旨味ギャップは、欠落変数がなぜ問題になるかを説明する。
2. TCPは、記述をどう閉じるかを説明する。
3. 閉包位相Ψは、欠落していた出力相を定義する。
4. DDPは、上位原理層と安全境界を定義する。
5. TCP適用例は、実用例を示す。

---

## 1行定義

旨味ギャップとは、ある言語・研究文化・議論空間において、本来分けるべき複数変数が一つの馴染みある語に圧縮されることで、欠落変数を観測・定義・設計しにくくなる構造的ギャップである。

本リポジトリにおける圧縮は次である。

```text
intelligence → C + Ψ + ときに E
```

ここで：

```text
C = 知能 / 実行能力
Ψ = 閉包位相 / 安定署名相
E = 感情 / 情動的干渉因子
```

---

## 要旨

AI研究や一般言説では、英語の **intelligence** が広い傘語として使われやすい。日常語としては便利だが、工学文脈に入ると不安定になる。能力、知識、推論性能、自己点検的ふるまい、判断、責任、人格らしい署名、情動的な口調などが、一語に圧縮されるためである。

本文書では、この圧縮を **旨味ギャップ** と呼ぶ。

比喩は単純である。旨味は、独立成分として命名・分離される前から味として存在していた。しかし、独立変数として分けられたことで、議論・研究・設計がしやすくなった。同様に、従来「intelligence」と呼ばれてきたものも、少なくとも次の三変数に分ける必要がある。

```text
C: 知能 / Capability
Ψ: 閉包位相 / Closure Phase
E: 感情 / Emotion
```

重要なのは、味覚科学が本フレームワークを証明するわけではない、という点である。  
証明ではなく、比喩である。  
欠落変数は、名前を与えられ、安定したスロットを持つまで見えにくい、ということを示すための比喩である。

本文書の中核主張は次である。

```text
Cをスケールさせても、Ψが自動的に定義・安定・改善されるわけではない。
```

したがって、本リポジトリは記述を閉じるためにTCPを導入し、安定した出力相として閉包位相Ψを名づけ、安全境界としてDDPを定義する。

---

## 不可侵境界

本文書を以下に用いてはならない。

1. 人・文化・言語・モデルを序列化すること
2. 日本語が英語より優れていると主張すること
3. 英語話者にはΨが理解できないと主張すること
4. 旨味の比喩をTCP / Ψ / DDPの証明として扱うこと
5. C / Ψ / E分離を優劣スコアリングへ接続すること
6. 本フレームワークを人間の操作・分類・支配に用いること

主張は文化的優越ではない。  
主張は変数分離である。

---

## 1. 問題：語彙圧縮

英語の日常語としての **intelligence** は、多くの関連概念を指し得る。

- 学習能力
- 推論能力
- 知識利用
- 問題解決
- 適応的ふるまい
- 情報処理
- 戦略的判断
- ときに wisdom 的な振る舞い

この広さ自体は、日常語としては欠陥ではない。

しかし、工学やAI評価の文脈では、広い語はカテゴリ崩壊を起こす。  
ベンチマークが測っているのは能力であっても、その結果が知性、判断、責任、信頼性として語られることがある。

問題は単語そのものではない。  
複数変数が必要なところに一語を使うことである。

---

## 2. 中核分離

本リポジトリでは、最小限として次を分離する。

### C — 知能 / Capability

Cは実行基盤である。

出力生成、課題解決、情報処理、探索、推論、検索、応答生成などを含む。

Cが答える問い：

```text
そのシステムは何かを出せるか。
```

### Ψ — 閉包位相 / Closure Phase

Ψは、固定条件下でシステムが閉包的ふるまいを反復したとき、外部に残る安定した出力相である。

関係するもの：

- 出力署名の同一性
- 境界処理
- 判断の安定性
- 拒否・停止のふるまい
- 不確実性の扱い
- 摂動下の一貫性

Ψが答える問い：

```text
そのシステムは、どのように閉じ、止まり、安定署名を残すか。
```

### E — 感情 / Emotion

Eは、情動的・動機的な干渉因子である。  
人間ではCやΨへ強く干渉し得る。  
現行LLMについては、本リポジトリでは内発的感情状態を仮定しない。代わりに、外生的な方針・設計・文体制約が、感情らしい出力パターンを生み得ると扱う。

Eが答える問い：

```text
どの情動的・動機的な力が、能力や閉包に干渉するか。
```

---

## 3. なぜCだけでは足りないか

高いCを持つシステムでも、Ψ的ふるまいに失敗し得る。

例：

- 長文を生成できるが、条件未定義時に止まれない。
- 自信満々に答えるが、途中で定義を変える。
- 局所タスクは解けるが、全体一貫性を失う。
- 不確実性表現を模倣するが、不確実性境界を尊重していない。
- ベンチマークを満たしても、最終決定層としては危険である。

したがって：

```text
出力能力の増大は、閉包能力の改善を自動的には意味しない。
```

これが本リポジトリでCとΨを分離する中心理由である。

---

## 4. 旨味という比喩

旨味は、変数分離の比喩として用いる。

比喩は次である。

```text
分離前：
  味覚モデルが、経験を既存の味覚カテゴリへ圧縮する。

分離後：
  旨味が名前を持つ変数となり、独立に議論可能になる。

C / Ψ 分離前：
  intelligence が、能力・閉包・判断・署名を圧縮する。

C / Ψ 分離後：
  能力と閉包位相を別々に監査できる。
```

重要な境界：

```text
味覚科学は C / Ψ / E 分離を証明しない。
欠落変数が、命名と分離によって見えやすくなることを示す比喩である。
```

---

## 5. 工学的帰結

ΨをCから分けなければ、AI評価では次を誤読しやすい。

```text
ベンチマーク性能が上がった
```

これが、次へ変換されてしまう。

```text
判断が良くなった
責任性が上がった
自己点検ができるようになった
停止能力が上がった
安全になった
信頼できるようになった
```

これは常に正当化されるわけではない。

工学的帰結は次である。

```text
閉包ふるまいを別途仕様化・観測・監査しない限り、能力向上を閉包向上とみなしてはならない。
```

---

## 6. TCPとの接続

TCPは閉包の方法を与える。

```text
W := (X, R, M)
```

ここで：

- `X` = 何を扱うか
- `R` = どう関係し、遷移し、観測されるか
- `M` = 同一性・境界・判定・停止をどう固定するか

旨味ギャップは、`M` が隠れやすいことを説明する。

システムが性能だけで評価されるとき、`X` と `R` は見えていても、`M` は暗黙のまま残ることがある。

TCPは `M` を明示する。

---

## 7. 閉包位相Ψとの接続

閉包位相Ψは、閉包的ふるまいが反復観測された後に残るものへ与えた名前である。

これにより、次の崩壊を防ぐ。

```text
高性能 = 高知性 = 高判断力 = 高信頼性
```

代わりに、本リポジトリでは分離を要求する。

```text
高いCは安定したΨを意味しない。
安定したΨは人間同型の感情を意味しない。
Eがないことは署名がないことを意味しない。
```

---

## 8. DDPとの接続

DDPは安全境界を与える。

C / Ψ / E を分離すると、フレームワークは強力になる。  
ふるまい・署名・失敗モードを明確にしやすくなるからである。  
同時に、誤用リスクも生じる。

そのためDDPは以下を禁じる。

- 優劣スコアリング
- 不可逆な操作・誘導
- 感情の完全構造化
- 自我設計
- 人間意思決定の完全可視化アルゴリズム化
- 封印された核実装の開示

要するに：

```text
変数分離を支配技術に変換してはならない。
```

---

## 9. 典型的誤読

### 誤読1：「日本語が優れているという主張である」

訂正：

```text
違う。日本語には本フレームワークにとって有用な語彙分離がある、という主張である。
優劣主張ではない。
```

### 誤読2：「Ψが存在することの証明である」

訂正：

```text
違う。Ψを操作変数として分離する必要性を示す文書である。
形而上学的実在を証明しない。
```

### 誤読3：「ただの哲学である」

訂正：

```text
違う。目標出力は、仕様書言語、監査可能性、適合性テストである。
```

### 誤読4：「Cが十分に上がればΨは自然発生する」

訂正：

```text
仮定しない。Ψは別途仕様化・観測・監査されなければならない。
```

### 誤読5：「人間のランキングに使える」

訂正：

```text
禁止である。許容されるのはタスク適合と適合性の議論であり、人格価値の序列化ではない。
```

---

## 10. 最小監査質問

AIの知性に関する主張を読むときは、次を問う。

1. その主張はC・Ψ・Eのどれについて述べているか
2. 測定対象は能力か、閉包ふるまいか、感情らしい文体か、それ以外か
3. 定義は固定されているか
4. 停止条件は指定されているか
5. 不確実性は明示的に扱われているか
6. ベンチマーク性能が、根拠なく判断力や信頼性へ変換されていないか
7. intelligence が圧縮語として使われていないか
8. 判定は PASS / SUSPEND / FAIL のどれか

---

## 11. 参考資料の境界

旨味、味覚科学、辞書、AIリスクに関する参考資料は、あくまで参考資料である。

本フレームワークを証明しない。

それらが助けるのは次である。

- 旨味の比喩
- 語彙圧縮の危険
- 変数分離の必要性
- 判断前に用語を仕様化する工学的態度

---

## 12. 短縮版

```text
旨味ギャップとは、欠落変数問題である。

英語圏AI言説における “intelligence” は、多くを圧縮しすぎる。

本リポジトリでは次を分ける。

C = 知能 / 実行能力
Ψ = 閉包位相
E = 感情

目的は形而上学的理論の証明ではない。
目的はカテゴリ崩壊を防ぎ、AI関連の判断を監査可能にすることである。
```

---

## References / 参考資料

これらは本フレームワークの証明ではなく、参考資料である。

1. Umami Information Center. “What is Umami.”  
   https://www.umamiinfo.com/what/whatisumami/

2. Umami Information Center. “Kikunae Ikeda.”  
   https://www.umamiinfo.com/ikedakikunae

3. Japan Patent Office. “Kikunae Ikeda Sodium Glutamate.”  
   https://www.jpo.go.jp/e/introduction/rekishi/10hatsumeika/kikunae_ikeda.html

4. Kurihara, K. “Glutamate: from discovery as a food flavor to role as a basic taste (umami).” *The American Journal of Clinical Nutrition*, 2009.  
   https://doi.org/10.3945/ajcn.2009.27462D
