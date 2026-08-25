# 認知工学とは何か
## ― Science / Engineering の分別と、全学問の基底工学としての再定義 ―

**版**：v0.1  
**著者**：がっちむち♂  
**文章生成支援**：LLM  
**原典言語**：日本語  

> **言語規定**：本稿は日本語原典を正本とする。英語版は日本語原典成立後に作成された翻訳であり、意味が衝突する場合は日本語原典を優先する。

---

# Part I. 日本語原典

## 1行定義

> **認知工学とは、世界から何を検出し、何を対象として切り出し、どう関係づけ、どう意味づけ、どこで判断し、どこで停止し、どのように再認知するかという、認知そのものの成立・作用・制御を工学対象として扱う基底工学である。**

本稿における認知工学は、心理学の応用分野でも、Human–Computer Interaction の別名でも、人間工学の部分集合でもない。

認知工学は、それらを含むあらゆる学問が成立する以前に必要となる、対象化・差異化・抽象化・関係化・判断・記述・更新という認知操作そのものを扱う。

---

## 要旨

人類は、世界をそのまま記述しているのではない。

何かを検出し、対象として切り出し、差異を認識し、名前を与え、関係を組み、原因を置き、時間や空間を与え、規則や法則として圧縮した後、それを「世界」として記述している。

この一連の操作を経ずに、物理学、数学、医学、言語学、経済学その他の学問は成立しない。

ところが現代の学問体系では、この最上流に存在する認知操作そのものが十分に独立した工学対象として扱われていない。

一方、「認知科学」は、直接観測できない認知そのものを、行動・発話・脳活動・自己報告等の外部観測から構成されたモデルによって対象化し、そのモデルと認知そのものとの境界を曖昧にし得る。

また現在「認知工学」と呼ばれる領域は、認知の何を対象とし、どの状態を目的とし、何を作用させるのかという工学上の核心が曖昧なまま、多数の既存工学領域を包む上位ラベルとして使用される傾向がある。

本稿は、まず Science と Engineering を分別し、次に認知科学および既存認知工学の成立条件を再監査する。

その上で認知を、

> **世界から差異を検出し、切断し、圧縮し、変換するセンサー／前処理系**

として扱い、メタ認知を、

> **その認知出力を監査・校正・抑制・保留・更新する制御系**

として位置づける。

この構造から、認知工学を一専門分野ではなく、あらゆる学問を成立させる前段の操作を扱う**基底工学**として再定義する。

ここでいう「全学問の祖」とは歴史的・制度的な起源を意味しない。

あらゆる学問が成立するために認知操作を必要とするという、**構造上・成立上の上流性**を意味する。

---

# 1. 問題設定

## 1.1 「認知工学」という名称は何を意味するのか

工学には対象が必要である。

さらに、その対象について、

- 何を目的とするのか
- 何を変化させるのか
- どの手段によって作用するのか
- 何をもって目的達成とするのか

が必要になる。

したがって「認知工学」と名乗るのであれば、最低限、

> **認知とは何か。  
> 認知の何を工学対象とするのか。  
> どの状態からどの状態へ変化させるのか。  
> 何を作用させるのか。**

が示されなければならない。

しかし現在「認知工学」と呼ばれる領域では、インターフェース、人間機械系、作業負荷、情報提示、意思決定支援等、多数の異なる実務が同一ラベルに回収される。

各技術や研究の価値を本稿は否定しない。

問題は、

> **それらをまとめて「認知工学」と呼ぶとき、認知という対象そのものが何を意味するのかが失われている**

ことである。

認知工学というラベルが対象を識別できないのであれば、その名称は工学分類として機能していない。

---

# 2. Science と Engineering

## 2.1 Scienceとは何か

本稿では Science を、

> **観測可能な現象・作用・関係に対し、何が成立しているのかを観測し、記述し、説明を更新する営み**

として扱う。

Science の目的は、目的状態を人工的に実現することではない。

まず、

> **何が起きているのか。**

を問う。

ここで重要なのは、モデルと対象を同一視しないことである。

観測された現象からモデルを構築することはできる。

しかし、

> **観測されたもの**

と、

> **観測から構築された説明モデル**

は同一ではない。

Science が成立するには、この境界が保持されなければならない。

## 2.2 Engineeringとは何か

Engineering は Science の応用ではない。

科学的知識を利用することはあるが、それは工学の必要条件ではない。

本稿では Engineering を、

> **目的を置き、対象を定め、対象へ作用する手段を設計し、目的状態を実現し、その結果を観測して再設計する営み**

と定義する。

したがって工学には、対象、目的、手段、作用、結果、評価、帰還が存在する。

Science の中心的な問いが、

> **何が成立しているのか**

であるなら、Engineering の中心的な問いは、

> **どうすれば目的状態を成立させられるのか**

である。

両者は接続する。しかし同一ではない。

---

# 3. 認知科学への批判

## 3.1 認知そのものは直接観測できるのか

人間の認知を外部から直接見ることはできない。

観測できるのは、発話、行動、選択、反応、身体変化、脳活動、自己報告、生成物等である。

これらは認知そのものではない。

**認知を経た後に外へ現れた観測可能な現象**である。

したがって、

> 外部現象  
> → そこから認知過程を推定  
> → 認知モデルを構築

までは可能である。

問題はその次である。

構築したモデルを、

> **認知そのもの**

として扱った瞬間、対象とモデルの境界が崩れる。

## 3.2 モデル化できることと科学対象であることは同じではない

観測できない対象についてモデルを作ることは可能である。

しかし、

> モデルを作れた  
> ＝  
> その対象そのものを観測した

とはならない。

認知科学が外部観測から構成された認知モデルを扱うのであれば、そのモデルは人間が構築した認知後の記述である。

それを対象本体へ昇格させることはできない。

本稿は、脳活動・行動・反応等の観測可能な研究まで否定しない。それらは観測対象として成立し得る。

本稿が批判するのは、

> **観測された現象から構築した「認知」というモデルを、認知そのものと混同したままScienceとして扱うこと**

である。

この境界が明示できない限り、「認知科学」という名称は再監査される必要がある。

---

# 4. 認知とは何か

## 4.1 認知はセンサーである

本稿では認知を、単なる「考える能力」として扱わない。

認知とは、

> **世界から差異を検出し、切り出し、分類し、圧縮し、意味や関係を与え、主体が扱える表現へ変換する系**

である。

工学的には、センサー＋前処理器＋分類器に近い。

ただし通常のセンサーと異なる。

認知は入力を受け取るだけではなく、

> **何を入力として扱うかそのものを決める。**

世界全体がそのまま入力されるのではない。

何かを対象として切り出した時点で、すでに認知が作用している。

## 4.2 認知は世界像を生成する

人間が扱う世界には、主体、対象、同一性、差異、関係、文脈、時間、空間、因果、価値、評価基準、法則、原理等が存在する。

しかし本稿では、これらを最初から世界本体に備わった固定項として扱わない。

これらは少なくとも、

> **人間が世界を認知し、扱える状態へ変換する過程で成立する世界像**

として扱われる。

したがって、

> **人間が語る世界**

と、

> **認知以前の世界本体**

を無条件に同一視することはできない。

この境界の具体的な公開原理として、**神の領域原理（仮）**が存在する。

---

# 5. メタ認知とは何か

認知がセンサーであるなら、そのセンサー自体を無監査で使い続けることはできない。

認知には、誤検出、過剰一般化、固定化、欠落、文脈誤認、因果誤認、対象境界の誤設定が起こり得る。

そこで必要になるのがメタ認知である。

本稿ではメタ認知を、

> **認知出力および認知の仕方そのものを監視し、必要に応じて校正・抑制・保留・更新・再認知する制御系**

として扱う。

工学的には、

> **認知＝センシング系  
> メタ認知＝制御・監査系**

という関係になる。

認知は世界像を生成する。

メタ認知は、その世界像を固定物として信じ込むことを防ぐ。

---

# 6. 認知工学とは何か

以上から、本稿は認知工学を次のように再定義する。

> **認知工学とは、世界から対象・差異・関係・意味・価値・法則等が認知によって成立する過程、およびその認知出力を監査・更新・停止する制御過程を、目的に応じて設計・運用・改善する工学である。**

認知工学が扱うのは、単にUIを分かりやすくすることではない。

情報提示を改善することでもない。

それらは認知工学の応用先となり得るが、認知工学そのものではない。

認知工学の本体は、

> **何を対象として認知するのか。  
> どのような差異を保持するのか。  
> どの関係を成立させるのか。  
> 何を判断として固定するのか。  
> どこで断定を止めるのか。  
> 新しい観測をどこへ帰還させるのか。**

を扱うことである。

---

# 7. なぜ認知工学は全学問の祖なのか

## 7.1 歴史的起源という意味ではない

本稿が、

> **認知工学はあらゆる学問の祖である**

と言うとき、認知工学という名称の学科が物理学や数学より先に存在した、という歴史的主張をしているのではない。

意味は構造的である。

## 7.2 学問が成立するために必要な操作

どの学問であっても、その成立前に必ず、

1. 何かを認知する
2. 対象として切り出す
3. 別のものと区別する
4. 名前を与える
5. 概念として保持する
6. 関係を組む
7. 変化を観測する
8. 記録する
9. 比較する
10. 判断する
11. 説明を作る
12. 必要なら修正する
13. 他者へ伝える

という操作が存在する。

物理学が物理現象を扱う前に、何を物理現象として切り出すかがある。

数学が対象を操作する前に、何を同一とし、何を差異とし、どの関係を採用するかがある。

医学が病態を分類する前に、何を正常とし、何を異常とし、どこまでを一つの状態として扱うかがある。

つまり、

> **各学問が始まる前に、その学問が扱える世界を成立させる認知操作がある。**

認知工学が扱うのは、この前段である。

## 7.3 無名の認知工学は常に存在していた

人類は「認知工学」という名称を持つ以前から、認知を操作してきた。

分類法を作る、単位を作る、記号を作る、言語を作る、図を作る、数式を作る、観測方法を作る、実験方法を作る、判断基準を作る、学問分野を分ける。

これらは全て、

> **人間が世界をどのように認知し、外部化し、再利用可能にするか**

への操作でもある。

したがって認知工学は、新しく人類史へ追加される特殊な営みではない。

> **人類が常に行ってきたにもかかわらず、それ自体が独立した基底工学として十分に認識されてこなかった操作を、改めて対象化する営み**

である。

---

# 8. 認知工学と他学問の位置関係

認知工学を他の学問と横並びに置くと、その位置を誤る。

構造は、

```text
認知
 ↓
対象化・差異化・抽象化・関係化・記述化
 ↓
各学問の対象世界が成立
 ↓
各学問
```

である。

認知工学は、その最上流の操作を工学対象とする。

ゆえに、

> **認知工学は全学問の一分野ではなく、全学問の成立条件を扱う基底工学である。**

---

# 9. 既存認知工学への批判

既存の「認知工学」という名称が扱う個別研究や技術を、本稿は一括して否定しない。

批判するのはその分類構造である。

認知の定義が曖昧なまま、人間機械系、インターフェース、情報提示、作業支援、エラー抑制、意思決定支援等をまとめても、それだけでは「認知工学」にはならない。

それらが、

> **何を認知として扱い、認知のどこへ作用し、どの認知状態を目的としているのか**

を示さない限り、認知は単なる修飾語でしかない。

したがって現在の認知工学は、多くの場合、

> **有用な個別工学を包んでいるが、「認知工学」というラベル自体の識別能力を失っている**

と本稿は批判する。

必要なのは認知工学を捨てることではない。

**認知工学を本来の対象へ戻すことである。**

---

# 10. 認知工学における境界

認知を工学対象として扱えるからといって、認知を完全に解体し、完全に操作し、完全に支配することが正当化されるわけではない。

工学には、

> **できるか**

とは別に、

> **どこまで作用すべきか**

という境界が必要である。

認知そのものを扱う以上、この境界は特に重要になる。

認知を完全に予測・固定・誘導する工学は、人間の意思決定・自律・尊厳その他へ直接接続し得る。

したがって認知工学には、観測境界、作用境界、不可逆性、再設計可能性、停止、未認知・未知の保持が必要になる。

この上位境界を扱う公開原理として、**神の領域原理（仮）**を位置づける。

---

# 11. トリニティ原理との関係

認知された世界を記述するとき、何を対象としているのか、対象がどう関係しているのか、何をもって同一・境界・判断・停止とするのか、という問題が生じる。

この記述・閉包構造を扱う公開原理として、**トリニティ原理**を位置づける。

したがって、

> **神の領域原理（仮）＝認知による世界形成を世界本体へ誤投影しないための上位境界**

> **トリニティ原理＝認知後の対象・関係・閉包を扱う構造原理**

として、両者は認知工学体系の公開原理的実例となる。

両者が認知工学の全てなのではない。

認知工学というより大きな工学体系の中で、それぞれ異なる役割を担う。

---

# 12. Human Decision-making System（仮）

本認知工学体系には、

**Human Decision-making System（仮）**  
**人間意思決定理論（仮）**

が存在する。

略称は **HDS** とする。

本稿における公開情報は名称のみとし、内部構造、運用方法、評価方式、実装その他の詳細は扱わない。

---

# 13. 認知工学と言語

人間が認知したものを、記録、保存、再利用、結合、伝達、継承するためには外部表現が必要になる。

その主要な外部表現の一つが言語である。

したがって、

> **どの言語・記述形式を採用すれば、認知された情報を最も損失少なく、効率的に操作できるのか**

という問いは、認知工学から情報工学へ接続する問題となる。

この問題は別稿『情報工学における言語基底論』で扱う。

---

# 14. 非目標

本稿は、

- 人間の認知を完全に説明すること
- 認知の起動因果を完全に解明すること
- 人間の意思決定を完全可視化すること
- 認知操作による支配技術を提供すること
- 全学問を認知工学へ還元し、各学問の固有性を否定すること

を目的としない。

「全学問の祖」という表現も、各学問は認知工学へ還元できるという意味ではない。

意味は、

> **各学問が成立する前段に認知操作が存在し、その前段自体を工学対象として扱うのが認知工学である**

ということである。

---

# 15. 結論

人類は世界をそのまま学問にしてきたのではない。

世界を認知し、対象を切り出し、差異を作り、名前を与え、関係を組み、説明を作った後で、その対象ごとに学問を作ってきた。

つまり、

> **学問より先に認知がある。**

しかしその認知操作自体は、多くの場合、各学問の暗黙の前提として処理されてきた。

認知科学は、認知そのものを直接観測できないにもかかわらず、外部観測から構築した認知モデルと認知本体との境界を曖昧にし得る。

既存の認知工学は、認知そのものの工学対象を十分に固定しないまま、複数の既存工学を包む曖昧なラベルとなっている。

本稿はこの混線を解く。

> **Science は、何が成立しているかを観測する。**

> **Engineering は、目的に対して対象へ作用し、目的状態を成立させる。**

そして認知工学は、

> **人間が何を世界として認知し、対象化し、関係づけ、判断し、停止し、再び更新するかという、あらゆる学問の成立以前に存在する操作を工学対象とする。**

この意味で、

> **認知工学は、あらゆる学問の祖である。**

それは歴史上最初の学問だからではない。

**あらゆる学問を成立させる前段を扱うからである。**

そして本認知工学体系は、その一部を、神の領域原理（仮）、トリニティ原理その他の理論として外部化している。

認知工学とは、新しい一分野を学問体系の横に追加することではない。

> **人類が学問を作る以前から使い続けてきた最上流の操作を、工学対象として正面から扱うことである。**

---

# Part II. English Translation

# What Is Cognitive Engineering?
## Distinguishing Science from Engineering and Redefining Cognitive Engineering as the Foundational Engineering Upstream of All Academic Disciplines

**Version**: v0.1  
**Author**: Gacchimuchi♂  
**Writing assistance**: LLM  
**Authoritative language**: Japanese  

> **Language rule**: Part I, the Japanese original, is authoritative. This English text was translated only after the Japanese original was established. If meanings conflict, the Japanese original controls.

## One-line definition

> **Cognitive Engineering is the foundational engineering discipline that treats cognition itself—how differences are detected from the world, how targets are cut out, how relations and meanings are formed, where judgments are fixed, where assertion stops, and how cognition is reopened—as an object of engineering.**

Cognitive Engineering in this document is not an applied branch of psychology, another name for Human–Computer Interaction, or a subset of ergonomics.

It addresses the cognitive operations—objectification, differentiation, abstraction, relationalization, judgment, description, and revision—that are required before any academic discipline can exist.

## Abstract

Humans do not describe the world as it is given in itself. They detect something, cut it out as a target, recognize differences, name it, organize relations, assign causes, temporalize and spatialize it, compress repeated patterns into rules or laws, and only then describe the result as “the world.”

Physics, mathematics, medicine, linguistics, economics, and other disciplines cannot exist without these operations.

Yet modern academic organization rarely treats these upstream cognitive operations themselves as an independent engineering target.

At the same time, “cognitive science” can blur the boundary between cognition itself—which is not directly observable from outside—and models of cognition reconstructed from behavior, speech, brain activity, self-report, and other observable outputs.

Likewise, what is currently called “cognitive engineering” often functions as a broad label covering existing engineering practices while leaving unclear what part of cognition is the actual engineering target, what target state is intended, and what mechanism is meant to act on it.

This paper first distinguishes Science from Engineering, then re-audits the conditions under which cognitive science and existing cognitive engineering are said to stand.

It treats cognition as a sensor/preprocessing system that detects, cuts, compresses, and transforms differences from the world, and metacognition as a control system that audits, calibrates, suppresses, suspends, and updates the outputs of cognition.

From this structure, Cognitive Engineering is redefined not as one specialist discipline among others but as a **foundational engineering discipline** dealing with the operations required before any academic discipline can be formed.

Calling it “the ancestor of all disciplines” does not mean historical or institutional priority. It means structural and constitutive upstreamness: every discipline requires cognition before it can constitute its object.

## 1. Problem Statement

Engineering requires an object. It also requires a purpose, a state transition to be achieved, a means of acting on the object, and a criterion for evaluating the result.

Therefore, any field called Cognitive Engineering must at minimum answer:

> **What is cognition?  
> What part of cognition is the engineering target?  
> What state is to be changed into what other state?  
> What is meant to act on it?**

When interface design, human–machine systems, workload, information presentation, and decision support are all collected under one label without answering these questions, the label loses its ability to identify a coherent engineering object.

This paper does not deny the value of individual technologies or studies. It criticizes the classification structure in which “cognition” becomes merely a modifier whose engineering object is left unclear.

## 2. Science and Engineering

### 2.1 Science

In this paper, Science is treated as:

> **the practice of observing phenomena, actions, and relations that can be observed, describing what is established, and updating explanations accordingly.**

Science first asks:

> **What is happening?**

A model may be constructed from observed phenomena, but the observed phenomenon and the explanatory model constructed from observation are not identical. Science requires that this boundary be maintained.

### 2.2 Engineering

Engineering is not merely “applied science.” Scientific knowledge may be used, but it is not a necessary condition of engineering.

Engineering is defined here as:

> **the practice of setting a purpose, defining an object, designing means that act on the object, realizing a target state, observing the result, and feeding the result back into redesign.**

Thus engineering contains object, purpose, means, action, result, evaluation, and feedback.

Science asks what is established. Engineering asks how a target state can be made to hold. They connect, but they are not the same activity.

## 3. Critique of Cognitive Science

Cognition itself cannot be directly observed from outside. What can be observed includes speech, action, choices, responses, bodily changes, brain activity, self-report, and artifacts.

These are not cognition itself. They are phenomena that appear externally after cognition has operated.

It is possible to infer cognitive processes from such phenomena and construct cognitive models. The problem begins when a constructed model is treated as cognition itself.

Being able to model an unobservable target is not the same as having observed the target itself.

This paper does not deny research on observable brain activity, behavior, or responses. It criticizes the treatment of models of “cognition” reconstructed from such observations as if the model and cognition itself were the same scientific object.

If that boundary is not maintained, the category “cognitive science” requires re-audit.

## 4. Cognition

Cognition is not treated here merely as “the ability to think.”

It is:

> **a system that detects differences from the world, cuts them out, classifies and compresses them, gives them meaning and relations, and transforms them into representations that an agent can handle.**

In engineering terms, it resembles a sensor + preprocessor + classifier.

But unlike an ordinary sensor, cognition does not merely receive input. It also determines what is to count as input.

The moment something is cut out as a target, cognition has already intervened.

Cognition therefore generates a world-image. Subject, object, identity, difference, relation, context, time, space, causality, value, judgment criteria, law, and principle are not treated here as fixed items that must already exist in the world-itself. They are at least treated as structures that arise within the world-image through which humans make the world operable.

The public boundary principle governing the distinction between a cognition-after world-image and the pre-cognitive world-itself is **神の領域原理（仮）**.

## 5. Metacognition

If cognition is a sensing system, the sensing system itself cannot remain unaudited.

Cognition may misdetect, overgeneralize, fix prematurely, omit, misread context, misattribute causality, or draw incorrect target boundaries.

Metacognition is therefore treated as:

> **a control system that monitors cognitive outputs and cognitive operations themselves and, when necessary, calibrates, suppresses, suspends, updates, or reopens cognition.**

In engineering terms:

> **Cognition = sensing system  
> Metacognition = control/audit system**

Cognition generates a world-image. Metacognition prevents that world-image from being treated as irrevocably fixed.

## 6. Definition of Cognitive Engineering

Cognitive Engineering is therefore redefined as:

> **the engineering of the processes by which targets, differences, relations, meanings, values, and laws become cognitively constituted from the world, together with the control processes by which those cognitive outputs are audited, updated, suspended, or reopened according to purpose.**

Making a UI easier to understand or improving information presentation may be applications of Cognitive Engineering, but they are not themselves the definition of the field.

The core questions are what is recognized as a target, which differences are preserved, which relations are formed, what is fixed as judgment, where assertion stops, and where new observations are fed back.

## 7. Why Cognitive Engineering Is the Ancestor of All Disciplines

This is not a historical claim that a department called Cognitive Engineering existed before physics or mathematics.

The claim is structural.

Before any discipline exists, someone must recognize something, cut it out as a target, distinguish it from something else, name it, preserve it as a concept, relate it to other things, observe changes, record, compare, judge, construct explanations, revise them, and communicate them.

Before physics can treat a physical phenomenon, cognition has already selected what counts as a physical phenomenon.

Before mathematics can operate on objects, cognition has already fixed what counts as identity, difference, and relation.

Before medicine classifies pathology, cognition has already drawn boundaries around normality, abnormality, and states.

Therefore:

> **Before each academic discipline begins, cognitive operations constitute the world that the discipline can handle.**

Cognitive Engineering deals with that upstream layer.

Humans have always performed unnamed cognitive engineering: building classifications, units, symbols, languages, diagrams, equations, observation methods, experimental procedures, judgment criteria, and academic boundaries.

Cognitive Engineering therefore does not add an exotic new activity to human history. It makes explicit an upstream operation humans have long performed without adequately treating the operation itself as a foundational engineering target.

## 8. Position Relative to Other Disciplines

Cognitive Engineering should not be placed laterally beside physics, chemistry, biology, medicine, mathematics, economics, or linguistics.

Its structural position is:

```text
Cognition
 ↓
Objectification / differentiation / abstraction / relation / description
 ↓
The target-world of each discipline is constituted
 ↓
Each academic discipline
```

Thus Cognitive Engineering is not merely one discipline among others. It is a foundational engineering discipline dealing with conditions under which disciplines themselves become operable.

## 9. Critique of Existing Cognitive Engineering

This paper does not reject the individual studies and technologies currently grouped under “cognitive engineering.”

It criticizes the classification structure.

If human–machine systems, interface design, information presentation, work support, error reduction, and decision support do not identify what they mean by cognition, where they act on cognition, and what cognitive state they intend to realize, then “cognitive” functions only as a decorative modifier.

In that sense, much of current cognitive engineering contains valuable individual engineering work while the label “cognitive engineering” itself has lost discriminative power.

The solution is not to abandon Cognitive Engineering but to return it to its actual object.

## 10. Boundary of Cognitive Engineering

The fact that cognition can be treated as an engineering target does not justify complete decomposition, manipulation, prediction, or domination of cognition.

Engineering requires a boundary separate from the question of what is technically possible.

Because Cognitive Engineering deals with cognition itself, it directly approaches autonomy, decision-making, dignity, irreversibility, and control. It therefore requires observation boundaries, action boundaries, reversibility, stopping, and preservation of the unknown.

The public upper-boundary principle for this role is **神の領域原理（仮）**.

## 11. Relationship to the Trinity Principle

Once a cognition-after world is described, questions arise about what the target is, how targets relate, and what fixes identity, boundary, judgment, and stopping.

The public structural principle handling this description and closure relation is the **Trinity Principle**.

Thus:

> **神の領域原理（仮） = upper boundary preventing cognition-generated world-images from being projected into the world-itself**

> **Trinity Principle = structural principle for target, relation, and closure in cognition-after description**

These are public examples within a larger Cognitive Engineering system. Neither exhausts Cognitive Engineering as a whole.

## 12. Human Decision-making System（仮）

This Cognitive Engineering system includes:

**Human Decision-making System（仮）**  
**人間意思決定理論（仮）**

Abbreviation: **HDS**.

Only the name is public in this paper. Internal structure, operation, evaluation, implementation, and other details are outside scope.

## 13. Cognitive Engineering and Language

Cognitive results require external representation if they are to be recorded, preserved, recombined, transmitted, and inherited. Language is one of the principal external representation systems for this purpose.

The question of which language or descriptive form allows cognitively generated information to be handled with the least loss and highest efficiency connects Cognitive Engineering to Information Engineering.

That question is addressed separately in *A Theory of Language Bases in Information Engineering*.

## 14. Non-goals

This paper does not aim to completely explain cognition, reveal activation causality, fully visualize human decision-making, provide manipulation techniques, or reduce the uniqueness of all disciplines to Cognitive Engineering.

Calling Cognitive Engineering “the ancestor of all disciplines” means only that cognitive operations exist upstream of every discipline and that Cognitive Engineering treats that upstream layer as an engineering object.

## 15. Conclusion

Humans did not directly turn the world-itself into academic disciplines. They first cognized the world, cut out targets, generated differences, named them, built relations and explanations, and only then formed disciplines around those constituted targets.

Therefore:

> **Cognition precedes academic disciplines.**

Science observes what is established. Engineering acts on a defined object to realize a target state.

Cognitive Engineering treats as an engineering object the operations that exist before every discipline: what humans recognize as the world, how they objectify it, relate it, judge it, stop assertion, and reopen it.

In this sense:

> **Cognitive Engineering is the ancestor of all academic disciplines.**

Not because it historically came first, but because it operates on the upstream layer required for all disciplines to become possible.

Cognitive Engineering is not the addition of another specialist field beside existing disciplines. It is the explicit engineering treatment of the most upstream operations humans have used since before academic disciplines were formed.
