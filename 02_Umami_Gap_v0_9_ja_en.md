# 旨味ギャップ
## ― intelligence の語彙圧縮と、欠落変数を見えなくする言語スロット問題 ―

**版**：v0.9  
**著者**：がっちむち♂  
**文章生成支援**：LLM  
**原典言語**：日本語  

> **言語規定**：本稿は日本語原典を正本とする。英語版は後段の翻訳である。

---

# Part I. 日本語原典

## 1行定義

> **旨味ギャップとは、本来分けるべき複数の変数が一つの馴染みある語へ圧縮されることで、欠落している変数そのものを観測・定義・設計しにくくなる構造的ギャップである。**

本稿では、英語圏AI言説における `intelligence` を代表例として扱う。

---

## 1. 位置づけ

本稿は認知工学体系の導入アダプタであり、中核原理ではない。

前段の『認知工学とは何か』『情報工学における言語基底論』を受け、言語上の概念圧縮が工学的な変数欠落へどう接続するかを説明する。

比喩として「旨味」を用いるが、味覚研究が本理論群を証明するという主張はしない。

---

## 2. 問題：一語が複数の変数を飲み込む

日常語は厳密な変数分離を目的としていない。そのため、一語が複数の近接概念を担うこと自体は異常ではない。

しかし、工学では問題になる。

ある語が複数の異なる機能を圧縮すると、測定・設計・監査の対象が混線するからである。

AI領域で `intelligence` は、能力、知識、推論性能、判断、停止、一貫性、人格印象、感情的な表出等を横断して使われやすい。

そこで本稿は、少なくとも次を分ける。

```text
C = Capability / 知能・実行能力
Ψ = 閉包位相 / Closure Phase
E = Emotion / 感情
```

必要に応じて知識Kや外生制約A等を別に扱う。

---

## 3. 欠落変数は増量では生まれない

あるモデルに必要な変数スロットが存在しない場合、既存変数を増量しても欠落変数は自動的に現れない。

旨味の比喩で重要なのはここである。

既存の味カテゴリだけで記述している間、既存カテゴリを強めても「別の変数スロット」は立たない。独立した差異として切り出し、名前を与え、観測可能な位置を与えることで初めて、別変数として扱える。

同様に、

> **Cを増やしても、Ψの定義・観測・安定性が自動的に与えられるわけではない。**

性能向上と、閉包・停止・境界・署名の安定は別問題である。

---

## 4. 日本語との関係

本稿は、言語を人間・民族・文化の優劣スコアへ接続しない。

一方で、**特定の情報工学目的に対する言語表現の適合性比較は許容する。**

『情報工学における言語基底論』では、日本語が意味・関係・文脈・未確定性の保持に高い適合性を持つという工学評価を行っている。

これは「日本人が英語話者より優れている」という主張ではない。

本稿が扱うのは、語彙・文字・文法・文脈が、どの差異を独立したスロットとして保持しやすいかという**表現系の設計問題**である。

---

## 5. C / Ψ / E の最小分離

### C — Capability

出力生成、処理、探索、推論、記憶等を可能にする実行能力側。

### Ψ — 閉包位相

固定条件下の反復観測において、閉包的作用の結果として外部へ残る安定した出力相。

### E — Emotion

CやΨと同一視しない感情・情動側の要因。

この分離は人格価値の序列化を目的としない。

---

## 6. 工学上の帰結

CとΨを分けない場合、次の短絡が起こりやすい。

```text
高いベンチマーク性能
→ 高い判断能力
→ 高い停止能力
→ 高い信頼性
```

この連鎖は自動的には成立しない。

したがって、

> **能力の向上を、閉包・判断・停止・信頼性の向上として無条件に読み替えない。**

ことが必要になる。

---

## 7. 他文書との関係

- **トリニティ原理**：対象・関係・閉包をどう記述するかを扱う。
- **閉包位相Ψ**：本稿で分離したΨを操作的に定義する。
- **神の領域原理（仮）**：認知後に成立した変数・モデルを世界本体へ誤投影しない境界を与える。

本稿はこれらの証明ではなく、なぜ変数分離が必要になるのかを説明する導入文書である。

---

## 8. 誤用防止

本稿を、次へ接続してはならない。

- 人間・民族・文化・言語話者の価値序列化
- C / Ψ / E を用いた人格査定
- 欠落変数という言葉を権威の盾として使うこと
- 変数分離を支配・操作技術へ接続すること
- 認知後モデルを認知以前の世界本体として扱うこと

---

## 9. 結論

旨味ギャップの核心は、

> **存在しないのではなく、独立変数として切り出すスロットがないために見えない。**

という問題である。

AIにおける `intelligence` の一語圧縮は、能力、閉包、判断、感情等の異なる対象を混線させる。

本稿はその混線を切るため、C / Ψ / E 等を別変数として扱う。

目的は言語や人間の優劣判定ではない。

> **情報工学上、必要な差異を必要な差異として保持し、設計・観測・監査可能にすること。**

である。

---

# Part II. English Translation

# The Umami Gap
## Lexical Compression of “Intelligence” and the Missing-Variable Slot

**Version**: v0.9  
**Author**: がっちむち♂  
**Writing assistance**: LLM  
**Authoritative language**: Japanese

> The Japanese original above is authoritative. This English section is a later translation.

## One-line definition

> **The Umami Gap is the structural gap that appears when variables that should be separated are compressed into one familiar word, making a missing variable difficult to observe, define, and engineer.**

In AI discourse, this paper uses `intelligence` as a representative example.

## Core separation

```text
C = Capability
Ψ = Closure Phase
E = Emotion
```

The point is not that the umami analogy proves this framework. The analogy illustrates a missing-variable problem: increasing existing variables does not automatically create a separate variable slot.

Therefore:

> **Scaling C does not automatically define, stabilize, or improve Ψ.**

## Language and engineering comparison

This paper prohibits ranking people, ethnic groups, cultures, or language speakers.

It does **not** prohibit purpose-specific engineering comparison of representation systems. The companion paper *A Theory of Language Bases in Information Engineering* evaluates Japanese as a base language for preserving semantic structure under a defined engineering objective.

That is an evaluation of a representation system, not a claim of human superiority.

## Relationship to other documents

- **Trinity Principle**: methodology for target, relation, and closure.
- **Closure Phase Ψ**: operational definition of Ψ.
- **神の領域原理（仮）**: upper boundary preventing cognition-after variables and models from being projected into the pre-cognitive world-itself.

## Conclusion

The Umami Gap is a missing-variable problem. The engineering task is to preserve necessary distinctions as independently operable distinctions instead of compressing them into one ambiguous word.
