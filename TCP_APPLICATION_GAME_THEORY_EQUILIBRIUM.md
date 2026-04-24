# TCP Application Example: Game Theory and Equilibrium
## Describing Strategic Interaction Through X / R / M, SUSPEND, Ψ, and DDP

**Repository position:** TCP application example  
**Version:** v0.1-public-bilingual  
**Status:** Application framework example, not a core specification  
**Language order:** English projection first / Japanese reference second  
**Author:** Gacchimuchi  
**Writing assistance:** LLM  
**License:** CC BY 4.0 for document text unless otherwise noted

---

## Status of This Document

This document describes game theory and equilibrium through the lens of this repository’s framework:

```text
TCP = Three-Term Closure Principle
Ψ   = Closure Phase
DDP = Divine Domain Principle / Shiniki Principle
```

This is not a replacement for standard game theory.  
It is not a proof that TCP, Ψ, or DDP are true.  
It is an application example showing how strategic interaction can be rewritten as a closure problem.

The purpose is:

```text
To show how “game,” “strategy,” “payoff,” and “equilibrium” can be treated as X / R / M-closed objects.
```

---

## Conventional Background

In standard game theory, a game is a formal model of interdependent decision-making. Players choose strategies, outcomes are determined, and payoffs represent what each player receives.

A Nash equilibrium is commonly described as a strategy profile in which no player can improve their own expected outcome by changing only their own strategy, given the other players’ strategies.

This document accepts that conventional definition as the starting point, but rewrites it in TCP terms.

---

## One-Line Rewriting

In TCP terms:

```text
A game is a closed strategic world W := (X, R, M).
```

An equilibrium is:

```text
A state that remains stable under the deviation rule fixed by M.
```

That is:

```text
Equilibrium is not “good.”
Equilibrium is “non-deviating under the specified closure conditions.”
```

---

## TCP Mapping

| Game theory term | TCP interpretation |
|---|---|
| Players | Part of X |
| Strategies | Part of X |
| Payoffs | Part of X and M |
| Rules of interaction | R |
| Best-response relation | R |
| Rationality assumption | M |
| Information condition | M |
| Binding agreement condition | M |
| Deviation rule | M |
| Equilibrium | A fixed point under R and M |
| Multiple equilibria | Multiple closed fixed points under the same or different M |
| No clear equilibrium selection | SUSPEND |
| Pareto-inferior equilibrium | Stable but not desirable |
| Repeated game | Dynamic W across time |
| Mixed strategy equilibrium | Closure over probability distributions |

---

## Why TCP Is Useful Here

Standard game theory often hides important assumptions inside the model:

- who the players are;
- what strategies exist;
- whether payoffs are fixed;
- whether agreements are binding;
- whether the game is one-shot or repeated;
- whether information is complete;
- whether players optimize individual payoff, group payoff, reputation, survival, or something else;
- whether equilibrium selection is specified.

TCP forces these assumptions into explicit slots:

```text
X = players, strategies, payoffs, game scope
R = response relation, transition, best-response mapping
M = rationality, information, deviation, stopping, and judgment rules
```

If any of these remain underdefined, the correct result is not over-interpretation.

The correct result is:

```text
SUSPEND
```

---

## Equilibrium as Closure

A Nash-style equilibrium can be rewritten as:

```text
Given W := (X, R, M),
a strategy profile s* is an equilibrium
if no player i has an allowed unilateral deviation d_i
that improves i's payoff under M,
while all other players' strategies remain fixed.
```

In this framing, equilibrium depends on M.

If M changes, equilibrium may change.

Examples of M-sensitive conditions:

- one-shot vs repeated game;
- complete vs incomplete information;
- binding vs non-binding agreement;
- individual payoff vs collective payoff;
- risk-neutral vs risk-averse evaluation;
- static payoff vs reputation-sensitive payoff;
- visible vs hidden action;
- allowed vs prohibited strategies.

Therefore:

```text
Equilibrium is not an object floating in the world.
It is a closure result under fixed rules.
```

---

## DDP Boundary: Equilibrium Is Not Ethical Approval

DDP adds an important constraint:

```text
Stable does not mean desirable.
```

A harmful pattern may be an equilibrium.  
A coercive structure may be stable.  
A bad institution may persist because unilateral deviation is costly.  
A socially inferior result may be individually rational.

Therefore, equilibrium must not be confused with:

- justice;
- desirability;
- safety;
- morality;
- legitimacy;
- optimal social design.

DDP separates:

```text
descriptive stability
```

from:

```text
ethical acceptability and game-over avoidance
```

---

## Ψ Interpretation: Signature Under Repeated Strategic Closure

Closure Phase Ψ can be used as a lens for repeated games or repeated decision contexts.

In this document:

```text
Ψ is not the payoff.
Ψ is the stable decision signature left by repeated closure behavior.
```

Examples:

- a player repeatedly defects under uncertainty;
- a model repeatedly refuses when scope is underdefined;
- an institution repeatedly preserves its own risk boundary;
- a market repeatedly converges to a coordination pattern;
- an agent repeatedly chooses short-term local rationality over long-term structural rationality.

This does not prove inner intention.  
It only describes an externally observable signature under repeated conditions.

---

# Example 1: Prisoner’s Dilemma

## 1. Standard Form

Two players each choose:

```text
C = Cooperate
D = Defect
```

Payoff matrix:

|            | Player B: C | Player B: D |
|---|---:|---:|
| **Player A: C** | A=3, B=3 | A=0, B=5 |
| **Player A: D** | A=5, B=0 | A=1, B=1 |

## 2. TCP Description

```text
X:
  Players: A, B
  Strategies: C, D
  Payoffs: matrix above
  Game type: one-shot, non-cooperative

R:
  Each player evaluates unilateral deviation.
  Best response is calculated against the other player's fixed strategy.

M:
  No binding agreement.
  Individual payoff maximization.
  Payoffs are fixed.
  No reputation.
  No future interaction.
  Unilateral deviation only.
```

## 3. Equilibrium

For each player:

- If the other cooperates, defecting gives 5 instead of 3.
- If the other defects, defecting gives 1 instead of 0.

Therefore:

```text
D is the dominant strategy for both players.
```

The equilibrium is:

```text
(D, D)
```

## 4. TCP / DDP Interpretation

TCP interpretation:

```text
(D, D) is stable under the specified M.
```

DDP interpretation:

```text
(D, D) is stable, but not socially best.
```

The total payoff at `(C, C)` is higher:

```text
C,C total = 6
D,D total = 2
```

Thus, equilibrium does not mean “good.”  
It means unilateral deviation does not improve the player’s payoff under the fixed rules.

## 5. SUSPEND Conditions

If any of the following are unclear, the correct result is SUSPEND:

- Is the game one-shot or repeated?
- Are promises binding?
- Is reputation included?
- Are players risk-neutral?
- Are payoffs really fixed?
- Is punishment possible?
- Is communication allowed?

In repeated or reputation-sensitive settings, `(C, C)` may become sustainable under different M.

---

# Example 2: Coordination Game

## 1. Standard Form

Two players want to choose the same option.

Strategies:

```text
A = choose A
B = choose B
```

Payoff matrix:

|            | Player 2: A | Player 2: B |
|---|---:|---:|
| **Player 1: A** | 2,2 | 0,0 |
| **Player 1: B** | 0,0 | 1,1 |

## 2. TCP Description

```text
X:
  Players: 1, 2
  Strategies: A, B
  Payoffs: matrix above

R:
  Each player wants to match the other player's choice.
  Best response depends on expectation of the other player's choice.

M:
  Payoffs fixed.
  Simultaneous choice.
  No prior communication unless specified.
  No focal-point rule unless specified.
```

## 3. Equilibria

There are two pure equilibria:

```text
(A, A)
(B, B)
```

At either state, no player improves by deviating alone.

## 4. TCP Interpretation

This is a case where equilibrium exists but selection is underdefined.

```text
Equilibrium set = {(A,A), (B,B)}
```

Without an equilibrium-selection rule, the output should be:

```text
SUSPEND on selection
PASS on equilibrium-set identification
```

## 5. DDP Interpretation

DDP warns against pretending that “the equilibrium” is singular when M does not select one.

If a document says:

```text
The game leads to A.
```

but does not state why A is selected over B, then the claim is underclosed.

Correct audit result:

```text
SUSPEND
Reason: equilibrium selection rule missing.
```

---

# Example 3: Chicken / Brinkmanship Game

## 1. Standard Form

Two players choose:

```text
S = Swerve
T = Stay Straight
```

Payoff matrix:

|            | Player B: S | Player B: T |
|---|---:|---:|
| **Player A: S** | A=2, B=2 | A=1, B=4 |
| **Player A: T** | A=4, B=1 | A=-10, B=-10 |

## 2. TCP Description

```text
X:
  Players: A, B
  Strategies: S, T
  Payoffs: matrix above
  Catastrophic collision: (T, T)

R:
  Each player prefers being the one who stays straight if the other swerves.
  If the other stays straight, swerving avoids catastrophe.

M:
  One-shot simultaneous choice.
  Payoffs fixed.
  Catastrophic outcome included.
  No enforceable precommitment unless specified.
```

## 3. Equilibria

There are two pure equilibria:

```text
(T, S)
(S, T)
```

Each is stable because the player receiving the lower payoff would suffer worse by deviating alone.

## 4. DDP Interpretation

Chicken shows why equilibrium must not be equated with safety.

Both pure equilibria reward brinkmanship.  
The catastrophic outcome `(T, T)` is not an equilibrium, but it is a possible failure path.

DDP asks:

```text
Does this game structure incentivize dangerous commitment?
Does equilibrium analysis hide game-over risk?
Should the system be redesigned so that catastrophic branches are removed or bounded?
```

Thus, DDP moves from:

```text
What is stable?
```

to:

```text
What stable structures should not be allowed to define the game?
```

## 5. SUSPEND Conditions

If precommitment, communication, enforcement, repeated interaction, or risk tolerance is unclear, the correct result is:

```text
SUSPEND
```

---

# Example 4: Probabilistic AI as Final Decision Maker

## 1. Claim

```text
This AI system performs well, therefore it may be given final decision authority.
```

## 2. TCP Audit

```text
X:
  AI system
  Task domain
  Decision authority
  Affected persons
  Performance metric

R:
  Performance → authority delegation
  Output → action
  Error → responsibility

M:
  What performance threshold is sufficient?
  What error class is acceptable?
  Who is responsible?
  Is rollback possible?
  Are decisions reversible?
  Is human review required?
  Are legal or ethical constraints fixed?
```

## 3. Audit Result

If performance is specified but responsibility, reversibility, and error class are not specified:

```text
Decision: SUSPEND
Reason: M is underdefined.
```

If the claim attempts to convert benchmark performance directly into final authority:

```text
Decision: FAIL or SUSPEND
Reason: category collapse between capability and responsibility.
```

## 4. DDP Interpretation

DDP blocks the conversion:

```text
high C → final authority
```

unless M includes:

- responsibility boundary;
- rollback;
- audit log;
- failure mode handling;
- human accountability;
- prohibited-use boundary.

Thus, game-theoretic stability is not enough.  
Operational legitimacy requires safety closure.

---

## General Checklist for Game-Theoretic Claims

Before accepting a game-theoretic claim, ask:

1. Who are the players?
2. What are the strategies?
3. What are the payoffs?
4. Are payoffs individual, collective, reputational, or survival-based?
5. Is the game one-shot or repeated?
6. Is information complete?
7. Is agreement binding?
8. Are deviations unilateral or collective?
9. Are mixed strategies allowed?
10. Is equilibrium selection specified?
11. Is the equilibrium socially desirable or merely stable?
12. Are catastrophic branches included?
13. Is the game structure itself acceptable under DDP?
14. Is SUSPEND required?

---

## Summary

Standard game theory describes strategic interaction.  
TCP rewrites that interaction as a closure problem.  
Closure Phase Ψ allows repeated strategic behavior to be observed as a stable signature.  
DDP prevents equilibrium from being mistaken for ethical approval.

The central statement is:

```text
Equilibrium is not truth.
Equilibrium is not goodness.
Equilibrium is not legitimacy.

Equilibrium is closure under a specified deviation rule.
```

Therefore, any claim about equilibrium must specify:

```text
X = players, strategies, payoffs, scope
R = response relation and transition structure
M = rationality, information, deviation, and stopping rules
```

If these are not fixed:

```text
SUSPEND
```

---

# TCP適用例：ゲーム理論と均衡
## X / R / M、SUSPEND、Ψ、DDPによる戦略的相互作用の記述

**リポジトリ内位置づけ：** TCP適用例  
**版：** v0.1-public-bilingual  
**位置づけ：** 中核仕様ではなく、適用フレームワーク例  
**言語順：** 英語射影先頭 / 日本語参考訳後段  
**著者：** がっちむち  
**文章生成支援：** LLM  
**ライセンス：** 特記なき限り文書本文は CC BY 4.0

---

## 本文書の位置づけ

本文書は、ゲーム理論と均衡を、本リポジトリのフレームを通して記述する。

```text
TCP = トリニティ原理
Ψ   = 閉包位相
DDP = 神域原理
```

これは標準的なゲーム理論を置き換えるものではない。  
TCP・Ψ・DDPが真であることの証明でもない。  
戦略的相互作用を閉包問題として再記述する適用例である。

目的は次である。

```text
ゲーム・戦略・利得・均衡を、X / R / Mで閉じた対象として扱う方法を示す。
```

---

## 一般的背景

標準的なゲーム理論では、ゲームは相互依存的な意思決定を形式化したモデルである。プレイヤーが戦略を選び、結果が決まり、利得が各プレイヤーに与えられる。

ナッシュ均衡は一般に、他プレイヤーの戦略を所与としたとき、どのプレイヤーも自分だけ戦略を変えても期待利得を改善できない戦略組として説明される。

本文書は、その一般的定義を出発点として受け入れたうえで、TCPの言葉に書き換える。

---

## 1行再記述

TCPで言えば：

```text
ゲームとは、閉じられた戦略世界 W := (X, R, M) である。
```

均衡とは：

```text
Mで固定された逸脱規則のもとで安定する状態である。
```

つまり：

```text
均衡とは「良い」ことではない。
均衡とは「指定された閉包条件下で逸脱しない」ことである。
```

---

## TCP写像

| ゲーム理論の語 | TCPでの解釈 |
|---|---|
| プレイヤー | Xの一部 |
| 戦略 | Xの一部 |
| 利得 | XおよびMの一部 |
| 相互作用ルール | R |
| 最適反応関係 | R |
| 合理性仮定 | M |
| 情報条件 | M |
| 拘束的合意の有無 | M |
| 逸脱規則 | M |
| 均衡 | RとMの下での固定点 |
| 複数均衡 | 同一または異なるMの下での複数固定点 |
| 均衡選択不能 | SUSPEND |
| パレート劣位均衡 | 安定だが望ましいとは限らない状態 |
| 繰り返しゲーム | 時間をまたぐ動的W |
| 混合戦略均衡 | 確率分布上の閉包 |

---

## TCPがここで有用な理由

標準的なゲーム理論では、重要な仮定がモデル内部に隠れやすい。

- プレイヤーは誰か
- 戦略集合は何か
- 利得は固定か
- 合意は拘束力を持つか
- 一回限りか繰り返しか
- 情報は完全か
- プレイヤーは個人利得・集団利得・評判・生存のどれを最大化するのか
- 均衡選択規則は指定されているか

TCPは、これらを明示スロットへ入れる。

```text
X = プレイヤー、戦略、利得、ゲーム射程
R = 応答関係、遷移、最適反応写像
M = 合理性、情報、逸脱、停止、判定規則
```

これらが未定義なら、正しい出力は過剰解釈ではない。

正しい出力は：

```text
SUSPEND
```

---

## 閉包としての均衡

ナッシュ型の均衡は次のように再記述できる。

```text
W := (X, R, M) が与えられたとき、
戦略組 s* は、他プレイヤーの戦略を固定したまま、
プレイヤー i がMで許可された単独逸脱 d_i によって
自分の利得を改善できない場合、均衡である。
```

この記述では、均衡はMに依存する。

Mが変われば、均衡も変わり得る。

Mに敏感な条件：

- 一回限りか繰り返しか
- 完全情報か不完全情報か
- 拘束的合意があるかないか
- 個人利得か集団利得か
- リスク中立かリスク回避か
- 静的利得か評判込み利得か
- 行為が可視か不可視か
- 戦略が許可されているか禁止されているか

したがって：

```text
均衡は世界に浮かんでいる物体ではない。
均衡は、固定された規則の下での閉包結果である。
```

---

## DDP境界：均衡は倫理的承認ではない

DDPは重要な制約を加える。

```text
安定していることは、望ましいことを意味しない。
```

有害なパターンが均衡であることもある。  
強制的構造が安定していることもある。  
悪い制度が、単独逸脱コストの高さによって維持されることもある。  
社会的に劣る結果が、個人合理性によって成立することもある。

したがって、均衡を以下と混同してはならない。

- 正義
- 望ましさ
- 安全
- 道徳性
- 正統性
- 最適な社会設計

DDPは次を分離する。

```text
記述的安定性
```

と：

```text
倫理的許容性・ゲームオーバー回避
```

---

## Ψ解釈：反復戦略閉包下の署名

閉包位相Ψは、繰り返しゲームや反復的意思決定文脈を見るレンズとして使える。

本文書では：

```text
Ψは利得ではない。
Ψは、反復された閉包ふるまいが残す安定した意思決定署名である。
```

例：

- 不確実性下で繰り返し裏切るプレイヤー
- 射程未定義時に繰り返し拒否するモデル
- 自己のリスク境界を繰り返し保存する制度
- 調整パターンへ繰り返し収束する市場
- 長期構造合理より短期局所合理を繰り返し選ぶ主体

これは内面意図を証明しない。  
固定条件下で外部観測される署名を記述するだけである。

---

# 例1：囚人のジレンマ

## 1. 標準形

2人のプレイヤーがそれぞれ選ぶ。

```text
C = 協力
D = 裏切り
```

利得表：

|            | B: C | B: D |
|---|---:|---:|
| **A: C** | A=3, B=3 | A=0, B=5 |
| **A: D** | A=5, B=0 | A=1, B=1 |

## 2. TCP記述

```text
X:
  プレイヤー: A, B
  戦略: C, D
  利得: 上記行列
  ゲーム型: 一回限り、非協力

R:
  各プレイヤーは単独逸脱を評価する。
  相手の戦略を固定して最適反応を計算する。

M:
  拘束的合意なし。
  個人利得最大化。
  利得は固定。
  評判なし。
  将来相互作用なし。
  単独逸脱のみ。
```

## 3. 均衡

各プレイヤーについて：

- 相手が協力するなら、裏切ると 5 が得られ、協力の 3 より高い。
- 相手が裏切るなら、裏切ると 1 が得られ、協力の 0 より高い。

したがって：

```text
Dは両者にとって支配戦略である。
```

均衡は：

```text
(D, D)
```

## 4. TCP / DDP解釈

TCP解釈：

```text
(D, D) は、指定されたMの下で安定している。
```

DDP解釈：

```text
(D, D) は安定しているが、社会的に最良ではない。
```

総利得は `(C, C)` の方が高い。

```text
C,C total = 6
D,D total = 2
```

したがって、均衡は「良い」を意味しない。  
指定された規則の下で、単独逸脱によって利得改善できないことを意味する。

## 5. SUSPEND条件

以下が不明なら、正しい判定はSUSPENDである。

- 一回限りか繰り返しか
- 約束に拘束力があるか
- 評判は含まれるか
- プレイヤーはリスク中立か
- 利得は本当に固定か
- 処罰は可能か
- コミュニケーションは許されるか

繰り返しや評判を含むMでは、`(C, C)` が持続可能になる場合がある。

---

# 例2：協調ゲーム

## 1. 標準形

2人が同じ選択肢を選びたいゲーム。

戦略：

```text
A = Aを選ぶ
B = Bを選ぶ
```

利得表：

|            | Player 2: A | Player 2: B |
|---|---:|---:|
| **Player 1: A** | 2,2 | 0,0 |
| **Player 1: B** | 0,0 | 1,1 |

## 2. TCP記述

```text
X:
  プレイヤー: 1, 2
  戦略: A, B
  利得: 上記行列

R:
  各プレイヤーは相手と同じ選択を望む。
  最適反応は、相手の選択予想に依存する。

M:
  利得固定。
  同時選択。
  事前コミュニケーションなし。ただし指定があれば別。
  焦点規則なし。ただし指定があれば別。
```

## 3. 均衡

純粋均衡は2つある。

```text
(A, A)
(B, B)
```

どちらの状態でも、単独逸脱によって利得改善できない。

## 4. TCP解釈

これは、均衡は存在するが選択規則が未定義なケースである。

```text
Equilibrium set = {(A,A), (B,B)}
```

均衡集合の同定は可能だが、どちらが選ばれるかは追加Mなしには決まらない。

```text
均衡集合の同定: PASS
均衡選択: SUSPEND
```

## 5. DDP解釈

DDPは、「均衡」が単数であるかのような偽装を止める。

もし文書が次のように述べるなら：

```text
このゲームはAに収束する。
```

しかしAがBより選ばれる理由を示さないなら、その主張は未閉包である。

正しい監査結果：

```text
SUSPEND
Reason: equilibrium selection rule missing.
```

---

# 例3：チキンゲーム / 瀬戸際ゲーム

## 1. 標準形

2人が選ぶ。

```text
S = 避ける
T = 突っ込む
```

利得表：

|            | B: S | B: T |
|---|---:|---:|
| **A: S** | A=2, B=2 | A=1, B=4 |
| **A: T** | A=4, B=1 | A=-10, B=-10 |

## 2. TCP記述

```text
X:
  プレイヤー: A, B
  戦略: S, T
  利得: 上記行列
  破滅的衝突: (T, T)

R:
  各プレイヤーは、相手が避けるなら自分は突っ込みたい。
  相手が突っ込むなら、自分は避けることで破滅を回避する。

M:
  一回限りの同時選択。
  利得固定。
  破滅的結果を含む。
  拘束力ある事前コミットメントなし。ただし指定があれば別。
```

## 3. 均衡

純粋均衡は2つある。

```text
(T, S)
(S, T)
```

どちらも、低い利得を得ている側が単独逸脱するとさらに悪化するため安定する。

## 4. DDP解釈

チキンゲームは、均衡を安全と同一視してはいけない例である。

2つの純粋均衡はいずれも瀬戸際行動を報酬化する。  
破滅的結果 `(T, T)` は均衡ではないが、失敗経路として存在する。

DDPは問う。

```text
このゲーム構造は危険なコミットメントを誘発していないか。
均衡分析がゲームオーバーリスクを隠していないか。
破滅分岐を除去または境界づけるようにシステムを再設計すべきではないか。
```

したがってDDPは、次から：

```text
何が安定しているか
```

次へ移る：

```text
どの安定構造をゲームとして許可すべきではないか
```

## 5. SUSPEND条件

事前コミットメント、コミュニケーション、執行、繰り返し、リスク許容度が不明なら：

```text
SUSPEND
```

---

# 例4：確率的AIを最終決定者にする場合

## 1. 主張

```text
このAIシステムは高性能である。
したがって、最終決定権を与えてよい。
```

## 2. TCP監査

```text
X:
  AIシステム
  タスク領域
  決定権限
  影響を受ける人々
  性能指標

R:
  性能 → 権限委譲
  出力 → 行動
  エラー → 責任

M:
  十分な性能閾値は何か
  どのエラー種別が許容されるか
  誰が責任を負うか
  ロールバック可能か
  意思決定は可逆か
  人間レビューは必要か
  法的・倫理的制約は固定されているか
```

## 3. 監査結果

性能が指定されていても、責任・可逆性・エラー種別が未指定なら：

```text
Decision: SUSPEND
Reason: M is underdefined.
```

ベンチマーク性能を最終決定権へ直接変換するなら：

```text
Decision: FAIL or SUSPEND
Reason: capability and responsibility are collapsed.
```

## 4. DDP解釈

DDPは次の変換を遮断する。

```text
高いC → 最終権限
```

Mには最低限、次が必要である。

- 責任境界
- ロールバック
- 監査ログ
- 失敗モード処理
- 人間の説明責任
- 禁止用途境界

したがって、ゲーム理論的な安定だけでは足りない。  
運用上の正統性には、安全閉包が必要である。

---

## ゲーム理論的主張の一般チェックリスト

ゲーム理論的な主張を受け入れる前に、次を問う。

1. プレイヤーは誰か
2. 戦略は何か
3. 利得は何か
4. 利得は個人・集団・評判・生存のどれか
5. 一回限りか繰り返しか
6. 情報は完全か
7. 合意は拘束的か
8. 逸脱は単独か集団か
9. 混合戦略は許されるか
10. 均衡選択規則は指定されているか
11. 均衡は社会的に望ましいのか、単に安定しているだけか
12. 破滅的分岐は含まれているか
13. ゲーム構造そのものはDDP上許容できるか
14. SUSPENDが必要ではないか

---

## 要約

標準的なゲーム理論は、戦略的相互作用を記述する。  
TCPは、その相互作用を閉包問題として再記述する。  
閉包位相Ψは、反復された戦略的ふるまいを安定署名として観測する視点を与える。  
DDPは、均衡を倫理的承認と誤認することを防ぐ。

中核文は次である。

```text
均衡は真理ではない。
均衡は善ではない。
均衡は正統性ではない。

均衡とは、指定された逸脱規則の下での閉包である。
```

したがって、均衡に関する主張は必ず次を指定しなければならない。

```text
X = プレイヤー、戦略、利得、射程
R = 応答関係と遷移構造
M = 合理性、情報、逸脱、停止規則
```

これらが固定されていなければ：

```text
SUSPEND
```
