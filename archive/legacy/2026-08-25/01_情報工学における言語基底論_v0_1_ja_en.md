# 情報工学における言語基底論
## ― 認知によって生成される情報を、いかに効率よく保持・操作・継承するか ―

**版**：v0.1  
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

したがって情報とは、

> **認知によって生成された対象**

である。

この意味で、「情報科学」という名称には根本的な問題がある。

情報そのものを自然界に独立して存在する対象として発見するのではなく、認知によって成立した情報を、記録・符号化・保存・伝送・検索・変換・結合・計算・再利用するのであれば、その営みは Science ではなく Engineering、すなわち**情報工学**として扱うべきである。

では、情報工学において最も根源的な問題は何か。

それは単なる計算速度でも記憶容量でもない。

> **認知によって得られた情報を、次の処理までどれだけ壊さず運べるか**

である。

人類がこの目的のために長期間使用してきた主要な情報基盤が言語である。

言語は単なる通信手段ではない。

認知結果を外部化し、意味を固定し、関係を保存し、複数人・複数世代・自己の異なる時点間で再利用するための情報操作系である。

したがって、情報を効率よく扱おうとするなら、

> **どの言語が情報工学上の基底表現として適しているのか**

を問う必要がある。

本稿は、日本語が、漢字とかな、意味と音、明示と文脈、固定と未確定を同一記述面で重ねて保持できることに注目する。

その結果、本理論群が要求する、意味の保持、関係の保持、文脈の保持、概念差の保持、未確定性の保持、再解釈可能性、圧縮された状態からの再展開という情報工学上の目的に対して、日本語が現在最も適合する基底言語であると判断する。

したがって本理論群では、

> **日本語で原典を生成し、日本語で監査し、日本語原典成立後にのみ、実務上必要な場合に他言語へ翻訳する。**

この順序を言語運用規定として採用する。

---

# 1. 問題設定

本稿の問いは、

> 日本語と英語のどちらが優秀か。

ではない。

問いは、

> **情報を取り扱うという行為において、最も効率的な方法・表現・操作系は何か。**

である。

したがって、最初に「情報とは何か」を明らかにしなければならない。

言語比較はその後である。

---

# 2. 情報とは何か

## 2.1 情報は世界そのものではない

世界に光がある。音がある。物体がある。変化がある。

しかし、それらがそのまま「情報」であるとは本稿では扱わない。

認知主体が、何かを検出する、他と区別する、一つの対象として切り出す、状態を認識する、他の対象と関係づける、意味を付与することによって初めて、その差異は主体にとって扱える情報となる。

したがって本稿では、

> **情報とは、認知によって世界から切り出され、主体が操作可能な状態へ変換されたもの**

と定義する。

## 2.2 世界 → 認知 → 情報

本稿の基本関係は次である。

```text
世界
 ↓
認知
 ↓
対象化・差異化・関係化・意味化
 ↓
情報
```

情報は認知より上流には置かない。

情報は、認知を経た後に成立する。

したがって、

> **情報は認知の産物である。**

---

# 3. 「情報科学」はなぜ成立しないのか

前稿『認知工学とは何か』では、Science と Engineering を分別した。

Science が問うのは、

> **何が成立しているのか。**

Engineering が問うのは、

> **目的状態を成立させるために、対象へどう作用するか。**

である。

情報は認知によって生成された後段の対象である。

そして一般に「情報」の名の下で行われる主要な営みは、符号化、記録、保存、圧縮、伝送、検索、分類、変換、計算、結合、推論、再利用である。

これらは、

> **情報をどう扱うか**

という操作・設計問題である。

したがって本稿は、

> **情報科学という独立した Science を認めない。**

情報という認知後生成物の性質を利用し、目的に応じて操作する営みは、原理的には**情報工学**である。

既存の「情報科学」という名称の下で行われている個々の有用な研究・技術を否定するものではない。

否定するのは分類である。

実際に行われている工学的営みを、対象の存在様式を再監査しないまま「Science」と呼ぶことを採用しない。

---

# 4. 認知科学との違い

認知科学への批判と情報科学への批判は同じではない。

認知科学の問題は、

> **直接観測できない認知そのものを、認知後の外部現象から構築したモデルによって Science の対象として扱えるのか**

という問題である。

対して情報科学の問題は、

> **その認知によって生成されたさらに下流の対象である情報が、なぜ独立した Science の対象たり得るのか**

という問題である。

位置が異なる。

```text
世界
 ↓
認知          ← 認知科学の成立問題
 ↓
情報          ← 情報科学の成立問題
 ↓
情報操作      ← 情報工学
```

この混線を解かなければ、言語が何を処理しているのかも定まらない。

---

# 5. 情報工学とは何をするのか

情報工学の目的は、情報を存在論的に説明することではない。

認知によって成立した情報を、

> **目的に応じて、損失少なく、効率的に扱うこと**

である。

したがって情報工学では、単純な処理速度だけではなく、必要な意味が残っているか、対象同士の関係が残っているか、文脈が保持されているか、元の差異が消えていないか、未確定なものが勝手に確定されていないか、後から再解釈できるか、別用途へ再利用できるかも性能になる。

本稿ではこれらをまとめて、

> **意味構造保持効率**

と呼ぶ。

---

# 6. 情報量と意味構造保持効率は別である

情報工学というと、bit数、圧縮率、通信速度等が想起されやすい。

これらは重要である。

しかし本稿が扱う効率は、それだけではない。

例えば一文字の記号で巨大な概念集合を参照できるなら、文字数だけを見れば極めて効率的である。

しかしその記号が何を意味するか再構成できなければ、意味処理としては成立しない。

逆に、全てを長文で逐一展開すれば意味は明示できるかもしれない。しかし、そのたびに巨大な再展開を要求するなら操作効率が悪い。

したがって重要なのは、

> **圧縮された状態でも必要な意味構造を保持し、必要なときに再展開できること**

である。

これは通信路上の情報量とは異なる。

---

# 7. 言語とは何か

## 7.1 言語は情報操作基盤である

言語を単なる会話手段として扱うと、その能力を過小評価する。

言語は、認知結果を外部化する、対象へ名前を付ける、差異を保存する、関係を記述する、状態を共有する、過去の認知を未来へ保存する、他者の認知へ入力する、複数の情報を組み合わせる、新しい認知を生成するためのシステムである。

したがって言語は、

> **人類が構築した巨大な情報工学基盤**

として扱える。

## 7.2 口語と記録

人間同士の直接通信には口語が使用できる。

しかし、個体の寿命を越えて情報を保存し、離れた場所へ伝え、巨大な社会で再利用するためには記録系が必要になる。

したがって本稿では、文明規模の情報工学基盤としての言語を、

> **口頭運用＋記録運用**

の双方を含むものとして扱う。

文字以前の口語を直接観測することはできない。

口語が文字より先に存在したという理解は自然な推論ではあるが、文字以前の音声そのものを現在直接参照できるという意味での観測事実ではない。

この区別を維持する。

---

# 8. 日本語の成立構造

本稿では、日本語を単一系統の単純な表音言語として扱わない。

現代日本語には少なくとも、大和言葉を中心とする口語的系譜、漢字・漢文から導入された意味記述・概念記録の系譜、かなによる日本語音声・文法の記録、漢語・和語・外来語の多重運用が重なっている。

歴史的細部の起源を本稿で一意に固定することは目的ではない。

重要なのは現在観測できる結果である。

> **日本語は、意味を強く保持する記号と、音・作用・関係を記述する記号を同一文中で併用する。**

この混成性を、本稿では欠陥ではなく情報処理能力として見る。

---

# 9. 漢字とかな

## 9.1 漢字

漢字は単純な一文字一意味の「表意文字」ではない。

しかし日本語運用において、漢字が音だけではなく、語・概念・意味の識別へ強く作用することは明らかである。

例えば同音であっても、

- 意思
- 意志
- 医師

は記述段階で即座に分離される。

音だけでは同一になる情報が、文字によって別スロットとして保持される。

## 9.2 かな

かなは、日本語の音を記録するだけではない。

特に、助詞、活用、語尾、接続、状態変化、話者態度等を記述するとき、関係情報を担う。

したがって日本語文では概略として、

> **漢字側に意味・概念の核を置き、かな側に関係・作用・状態を流す**

という多層記述が可能になる。

これは厳密な一対一規則ではない。

しかし情報工学的には重要な傾向である。

---

# 10. 日本語は一つの記述面に複数層を重ねる

日本語の重要な性質は、異なる情報層を逐一別構造へ展開せず、一つの文章へ重ねられることである。

文章には同時に、語そのものの意味、漢字が持つ意味差、文法関係、助詞による位置関係、語尾による態度、呼称による関係、敬語による距離、省略された共有情報、前後文脈、あえて確定していない部分が存在できる。

したがって日本語では、

> **情報を完全にフラットな一列へ展開しなくても処理可能である。**

---

# 11. 文脈は欠落ではない

明示されていない情報を全て「欠落」と扱うのは誤りである。

共有された文脈内に存在し、必要に応じて再構成できるなら、それは単純な情報消失ではない。

コンピュータで言えば、毎回全状態をパケットへ再記述するのではなく、

> **既存状態を参照しながら差分のみ操作する**

方式に近い。

日本語では主語や対象を省略できる。

これは常に優れているわけではない。文脈が共有されていなければ誤認を生む。

しかし文脈が共有されている条件では、

> **既知情報を繰り返し送信せず、新しい差分だけを伝達する**

ことが可能になる。

情報工学的には合理的な圧縮方式になり得る。

---

# 12. 未確定性を保持できること

情報処理では「明確であること」が常に正しいとは限らない。

まだ観測されていないもの、複数解釈が残っているもの、判断する必要がないもの、将来の入力によって変化するもの。

これらを早期に一つへ固定すると、情報が増えるのではなく、**可能性空間を勝手に削除する**。

日本語では、主体・確定度・態度・因果等の一部を、必要になるまで文脈の中へ保持する運用が比較的容易である。

本稿では、この性質を、

> **未確定性保持能力**

として情報工学的に評価する。

---

# 13. 英語との比較

## 13.1 英語の価値を否定しない

英語は現在、国際規格、API、ソフトウェア、技術文書、学術流通、国際共同作業において極めて強い実務基盤である。

したがって英語を排除することは合理的ではない。

本稿も英語使用そのものを否定しない。

## 13.2 基底言語として同じ評価にはならない

しかし、

> **外部との接続に便利であること**

と、

> **理論・概念を最初に生成する基底として効率的であること**

は別である。

英語は基本的に音声言語をアルファベットで逐次記録する。

意味差や関係差を保持するには、語彙の選択、語順、修飾、追加説明等によって線形に展開する必要が生じやすい。

日本語では、漢字・かな・助詞・省略・文脈等を併用し、複数情報を異なる層へ配置できる。

したがって本稿では、

> **英語は外部接続に強く、日本語は内部意味構造の保持に強い**

という役割差を置く。

これは普遍的優劣ではなく、本稿の目的に対する工学評価である。

---

# 14. 「12色と36色」の比喩

この差を説明する比喩として、

> **12色の絵具と36色の絵具**

を用いる。

これは日本語の語彙数が英語の3倍だという数量主張ではない。

同じ色を最終的に作れるとしても、初期スロットが少ない系では、複数の色を混合して目的色を生成する必要がある。

初期スロットが多い系では、より多くの中間差異を別の状態として保持したまま操作できる。

本稿が問題にするのは、最終的に表現できるかではない。

> **情報処理途中に、どの程度の差異を別状態として保持できるか**

である。

この意味で語彙・文字・文法・文脈スロットの多重性は、情報工学上の処理能力となる。

---

# 15. 認知様式と言語

本稿は、言語が認知を一方向に決定するという単純な言語決定論を採用しない。

むしろ生成方向としては、

```text
認知様式
 ↓
必要な情報処理形式
 ↓
言語の形成・選択
```

をまず置く。

人間集団がどの差異を重要視し、どのように関係を認識し、どの情報を保存する必要があったかが、言語形成へ作用したと考える方が自然である。

しかし一度言語が成立すると、それは次世代へ継承される。

すると今度は、成立した言語が次世代の認知操作へ作用する。

したがって全体は、

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

という再帰的自己強化系になる。

---

# 16. LLM時代に基底言語と公開言語を分けられる

従来は、最終的な学術公開が英語であるなら、最初から英語で文章を生成する実務上の圧力が存在した。

しかしLLMの登場により、翻訳、対訳、文体変換、用語固定、翻訳差分監査のコストは大幅に下がった。

これによって、

> **理論を生成する言語**

と、

> **外部へ公開する言語**

を一致させる必要性が低下した。

最も意味構造を保持しやすい基底形式で内部生成を行い、最後に要求された外部形式へ変換すればよい。

---

# 17. 日本語基底規定

## 17.1 基底

> **日本語を唯一の基底言語・規定言語とする。**

思考、理論生成、概念定義、仕様、設計、監査、原稿は、原則として日本語で行う。

## 17.2 原典

> **原典は必ず日本語で先に成立させる。**

英語その他の言語と同時並行で正本を生成しない。

## 17.3 多言語

英語その他の言語は、国際公開、外部規格、API、応募、共同作業、その他実務上やむを得ない場合にのみ使用する。

## 17.4 翻訳の位置づけ

多言語版は独立した原典ではない。

> **日本語原典から生成された翻訳物・射影**

として扱う。

翻訳と日本語原典に意味差が生じた場合、日本語原典を優先する。

## 17.5 翻訳によって原典の欠陥が見つかった場合

翻訳時に未定義、意味衝突、曖昧性、関係欠落、説明不足が発見された場合、翻訳側で勝手に確定しない。

日本語原典へ戻り、原典側を再監査・改訂する。

その後、改訂された日本語原典から再翻訳する。

---

# 18. 運用順序

したがって本理論群の言語生成工程を、

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

とする。

これは翻訳方針ではない。

> **理論生成工程そのものの仕様である。**

---

# 19. 認知工学体系との関係

本稿は、独立した言語優越論ではない。

前稿『認知工学とは何か』で示した認知工学体系の下流に位置する。

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

したがって本稿は、

> **認知工学体系における情報外部化・情報操作基盤の言語設計論**

として位置づけられる。

---

# 20. 関連理論

本認知工学体系には少なくとも、

- **神の領域原理（仮）**
- **トリニティ原理**
- **閉包位相Ψ**
- **Human Decision-making System（仮）／人間意思決定理論（仮）**

が存在する。

HDSについて本稿が公開するのは名称のみである。

内部構造、運用方法、評価方法、実装その他は本稿の射程外とする。

---

# 21. 非目標

本稿は、日本人が他言語話者より優れている、日本文化が他文化より優れている、日本語があらゆる用途で世界最高である、英語では高度な思考が不可能である、言語が認知を完全に決定する、日本語が必ず最小トークンになる、日本語が必ず最速通信になる、とは主張しない。

評価対象は限定されている。

> **認知によって生成された情報を、理論生成・構造化・監査・再利用する基底表現としての適合性**

である。

この対象範囲において日本語を採用する。

---

# 22. 再開放条件

日本語基底も絶対的な真理ではない。

以下が観測された場合、本規定は再監査される。

- 日本語より意味構造保持効率の高い言語・記述系が成立した場合
- 日本語固有の認知固定が本理論群に重大な取り零しを生じさせている場合
- 自然言語以外の中間表現が、日本語より高い意味保持・再利用性能を示した場合
- 技術環境の変化によって基底／翻訳分離の合理性が失われた場合

したがって本稿は、

> **日本語が絶対的に優れているから固定する**

とは言わない。

> **現在の対象・目的・手段に対して最も適合しているため採用する。**

---

# 23. 結論

情報は世界にそのまま置かれている物ではない。

人間が世界を認知し、差異を検出し、対象として切り出し、関係と意味を与えることで情報が成立する。

したがって、

```text
世界
 ↓
認知
 ↓
情報
```

である。

認知によって成立した情報を、保存・伝達・変換・計算・検索・結合・再利用する営みは、ScienceではなくEngineeringである。

ゆえに本稿は「情報科学」を採用せず、**情報工学**として扱う。

そして人類にとって、情報を外部化し、保存し、伝達し、再入力する最大級の基盤が言語である。

したがって情報工学は、

> **何語を使うか**

という問題を無視できない。

日本語は、漢字による意味差の保持、かなによる音・作用・関係の記述、助詞・活用・語尾による関係情報、省略による共有状態参照、文脈による差分伝達、未確定性の保持、複数文字体系・語彙系統の同時運用を一つの記述面で扱える。

この構造は、本理論群が要求する意味構造保持効率と高い整合性を持つ。

よって本理論群は、

> **日本語を基底言語・規定言語として採用する。**

そして運用は、

> **日本語原典を先に成立させ、その後、実務上必要な場合のみ他言語へ翻訳する。**

とする。

英語その他の言語を否定するのではない。

役割を分けるのである。

> **日本語は生成基底。  
> 他言語は必要に応じた外部出力。**

原典と翻訳の順序を逆転させない。

なぜなら、

> **外部出力形式の都合によって、理論生成時の情報構造を先に削る合理性はないからである。**

本稿の結論は、日本語への信仰ではない。

**情報を取り扱うという工学行為を、その上流から再検討した結果として得られる設計判断である。**

---

# Part II. English Translation

# A Theory of Language Bases in Information Engineering
## How to Preserve, Operate on, and Inherit Information Generated by Cognition with Maximum Efficiency

**Version**: v0.1  
**Author**: Gacchimuchi♂  
**Writing assistance**: LLM  
**Authoritative language**: Japanese  

> **Language rule**: Part I, the Japanese original, is authoritative. This English text was translated only after the Japanese original was established. If meanings conflict, the Japanese original controls.

## One-line definition

> **A language base in Information Engineering is a foundational representation system for preserving, operating on, and reusing information generated by cognition while losing as little meaning, relation, context, state, and unresolvedness as possible. For this purpose, this paper adopts Japanese as the base language.**

## Abstract

Information is not treated here as something that simply exists in the world as such.

Even if differences and interactions exist in the world, those differences become “information” only after a cognitive agent detects, objectifies, differentiates, relates, and gives them meaning.

Therefore:

> **Information is a product generated by cognition.**

This creates a fundamental problem with the category “Information Science.”

If the actual work performed on information consists of recording, encoding, storing, transmitting, searching, transforming, combining, computing, and reusing information already constituted by cognition, then the activity is not Science but Engineering—specifically, **Information Engineering**.

The most fundamental question in Information Engineering is therefore not only computation speed or memory capacity. It is how much of the cognitively generated structure can be carried into the next operation without being broken.

Language is one of the largest information infrastructures humans have built for this purpose. It externalizes cognition, preserves meanings and relations, and enables reuse across persons, generations, and different moments of the same person.

Therefore Information Engineering must ask which language is most suitable as a base representation for handling information efficiently.

This paper focuses on the ability of Japanese to place kanji and kana, meaning and sound, explicit expression and context, fixed content and unresolved content on the same descriptive surface.

For the objectives required by this theoretical system—preservation of meaning, relations, context, conceptual differences, unresolvedness, reinterpretability, and re-expansion from compressed form—Japanese is adopted as the currently most suitable base language.

Accordingly, the operational rule is:

> **Generate the original in Japanese, audit it in Japanese, establish the Japanese original first, and translate into other languages only when practically necessary.**

## 1. Problem Statement

The question of this paper is not whether Japanese or English is “the better language” in a universal sense.

The question is:

> **What is the most efficient method, representation, and operational system for handling information?**

Language comparison comes only after the nature of information has been fixed.

## 2. What Is Information?

Light, sound, objects, and change may exist in the world. This paper does not treat them as “information” merely by existing.

A cognitive agent must detect something, distinguish it, cut it out as a target, recognize a state, relate it to other targets, and give it meaning before that difference becomes information the agent can operate on.

Thus:

> **Information is what cognition cuts out from the world and transforms into an operable state for an agent.**

The basic relation is:

```text
World
 ↓
Cognition
 ↓
Objectification / differentiation / relationalization / meaning formation
 ↓
Information
```

Information is not placed upstream of cognition. It is constituted after cognition.

## 3. Why “Information Science” Does Not Stand as an Independent Science

The preceding paper distinguishes Science from Engineering.

Science asks what is established. Engineering asks how to act on an object to realize a target state.

Information is a downstream object generated by cognition.

The activities generally conducted under the name “information” include encoding, recording, storing, compressing, transmitting, searching, classifying, transforming, computing, combining, inferring, and reusing.

These are operational and design problems concerning how information is handled.

Therefore this paper does not recognize **Information Science** as an independent Science.

Using the properties of cognitively constituted information and operating on it according to purpose belongs, in principle, to **Information Engineering**.

This does not deny the value of individual studies or technologies currently placed under the label “Information Science.” It rejects the classification that treats such engineering activity as Science without re-auditing the mode in which its object exists.

## 4. Difference from the Critique of Cognitive Science

The critique of Cognitive Science and the critique of Information Science are not the same critique.

The Cognitive Science problem is:

> **Can cognition itself, which cannot be directly observed, be treated as a scientific object through models constructed from cognition-after external phenomena?**

The Information Science problem is further downstream:

> **Why should information, which is itself generated by cognition, stand as an independent object of Science?**

The positions differ:

```text
World
 ↓
Cognition        ← constitution problem of Cognitive Science
 ↓
Information      ← constitution problem of Information Science
 ↓
Information operation ← Information Engineering
```

Unless this distinction is made, it is not even clear what language is processing.

## 5. What Information Engineering Does

Information Engineering does not aim to explain information as an independent ontological substance.

It aims to handle cognitively constituted information with low loss and high efficiency according to purpose.

Performance therefore includes more than processing speed. It includes preservation of meaning, relations, context, differences, unresolved items, reinterpretability, and reusability.

This paper calls the combined property:

> **semantic-structure preservation efficiency**

## 6. Information Quantity and Semantic-Structure Preservation Efficiency Are Different

Bit counts, compression ratios, and transmission speed are important. But they are not the only form of efficiency relevant here.

A very short symbol may reference a huge concept, yet fail as meaningful information if the concept cannot be reconstructed. Conversely, fully expanding every meaning into long text may preserve explicitness but impose excessive operational cost.

The engineering target is therefore:

> **to preserve the semantic structure needed for later processing even in compressed form and to allow re-expansion when required.**

This is distinct from information quantity on a communication channel.

## 7. Language as Information Infrastructure

Language is not merely a conversational medium.

It externalizes cognitive results, names targets, preserves differences, describes relations, shares states, stores past cognition for future use, feeds information into the cognition of others, combines pieces of information, and generates new cognition.

Language can therefore be treated as:

> **a massive information-engineering infrastructure built by humanity.**

Civilizational information engineering requires both oral operation and record operation. Oral language before writing cannot be directly observed today; the claim that oral language preceded writing is treated as a natural inference, not as a directly observed fact about pre-writing speech.

## 8. The Structural Formation of Japanese

Modern Japanese is not treated here as a simple single-system phonographic language.

It layers at least oral lineages centered on native Japanese, semantic and conceptual recording lineages introduced through kanji and kanbun, kana as a system for recording Japanese sound and grammar, and the parallel operation of native, Sino-Japanese, and loan vocabulary.

This paper does not attempt to uniquely settle every historical origin. It focuses on the currently observable result:

> **Japanese uses symbols that strongly preserve semantic distinctions together with symbols that record sound, action, relation, and grammatical operation within the same sentence.**

This hybridity is treated as an information-processing capacity rather than a defect.

## 9. Kanji and Kana

Kanji are not simply “one character, one meaning.” Yet in Japanese usage they strongly support discrimination among words, concepts, and meanings beyond sound alone.

For example, `意思`, `意志`, and `医師` can be separated immediately in writing despite identical pronunciation.

Kana do more than record sound. Particles, inflection, endings, connections, state change, and speaker stance frequently carry relational information through kana-based grammar.

In broad engineering terms, Japanese can place semantic/conceptual cores largely in kanji while allowing relations, operations, and states to flow through kana. This is not a strict one-to-one rule, but it is an important structural tendency.

## 10. Layering Multiple Information Channels on One Descriptive Surface

Japanese can place word meaning, semantic distinctions carried by kanji, grammatical relations, particle relations, speaker stance, social distance, omitted shared information, surrounding context, and intentionally unresolved content on the same textual surface without first flattening all of them into separate explicit structures.

Thus:

> **Japanese can process multiple layers of information without fully expanding them into a single flat sequence.**

## 11. Context Is Not Necessarily Missing Information

Not all information that is not explicitly written is absent.

If it is preserved in shared context and can be reconstructed when needed, it is not simple information loss.

In computing terms, this resembles operating on deltas while referencing an existing state rather than resending the complete state every time.

Japanese often permits omission of subjects or objects. This is not always an advantage; without shared context, omission may cause error. But where context is shared, repeated transmission of known information can be avoided while transmitting only new differences.

## 12. Preserving Unresolvedness

Explicitness is not always optimal information processing.

Items that are unobserved, still admit multiple interpretations, need not yet be judged, or may change with future input should not be forced into premature certainty.

Premature fixing does not add information; it deletes possible states.

Japanese makes it comparatively easy to leave parts of agency, certainty, attitude, and causal commitment inside context until fixation becomes necessary.

This paper evaluates that property as:

> **capacity to preserve unresolvedness**

## 13. Comparison with English

English is an extremely strong practical infrastructure for international standards, APIs, software, technical documentation, academic distribution, and collaboration.

This paper does not reject the use of English.

However, convenience for external connection and efficiency as the language in which theories and concepts are first generated are different objectives.

English usually records speech linearly through alphabetic writing. Maintaining fine semantic and relational differences often requires explicit lexical choice, word order, modification, and additional explanation.

Japanese can distribute information across kanji, kana, particles, omission, and context.

The role distinction adopted here is therefore:

> **English is strong for external connection; Japanese is strong for preservation of internal semantic structure.**

This is an engineering evaluation under a defined purpose, not a universal ranking of languages.

## 14. The “12 Colors and 36 Colors” Analogy

The analogy of a 12-color palette and a 36-color palette is used to describe processing slots, not literal vocabulary counts.

Even when the same final color can be produced, a system with fewer initial slots must mix more states to produce intermediate colors, while a system with more slots can preserve more intermediate differences as distinct states.

The issue is not whether final expression is possible. It is:

> **how many distinctions can remain separately operable during information processing.**

In that sense, multiple lexical, script, grammatical, and contextual slots become information-engineering capacity.

## 15. Cognitive Form and Language

This paper does not adopt a simple one-way linguistic determinism in which language completely determines cognition.

The initial direction is instead modeled as:

```text
Cognitive form
 ↓
Required information-processing form
 ↓
Formation and selection of language
```

Once language is formed and inherited, it also feeds back into the cognitive operations of later generations.

The total relation therefore becomes recursive:

```text
Cognition
 ↓
Language
 ↓
Inheritance
 ↓
Cognition
 ↓
Language
 ↓
...
```

## 16. The LLM Era Allows Base Language and Publication Language to Be Separated

Historically, if academic publication was expected in English, there was practical pressure to generate drafts in English from the beginning.

LLMs sharply reduce the cost of translation, parallel-text generation, style conversion, terminology locking, and translation-difference audit.

Therefore the language used to generate theory no longer needs to be identical to the language used for external publication.

The theory may be generated in the representation that best preserves its semantic structure and only then converted into the required external language.

## 17. Japanese-Base Rule

This theoretical system adopts the following rules:

1. **Japanese is the sole base and normative language.**
2. **The original must first be established in Japanese.**
3. Other languages are permitted only when practically necessary for publication, standards, APIs, applications, collaboration, or equivalent external requirements.
4. Other-language versions are translations/projections generated from the Japanese original, not independent originals.
5. If translation exposes ambiguity, missing definition, relational loss, or semantic conflict, the translator must not silently repair the translation. The Japanese original must be reopened, revised, and then translated again.

## 18. Operational Order

```text
Cognize and think in Japanese
 ↓
Generate theory in Japanese
 ↓
Define and structure in Japanese
 ↓
Audit in Japanese
 ↓
Establish Japanese original
 ↓
Translate only when practically necessary
 ↓
Audit semantic differences against the Japanese original
```

This is not merely a translation policy.

> **It is a specification for the theory-generation process itself.**

## 19. Relationship to the Cognitive Engineering System

This paper is not an independent argument for language superiority.

Its place is downstream of the Cognitive Engineering framework defined in *What Is Cognitive Engineering?*

```text
Cognitive Engineering
 ↓
Cognitive constitution of a world
 ↓
Formation of information
 ↓
Information Engineering
 ↓
Language as information representation and operation base
 ↓
Japanese base
```

It is therefore a theory of language design for information externalization and operation within the larger Cognitive Engineering system.

## 20. Related Theories

This Cognitive Engineering system includes at least:

- **神の領域原理（仮）**
- **Trinity Principle**
- **Closure Phase Ψ**
- **Human Decision-making System（仮）／人間意思決定理論（仮）**

Only the name of HDS is public in this paper. Internal structure, operation, evaluation, implementation, and related details are outside scope.

## 21. Non-goals

This paper does not claim that Japanese people are superior to speakers of other languages, that Japanese culture is universally superior, that Japanese is optimal for every purpose, that advanced thought is impossible in English, that language fully determines cognition, or that Japanese always minimizes tokens or maximizes communication speed.

The evaluation target is limited to:

> **fitness as a base representation for theory generation, structuring, audit, and reuse of information generated by cognition.**

## 22. Reopening Conditions

The Japanese-base rule is not asserted as absolute truth.

It should be re-audited if a language or representation system demonstrates higher semantic-structure preservation efficiency, if Japanese itself creates systematic cognitive omissions in this theoretical system, if a non-natural intermediate representation becomes superior for preservation and reuse, or if technological conditions eliminate the rationale for separating base language from translation language.

Japanese is adopted not because it is declared absolutely superior, but because it is currently the best fit for the defined object, purpose, and operational method.

## 23. Conclusion

Information is not treated as something lying in the world waiting to be collected. It becomes information when cognition detects differences, cuts out targets, and assigns relations and meanings.

Thus:

```text
World
 ↓
Cognition
 ↓
Information
```

Operating on cognitively constituted information through storage, transmission, transformation, computation, search, combination, and reuse is Engineering, not Science. This paper therefore rejects “Information Science” as the governing category and treats the domain as **Information Engineering**.

Language is one of humanity’s largest infrastructures for externalizing, preserving, transmitting, and reinserting information.

Japanese can combine semantic distinctions through kanji, sound and relational description through kana, grammatical relations through particles and inflection, shared-state reference through omission and context, preservation of unresolvedness, and multiple script/vocabulary systems on one descriptive surface.

This structure aligns strongly with the semantic-structure preservation efficiency required by this theoretical system.

Therefore:

> **Japanese is adopted as the base and normative language.**

The Japanese original is established first. Other languages are produced afterward only when practically necessary.

The conclusion is not an act of faith in Japanese. It is an engineering decision obtained by reconsidering information-handling from its cognitive upstream conditions.
