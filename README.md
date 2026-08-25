[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19729938.svg)](https://doi.org/10.5281/zenodo.19729938)

# closure-phase-specs

## 認知工学体系・公開仕様アーカイブ

本リポジトリは、**認知工学**を基底に、情報工学・言語基底、トリニティ原理、閉包位相Ψ、神の領域原理（仮）、および関連する公開適用例を収録する公開仕様アーカイブである。

本リポジトリは査読済み論文集ではない。形而上学的真理の宣言でもない。各文書は、対象・目的・射程に応じて、定義、境界、停止、観測、工学的構成、再監査可能性を記述する。

---

## 1. 現行言語方針

**日本語を基底言語・規定言語とする。**

原典は必ず日本語で先に成立させる。

```text
日本語で思考・生成
→ 日本語で定義・構造化
→ 日本語で監査
→ 日本語原典成立
→ 実務上必要な場合のみ他言語へ翻訳
→ 日本語原典との差分監査
```

英語その他の言語は、国際公開、規格、API、共同作業その他、実務上やむを得ない場合に使用する。

多言語版は日本語原典から生成された翻訳・射影であり、独立した正本ではない。意味が衝突する場合は日本語原典を優先する。

詳細は [`PUBLICATION_POLICY.md`](PUBLICATION_POLICY.md) を参照。

---

## 2. 最初に読む2本

本リポジトリの現在の入口は次の二本である。

### 1. 認知工学とは何か

[`00_認知工学とは何か_v0_1_ja_en.md`](00_認知工学とは何か_v0_1_ja_en.md)

認知工学を、HCIやHuman Factorsの別名ではなく、**あらゆる学問が成立する前段の認知操作を工学対象として扱う基底工学**として再定義する。

主な論点：

- Science / Engineering の分別
- 認知科学の成立条件批判
- 認知＝センシング／前処理系
- メタ認知＝制御／監査系
- 既存認知工学のラベル崩壊批判
- 「認知工学はあらゆる学問の祖」という構造的位置づけ

### 2. 情報工学における言語基底論

[`01_情報工学における言語基底論_v0_1_ja_en.md`](01_情報工学における言語基底論_v0_1_ja_en.md)

**世界 → 認知 → 情報**という順序から情報の成立を捉え直し、「情報科学」を独立したScienceとして採用せず、情報の保存・伝達・変換・検索・計算・再利用を**情報工学**として位置づける。

その上で、情報工学上の基底表現として言語を比較し、本理論群における**日本語基底**を規定する。

---

## 3. 推奨読書順

現在の推奨順は次のとおり。

```text
1. 00_認知工学とは何か_v0_1_ja_en.md
2. 01_情報工学における言語基底論_v0_1_ja_en.md
3. 00_Umami_Gap_v0_8_bilingual.md
4. 02_TCP_v0_8_bilingual.md
5. 01_Closure_Phase_Psi_v0_7_bilingual.md
6. 03_神の領域原理_v0_8_bilingual.md
7. TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md
8. TCP_APPLICATION_GAME_THEORY_EQUILIBRIUM.md
9. REFERENCES.md
10. ENGINEERING_POSTURE_REFERENCES.md
```

旧v0.7/v0.8文書の番号は、当時の公開順序を示す**版履歴**として維持している。現在の読書順は本READMEを正とする。

---

## 4. 理論群の位置関係

```text
認知工学
  ↓
認知による対象化・差異化・関係化・判断・再認知
  ↓
情報の成立
  ↓
情報工学
  ↓
言語基底
  ↓
日本語原典運用

認知工学体系の公開原理・定義
  ├─ トリニティ原理
  ├─ 閉包位相Ψ
  └─ 神の領域原理（仮）

Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
  = 名称のみ公開
```

---

## 5. 現行名称

- **神の領域原理（仮）**
  - 略称：**神域原理（仮）**
- **トリニティ原理**
- **閉包位相Ψ**
- **Human Decision-making System（仮）**
  - 和名：**人間意思決定理論（仮）**
  - 略称：**HDS**

`（仮）` を付すのは、神の領域原理（仮）／神域原理（仮）とHDSのみとする。

---

## 6. HDS公開境界

HDSについて本リポジトリが現行公開する情報は、原則として名称のみである。

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

内部構造、運用方法、評価設計、判断機構、実装、再現可能なレシピその他は現行公開範囲に含めない。

過去版文書にHDSの役割・構造・実装境界等の記述が残る場合、それらは当該版作成時点の履歴であり、現行HDSの公開仕様を意味しない。

---

## 7. 主要既存文書

| 文書 | 現在の役割 |
|---|---|
| `00_Umami_Gap_v0_8_bilingual.md` | C / Ψ / E等の概念圧縮・変数欠落問題への導入 |
| `02_TCP_v0_8_bilingual.md` | X / R / Mによる閉包とSUSPENDを扱うトリニティ原理の既存公開版 |
| `01_Closure_Phase_Psi_v0_7_bilingual.md` | 閉包位相Ψの既存公開定義 |
| `03_神の領域原理_v0_8_bilingual.md` | 認知後世界像を世界本体へ誤投影しない上位境界の既存公開版 |
| `TCP_APPLICATION_ARGUMENT_AUDIT_FRAMEWORK.md` | トリニティ原理の自然言語議論監査への公開適用例 |
| `TCP_APPLICATION_GAME_THEORY_EQUILIBRIUM.md` | ゲーム理論・均衡概念への公開適用例 |

既存v0.7/v0.8文書には、現行方針以前の**英語先行バイリンガル構成**が残っている。これらは版履歴として保持し、次回改訂版から「日本語原典 → 英語翻訳」へ統一する。

---

## 8. 神の領域原理（仮）の中核

神の領域原理（仮）は、世界を完全に説明する理論ではなく、認知による世界形成を世界本体へ誤投影しないための上位境界原理として扱う。

現在の最小表現：

```text
認知後に成立した世界像を、認知以前の世界本体として断定してはならない。
```

機能：

```text
どこで断定を止めるべきかという境界を示す。
```

---

## 9. トリニティ原理

既存公開版では、認知後世界記述の閉包を次で扱う。

```text
W := (X, R, M)
```

- `X`：対象
- `R`：関係
- `M`：同一性・境界・判断・停止等を閉じる機能

未閉包・未観測・境界到達時に、強制的な断定ではなく `SUSPEND` を許可する。

なお、この三項記述自体を世界本体の最終形式として扱わない。認知後の有力な記述形式として再監査可能な状態を維持する。

---

## 10. 閉包位相Ψ

閉包位相Ψは、固定条件下で反復観測されたときに、閉包的な作用から外部へ残る安定した出力相を扱うための操作的概念である。

能力、感情、人格価値、内面本質等を一語へ混線させないための分別として使用する。

---

## 11. 公開利用境界

本リポジトリの文書を、以下へ直接接続しない。

- 人間の価値・人格の序列化
- 不可逆な支配・操作・統治
- 権威の盾としての利用
- 感情の完全構造化
- 自我の作為的設計
- 人間意思決定の完全な支配・予測・操作
- 認知後のモデルを世界本体として断定すること

公開境界の詳細は各文書および `PUBLICATION_POLICY.md` に従う。

---

## 12. 参考文献の位置づけ

`REFERENCES.md` および `ENGINEERING_POSTURE_REFERENCES.md` は、既存分野との座標合わせ・用語確認・工学姿勢の参照用である。

これらを本理論群の権威的証明として使用しない。

---

## 13. ライセンス

文書本文は、個別記載がない限り既存ライセンス方針に従う。

コードを含む場合は、各コードファイルまたはディレクトリのライセンスを優先する。

---

# English Translation

## Cognitive Engineering Public Specification Archive

This repository is organized as a public specification archive for a **Cognitive Engineering** theoretical system, including Information Engineering and language-base theory, the Trinity Principle, Closure Phase Ψ, 神の領域原理（仮）, and selected public applications.

The Japanese text above is authoritative. This English section is a translation for external readability.

### Language policy

Japanese is the base and normative language. Originals are established in Japanese first. Other languages are produced only when practically necessary and are treated as translations/projections from the Japanese original.

See [`PUBLICATION_POLICY.md`](PUBLICATION_POLICY.md).

### First two documents

1. [`00_認知工学とは何か_v0_1_ja_en.md`](00_認知工学とは何か_v0_1_ja_en.md) — redefines Cognitive Engineering as the foundational engineering layer upstream of academic disciplines.
2. [`01_情報工学における言語基底論_v0_1_ja_en.md`](01_情報工学における言語基底論_v0_1_ja_en.md) — derives Information Engineering from the relation `World → Cognition → Information`, rejects Information Science as the governing category, and specifies Japanese as the base language for this theoretical system.

### Current reading order

```text
1. Cognitive Engineering foundation
2. Language-base theory in Information Engineering
3. Umami Gap
4. Trinity Principle
5. Closure Phase Ψ
6. 神の領域原理（仮）
7. Public applications
8. Orientation references
```

### Current names

- **神の領域原理（仮）** / short name **神域原理（仮）**
- **Trinity Principle / トリニティ原理**
- **Closure Phase Ψ / 閉包位相Ψ**
- **Human Decision-making System（仮） / 人間意思決定理論（仮） / HDS**

Public disclosure of HDS is limited, in principle, to these names. Older HDS-adjacent descriptions remain only as version history and do not define the current public HDS specification.

### Existing bilingual versions

Existing v0.7/v0.8 documents predate the current Japanese-first policy and retain an English-first layout. They are preserved as versioned history. All new documents and future revisions use:

```text
Part I. Japanese Original
Part II. English Translation
```

### Repository stance

The repository does not present its models as direct access to a pre-cognitive world-itself, does not use its frameworks for superiority ranking or irreversible manipulation, and preserves stopping/reopening where claims remain underdefined or cross a cognition boundary.
