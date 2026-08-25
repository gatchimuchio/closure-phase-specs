# 情報工学における言語基底論
## ― 認知によって生成される情報を、いかに効率よく保持・操作・継承するか ―

**版**：v0.2  
**著者**：がっちむち♂  
**文章生成支援**：LLM  
**原典言語**：日本語  

> **言語規定**：本稿は日本語原典を正本とする。英語版は日本語原典成立後に作成された翻訳であり、意味が衝突する場合は日本語原典を優先する。

---

# Part I. 日本語原典

## 1行定義

> **情報工学における言語基底とは、認知によって生成された情報を、意味・関係・文脈・状態・未確定性を可能な限り失わず、効率的に保持・操作・再利用するための基礎表現系である。本稿は、この目的に対して日本語を基底言語として採用する。**

---

## 要旨

情報は世界にそのまま存在する物ではない。

世界に何らかの差異や作用が存在するとしても、それが「情報」として成立するためには、認知主体による検出、対象化、差異化、関係化、意味づけ等を必要とする。

したがって、

> **情報は認知の産物である。**

本稿の基本関係は、

```text
世界
↓
認知
↓
情報
↓
情報の操作
```

である。

この構造から、本稿は「情報科学」を独立した Science として採用しない。情報は認知より下流で成立する認知後生成物であり、その記録・符号化・保存・伝送・検索・変換・結合・計算・再利用は、情報をどう扱うかという目的付きの操作・設計問題である。したがって本稿では、その営みを**情報工学**として扱う。

情報工学の性能は、単なるbit数、通信速度、圧縮率、計算速度だけでは決まらない。認知によって成立した意味・関係・文脈・差異・未確定性を、次の処理までどれだけ壊さず運べるかも重要である。本稿はこれを**意味構造保持効率**と呼ぶ。

人類がこの目的のために長期間使用してきた主要な情報操作基盤が言語である。言語は会話手段にとどまらず、認知結果を外部化し、名前を与え、差異を保存し、関係を記述し、時間を越えて保存し、他者や次世代の認知へ再入力する情報工学基盤である。

本稿は、この目的において日本語の構造を評価する。日本語は、漢字・かな・助詞・活用・語尾・省略・文脈等を同一記述面で併用し、意味・関係・態度・共有状態・未確定性を複数層として保持できる。この特徴は、本理論群が要求する理論生成・構造化・監査・再利用に高い適合性を持つ。

したがって本理論群では、

> **日本語を唯一の基底言語・規定言語とし、日本語原典を先に成立させ、実務上必要な場合のみ後段で他言語へ翻訳する。**

---

# 1. 情報とは何か

世界に光、音、物体、変化があるとしても、本稿はそれらを存在するだけで「情報」とは呼ばない。

認知主体が何かを検出し、他と区別し、対象として切り出し、状態を認識し、他の対象と関係づけ、意味を与えることで、その差異は主体が扱える情報になる。

したがって本稿では、

> **情報とは、認知によって世界から切り出され、主体が操作可能な状態へ変換されたもの**

と定義する。

情報は認知より上流には置かない。

```text
世界
↓
認知
↓
対象化・差異化・関係化・意味化
↓
情報
```

---

# 2. 「情報科学」はなぜ成立しないのか

前稿『認知工学とは何か』で分別した通り、Science は観測可能な現象・作用・関係について何が成立しているかを観測する営みであり、Engineering は目的を置き、対象へ作用し、目的状態を実現する営みである。

情報は認知によって成立した後段の対象である。

一般に「情報」の名の下で行われる主要な営みは、符号化、記録、保存、圧縮、伝送、検索、分類、変換、計算、結合、推論、再利用等である。

これらは、

> **情報をどう扱うか**

という操作・設計問題である。

したがって、

> **本稿は「情報科学」という独立した Science を認めない。**

既存の「情報科学」という名称の下で行われている個々の有用な研究・技術を否定するものではない。否定するのは分類である。

認知によって生成された情報を目的に応じて扱う営みは、原理的には**情報工学**である。

---

# 3. 認知科学への批判との違い

認知科学への批判と情報科学への批判は同じではない。

認知科学の問題は、

> **直接観測できない認知そのものを、認知後の外部現象から構築したモデルによって Science の対象として扱えるのか。**

という問題である。

情報科学の問題はさらに下流にある。

> **その認知によって生成された情報が、なぜ独立した Science の対象たり得るのか。**

という問題である。

```text
世界
↓
認知       ← 認知科学の成立問題
↓
情報       ← 情報科学の成立問題
↓
情報操作   ← 情報工学
```

二つの批判は成立位置が異なる。

---

# 4. 情報工学とは何をするのか

情報工学の目的は、情報を独立した存在論的実体として説明することではない。

> **認知によって成立した情報を、目的に応じて、損失少なく、効率的に扱うこと。**

である。

したがって性能には、単純な処理速度だけでなく、次も含まれる。

- 必要な意味が保持されているか
- 対象間の関係が保持されているか
- 文脈が保持されているか
- 元の差異が潰れていないか
- 未確定なものが勝手に確定されていないか
- 後から再解釈できるか
- 別用途へ再利用できるか

本稿ではこれらをまとめて、

> **意味構造保持効率**

と呼ぶ。

---

# 5. 情報量と意味構造保持効率は別である

bit数、圧縮率、通信速度、計算速度は重要である。しかし、それだけでは認知によって生成された情報の取り扱い効率を評価できない。

極端に短い記号で巨大な概念を参照できても、その概念を再構成できなければ意味処理として成立しない。

逆に、すべてを長文で逐一展開すれば明示性は増えるが、常に巨大な再展開を要求するなら操作効率は低い。

したがって重要なのは、

> **圧縮された状態でも必要な意味構造を保持し、必要なときに再展開できること。**

である。

本稿でいう効率は、通信路上の情報量だけを指さない。

---

# 6. 言語は情報操作基盤である

言語は単なる会話手段ではない。

言語は、認知結果を外部化し、対象へ名前を与え、差異を保存し、関係を記述し、状態を共有し、過去の認知を未来へ保存し、他者の認知へ入力し、複数の情報を組み合わせ、新しい認知を生成する。

したがって、

> **言語は、人類が構築した巨大な情報工学基盤である。**

文明規模の情報継承には、口頭運用だけでなく記録運用が必要になる。

なお、文字以前の口語を直接観測することはできない。口語が文字より先に存在したという理解は自然な推論であるが、文字以前の音声そのものを現在直接参照できるという意味での観測事実ではない。本稿はこの区別を維持する。

---

# 7. 日本語の構造

本稿では、日本語を単純な単一系統の表音言語として扱わない。

現代日本語では、大和言葉を中心とする口語的系譜、漢字・漢文を通じて取り込まれた意味記述・概念記録の系譜、かなによる日本語音声・文法の記録、漢語・和語・外来語の多重運用が重なっている。

歴史的起源の全てを本稿で一意に固定することは目的ではない。

重要なのは現在観測できる構造である。

> **日本語は、意味差を強く保持する記号と、音・作用・関係・状態を記述する記号を同一文中で併用できる。**

この混成性を、本稿では情報処理能力として評価する。

---

# 8. 漢字とかな

漢字は単純な「一文字一意味」ではない。しかし日本語運用では、音だけでは重なる語・概念を記述段階で分離する強い働きを持つ。

例えば、

```text
意思
意志
医師
```

は同音でも、文字によって別の意味スロットとして保持される。

かなは音を記録するだけではない。助詞、活用、語尾、接続、状態変化、話者態度等を担い、関係情報の保持へ作用する。

本稿の比較モデルでは、日本語文は概略として、

> **漢字側に意味・概念の核を置き、かな側に関係・作用・状態を流す。**

という多層記述を可能にする。

これは厳密な一対一規則ではなく、情報工学上の構造傾向として扱う。

---

# 9. 文脈は必ずしも欠落ではない

明示されていない情報を、すべて欠落とみなすことはできない。

共有文脈内に保持され、必要に応じて再構成可能であれば、それは単純な情報消失ではない。

コンピュータで言えば、毎回全状態を送信するのではなく、既存状態を参照しながら差分を操作する方式に近い。

日本語では主語や対象を省略できる。文脈が共有されていなければ誤認を生むが、共有文脈が成立している条件では、既知情報を繰り返さず、新しい差分だけを伝達できる。

これは情報工学的には圧縮として機能し得る。

---

# 10. 未確定性を保持する

情報処理において、常に早く明確化することが最適とは限らない。

未観測、複数解釈、現時点で判断不要、将来入力によって変化する項目を早期に一つへ固定すると、情報が増えるのではなく可能性空間を削除する。

日本語は、主体・確定度・態度・因果等の一部を、必要になるまで文脈内に保持する運用と相性がよい。

本稿はこの性質を、

> **未確定性保持能力**

として評価する。

---

# 11. 英語との比較

英語は、国際規格、API、ソフトウェア、技術文書、学術流通、国際共同作業において極めて強い実務基盤である。

本稿は英語の使用を否定しない。

しかし、

> **外部接続に強いこと**

と、

> **理論・概念を最初に生成する基底として意味構造を保持しやすいこと**

は別の評価軸である。

本稿の比較モデルでは、英語はアルファベットによる線形記述を中心とし、細かな意味差・関係差を保持する際に、語彙選択、語順、修飾、説明追加等による明示展開を要求しやすい。

日本語は、漢字、かな、助詞、活用、省略、文脈等へ異なる情報を分散できる。

したがって本稿では、目的を限定した上で、

> **英語は外部接続に強く、日本語は内部意味構造の保持に強い。**

という役割差を置く。

これは人間・民族・文化の優劣評価ではない。情報工学上の基底表現に対する目的適合評価である。

---

# 12. 「12色と36色」の比喩

本稿では、言語の差を説明するために「12色の絵具と36色の絵具」という比喩を用いる。

これは日本語の語彙数が英語の3倍だという数量主張ではない。

同じ最終色を作れるとしても、初期スロットが少ない系では複数状態を混合して中間色を作る必要があり、初期スロットが多い系ではより多くの中間差異を別状態のまま保持できる。

本稿が問題にするのは、

> **最終的に表現できるかではなく、情報処理途中にどの程度の差異を別状態として保持できるか。**

である。

---

# 13. 認知様式と言語

本稿は、言語が認知を一方向に完全決定するという単純な言語決定論を採用しない。

生成方向としては、まず、

```text
認知様式
↓
必要な情報処理形式
↓
言語の形成・選択
```

を置く。

人間集団がどの差異を重視し、どう関係を認識し、何を記録する必要があったかが、言語形成へ作用したと考える。

一度言語が成立し継承されると、今度はその言語が次世代の認知操作へ作用する。

```text
認知
↓
言語
↓
継承
↓
認知
↓
言語
↓
……
```

したがって、認知と言語は再帰的に自己強化し得る。

---

# 14. LLM時代の言語分業

従来、最終公開先が英語であるなら、最初から英語で論文・仕様を生成する実務圧力が存在した。

LLMによって、翻訳、対訳、文体変換、用語固定、翻訳差分監査のコストは大幅に低下した。

その結果、

> **理論を生成する言語**

と、

> **外部へ公開する言語**

を同一にする必要性は低下した。

最も意味構造を保持しやすい言語で原典を成立させ、その後、必要な出力先へ変換すればよい。

---

# 15. 日本語基底規定

本理論群では次を規定する。

1. **日本語を唯一の基底言語・規定言語とする。**
2. **原典は必ず日本語で先に成立させる。**
3. 英語その他の言語は、国際公開、規格、API、応募、共同作業その他、実務上必要な場合にのみ使用する。
4. 多言語版は日本語原典から生成された翻訳・射影であり、独立した正本としない。
5. 翻訳で未定義・意味衝突・関係欠落・説明不足が発見された場合、翻訳側で勝手に補完せず、日本語原典を再監査・改訂してから再翻訳する。

運用順序は次である。

```text
日本語で認知・思考
↓
日本語で理論生成
↓
日本語で定義・構造化
↓
日本語で監査
↓
日本語原典成立
↓
必要な場合のみ他言語へ翻訳
↓
日本語原典との意味差監査
```

これは翻訳方針ではなく、

> **理論生成工程そのものの仕様である。**

---

# 16. 認知工学体系との関係

本稿は独立した言語優越論ではない。

```text
認知工学
↓
認知による世界の対象化
↓
情報の成立
↓
情報工学
↓
情報表現・操作基盤としての言語
↓
日本語基底
```

という位置にある。

本認知工学体系には、**神の領域原理（仮）**、**トリニティ原理**、**閉包位相Ψ**が存在する。

また、次の名称が存在する。

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

本稿でHDSについて公開するのは名称のみである。

---

# 17. 非目標と再開放

本稿は、日本人・日本民族・日本文化が他者より優れているとは主張しない。英語で高度な思考が不可能だとも主張しない。日本語が常に最少トークン・最高通信速度になるとも主張しない。

評価対象は限定されている。

> **認知によって生成された情報を、理論生成・構造化・監査・再利用する基底表現としての適合性。**

日本語より高い意味構造保持効率を持つ記述系が成立した場合、日本語固有の認知固定が重大な取り零しを生む場合、自然言語以外の中間表現がより適合する場合、本規定は再監査される。

---

# 18. 結論

情報は世界にそのまま置かれている物ではない。

> **世界 → 認知 → 情報**

である。

認知によって成立した情報を保存・伝達・変換・計算・検索・結合・再利用する営みは、Science ではなく Engineering である。

したがって本稿は「情報科学」を採用せず、**情報工学**として扱う。

言語は、人類が認知によって生成した情報を外部化・保存・伝達・再入力する巨大な情報工学基盤である。

日本語は、漢字による意味差の保持、かなによる音・作用・関係の記述、助詞・活用・語尾による関係情報、文脈による共有状態参照、未確定性の保持、複数文字体系・語彙系統の同時運用を一つの記述面で扱える。

この構造は、本理論群の意味構造保持効率という目的に高く適合する。

よって、

> **日本語を基底言語・規定言語として採用する。**

原典を日本語で先に成立させ、その後、実務上必要な場合のみ他言語へ翻訳する。

これは日本語への信仰ではない。情報を取り扱うという工学行為を、その認知上流から再検討した結果として得られる設計判断である。

---

# Part II. English Translation

# A Theory of Language Bases in Information Engineering
## Efficiently Preserving, Operating on, and Inheriting Information Generated by Cognition

**Version**: v0.2  
**Author**: がっちむち♂  
**Writing assistance**: LLM  
**Authoritative language**: Japanese  

> **Language rule**: Part I, the Japanese original, is authoritative. This English translation was produced only after the Japanese original was established.

## Core definition

> **A language base in Information Engineering is a foundational representation system for preserving, operating on, and reusing information generated by cognition while losing as little meaning, relation, context, state, and unresolvedness as possible. For this purpose, this paper adopts Japanese as the base language.**

## World → Cognition → Information

This paper does not treat information as an object that simply exists in the world as such.

Differences and interactions become information for an agent only after cognition detects, objectifies, differentiates, relates, and gives them meaning.

```text
World
↓
Cognition
↓
Information
↓
Information operation
```

Therefore, information is treated as a product of cognition.

## Why this paper rejects “Information Science”

Science, as defined in the preceding paper, observes observable phenomena, actions, and relations and asks what is established. Engineering sets a purpose and acts on a defined object to realize a target state.

Encoding, recording, storing, compressing, transmitting, searching, classifying, transforming, computing, combining, inferring, and reusing information are operational and design problems concerning how cognitively constituted information is handled.

Therefore this paper does not recognize “Information Science” as an independent Science. It treats this domain, in principle, as **Information Engineering**.

This critique differs from the critique of Cognitive Science. Cognitive Science attempts to science cognition itself through models reconstructed from cognition-after observable phenomena. Information Science places a further-downstream product of cognition—information—as an independent scientific object. The failures occur at different layers.

## Semantic-structure preservation efficiency

Information-engineering efficiency is not exhausted by bit count, compression ratio, transmission speed, or computation speed.

It also includes how much meaning, relation, context, difference, unresolvedness, reinterpretability, and reusability survive into later operations.

This paper calls this combined property **semantic-structure preservation efficiency**.

## Language as information infrastructure

Language externalizes cognitive results, names targets, preserves differences, describes relations, stores cognition across time, reinserts it into other agents, and supports recombination.

Language is therefore treated as a large-scale information-engineering infrastructure.

## Why Japanese is selected

Japanese can distribute different informational functions across kanji, kana, particles, inflection, endings, omission, and context on one descriptive surface.

Kanji can preserve distinctions among homophones and concepts. Kana-based grammar carries sound, relation, action, state, and stance. Shared context can reduce repeated transmission of known state. Unresolved agency, certainty, or causal commitment can remain unforced until fixation becomes necessary.

The comparison in this paper is purpose-specific:

> **English is strong for external connection; Japanese is strong for preserving internal semantic structure.**

This is not a ranking of people, ethnic groups, or cultures. It is an engineering evaluation of a base representation under a defined objective.

## 12 colors / 36 colors

The “12 colors and 36 colors” analogy does not claim literal vocabulary ratios. It describes the number of intermediate distinctions that can remain independently operable during processing.

The question is not whether the same final expression can eventually be produced. It is how many distinctions can remain separate before they must be mixed or expanded.

## Japanese-first rule

This theoretical system adopts the following process:

```text
Think and generate in Japanese
↓
Define and structure in Japanese
↓
Audit in Japanese
↓
Establish the Japanese original
↓
Translate only when practically necessary
↓
Audit differences against the Japanese original
```

Other-language versions are translations/projections, not independent originals. If translation exposes a defect, the Japanese original is reopened and corrected first.

## Related public theories

This Cognitive Engineering system includes **神の領域原理（仮）**, the **Trinity Principle**, and **Closure Phase Ψ**.

Only the following HDS names are public here:

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

## Conclusion

The Japanese-base rule is not an act of faith in Japanese. It is an engineering decision derived from the question of how cognitively generated information can be preserved and operated on with low semantic loss during theory generation, structuring, audit, and reuse.
