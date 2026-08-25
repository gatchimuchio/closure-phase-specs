[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19729938.svg)](https://doi.org/10.5281/zenodo.19729938)

# closure-phase-specs
## 認知工学体系・公開原典アーカイブ

本リポジトリは、がっちむち♂による**認知工学体系**の公開可能な原典・翻訳・境界宣言・公開適用論文を管理するリポジトリである。

基底言語・規定言語は**日本語**である。

```text
日本語原典を先に成立
→ 日本語で監査・改訂
→ 実務上必要な場合のみ英語等へ翻訳
```

英語その他の言語は日本語原典の後段翻訳であり、独立した正本ではない。

---

# 現行正本

root に置く番号付き文書は、現在の公開正本だけである。

## 基底・中核文書

| 順 | 文書 | 役割 |
|---|---|---|
| 00 | `00_認知工学とは何か_v0_2_ja_en.md` | 認知工学の定義、Science / Engineering の分別、全学問の基底工学としての位置づけ |
| 01 | `01_情報工学における言語基底論_v0_2_ja_en.md` | 世界→認知→情報、情報科学批判、情報工学と言語、日本語基底規定 |
| 02 | `02_Umami_Gap_v0_9_ja_en.md` | intelligence の語彙圧縮と欠落変数問題への導入 |
| 03 | `03_トリニティ原理_v0_9_ja_en.md` | X / R / M による認知後記述の三項閉包と SUSPEND |
| 04 | `04_閉包位相Ψ_v0_8_ja_en.md` | 能力・感情・人格価値から分離した閉包位相Ψの操作的定義 |
| 05 | `05_神の領域原理（仮）_v0_9_ja_en.md` | 認知後世界像を世界本体へ誤投影しない最上位境界原理 |

## 現行公開適用論文

| 順 | 文書 | 役割 |
|---|---|---|
| 06 | `06_トリニティ原理適用_論証監査_v0_2_ja_en.md` | 自然言語の論証を、座標・関係・前提・判定・停止から監査する公開適用例 |
| 07 | `07_トリニティ原理適用_ゲーム理論と均衡_v0_3_ja_en.md` | ゲーム理論の解を固定前提内の条件付き解として再記述する公開適用例 |

推奨読書順は **00 → 05** を基礎とし、その後、必要に応じて **06 → 07** の適用論文へ進む。

---

# 体系の最小関係

```text
認知工学
  ↓
認知による対象化・関係化・判断・再認知
  ↓
情報の成立
  ↓
情報工学
  ↓
言語基底
  ↓
日本語原典先行

旨味ギャップ
  = 欠落変数を見えなくする語彙圧縮の導入

トリニティ原理
  = 認知後記述を X / R / M で閉じる方法論
  = 未閉包では SUSPEND
  = 三項そのものも最終世界構造へ固定しない

閉包位相Ψ
  = 閉包的作用が外部へ残す安定出力相
  = 内面本質や人格価値ではない

神の領域原理（仮）
  = 認知後世界像を認知以前の世界本体へ誤投影しない境界
  = 原理自身も暫定Projectionとして自己適用する

公開適用論文
  = 上記原理を限定された対象へ射影した実例
  = 適用論文自体を唯一・最終の形式へ固定しない
```

---

# 現行名称

正式名称・表記は `PUBLICATION_POLICY.md` を正とする。

- **神の領域原理（仮）**
  - 略称：**神域原理（仮）**
- **トリニティ原理**
- **閉包位相Ψ**
- **Human Decision-making System（仮）**
  - 和名：**人間意思決定理論（仮）**
  - 略称：**HDS**

`（仮）` を付すのは、神の領域原理（仮）／神域原理（仮）と HDS のみである。

---

# HDS公開境界

HDSについて本リポジトリで公開する情報は、原則として名称のみである。

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

HDSの内部構造、相、層、判断機構、評価設計、運用手順、実装、再現可能なレシピ等は現行公開範囲に含めない。

旧版に存在するHDS詳細記述は `archive/` 内の歴史資料であり、現行公開仕様ではない。

---

# 版履歴と archive

`archive/` は旧版・旧適用例・旧ツールを保存する履歴領域である。

archive 内の文書には、次のような現行方針と異なる記述が残り得る。

- 英語先行レイアウト
- 旧名称
- 神の領域原理（仮）の `（仮）` 欠落
- 旧HDS公開記述
- 過去の読書順
- 過去のTCP固定表現
- 現行版へ改訂済みの旧適用論文

これらは削除・改竄せず履歴として保存するが、**現行正本として参照してはならない**。

旧適用論文の現行対応先：

```text
archive/legacy/applications/TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md
  → 06_トリニティ原理適用_論証監査_v0_2_ja_en.md

archive/legacy/applications/TCP_APPLICATION_GAME_THEORY_EQUILIBRIUM.md
  → 07_トリニティ原理適用_ゲーム理論と均衡_v0_3_ja_en.md
```

---

# 公開・言語ポリシー

詳細は `PUBLICATION_POLICY.md` を参照。

原則：

1. 日本語を基底言語・規定言語とする。
2. 日本語原典を先に成立させる。
3. 翻訳は後段の射影とする。
4. 翻訳で欠陥が見つかった場合、日本語原典を先に直す。
5. HDSは名称のみ公開する。
6. 旧版と現行正本を混在させない。
7. 適用Projectionを普遍的・最終的な形式へ昇格させない。

---

# 参照文献

`REFERENCES.md` は座標合わせ用の参考情報であり、本理論群の正しさを権威によって証明するものではない。

---

# License

文書本文は、特記がない限り `LICENSE` に従う。

---

# English Translation

## closure-phase-specs — Public Originals Archive for a Cognitive Engineering System

This repository manages the publicly disclosed originals, translations, boundary declarations, and public application papers of a Cognitive Engineering theoretical system authored by **がっちむち♂**.

Japanese is the base and normative language.

```text
Establish Japanese original first
→ Audit and revise in Japanese
→ Translate only when practically necessary
```

Other-language versions are later translations, not independent originals.

### Current canonical reading order

Core documents:

1. `00_認知工学とは何か_v0_2_ja_en.md`
2. `01_情報工学における言語基底論_v0_2_ja_en.md`
3. `02_Umami_Gap_v0_9_ja_en.md`
4. `03_トリニティ原理_v0_9_ja_en.md`
5. `04_閉包位相Ψ_v0_8_ja_en.md`
6. `05_神の領域原理（仮）_v0_9_ja_en.md`

Current public applications:

7. `06_トリニティ原理適用_論証監査_v0_2_ja_en.md`
8. `07_トリニティ原理適用_ゲーム理論と均衡_v0_3_ja_en.md`

The repository root contains only current public canonical documents. Superseded versions, old applications, and old tools are stored under `archive/` and do not define current specifications.

### HDS disclosure boundary

Only these names are public:

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

No internal HDS structure or reproducible operational detail is part of the current public scope.
