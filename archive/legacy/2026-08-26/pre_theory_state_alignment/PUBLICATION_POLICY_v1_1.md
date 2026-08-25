# 公開・言語・命名ポリシー
## Publication / Language / Naming Policy

**版**：v1.1  
**著者**：がっちむち♂  
**規定言語**：日本語  

本書は `closure-phase-specs` における現行公開方針を規定する。

---

# 1. 日本語を基底・規定言語とする

本理論群では、日本語を唯一の基底言語・規定言語とする。

原則となる生成順序は次である。

```text
日本語で理論生成
→ 日本語で定義・構造化
→ 日本語で監査・改訂
→ 日本語原典成立
→ 実務上必要な場合のみ多言語へ翻訳
```

多言語版は日本語原典から生成された翻訳・射影であり、独立した正本ではない。

意味が衝突した場合、日本語原典を優先する。

翻訳時に未定義・矛盾・関係欠落・説明不足が見つかった場合、翻訳側で勝手に補完せず、日本語原典を先に再監査・改訂する。

---

# 2. 多言語使用条件

英語その他の言語は、国際公開、外部規格、API、応募、共同作業その他、実務上必要な場合に限って使用する。

「国際公開するから最初から英語で原典を作る」という順序は採用しない。

---

# 3. 正式名称

現行の名称は次の通りとする。

## 3.1 神の領域原理（仮）

```text
正式名称：神の領域原理（仮）
略称：神域原理（仮）
```

英語環境でも日本語名を正式名として保持する。説明用の英訳は置換名ではない。

`（仮）` は、本原理自身を最終真理へ固定しない構造的な暫定性を示すため保持する。

## 3.2 トリニティ原理

```text
正式名称：トリニティ原理
英語説明：Trinity Principle
```

`（仮）` は付さない。

## 3.3 閉包位相Ψ

```text
正式名称：閉包位相Ψ
英語説明：Closure Phase Ψ
```

`（仮）` は付さない。

## 3.4 HDS

```text
正式名称：Human Decision-making System（仮）
和名：人間意思決定理論（仮）
略称：HDS
```

`（仮）` を保持する。

---

# 4. （仮）の適用範囲

本理論群で `（仮）` を名称に付すのは、原則として次の二系統のみである。

1. 神の領域原理（仮）／神域原理（仮）
2. Human Decision-making System（仮）／人間意思決定理論（仮）

その他の理論名には、個別の明示指示がない限り `（仮）` を付さない。

---

# 5. HDS公開境界

HDSについて現行公開範囲に含める情報は、原則として名称のみである。

公開可：

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

現行公開範囲外：

- 内部構造
- 相・層・ループ
- 判断機構
- 評価設計
- 運用手順
- 実装
- 再現可能なレシピ
- 内部パラメータ・閾値・検出器
- その他、名称を超えて内部作用を再構成できる情報

旧版にこれらの記述が存在する場合、その記述は歴史資料として `archive/` に保存し、現行仕様として扱わない。

---

# 6. root と archive の分離

リポジトリrootには現行公開正本だけを置く。

旧版、旧名称、旧読書順、旧適用例、旧ツールは `archive/` へ退避する。

```text
root    = current canonical public set
archive = historical / superseded set
```

archive 内の記述は、当時の状態を保持するため原則として無言修正しない。

ただし archive であることを明示し、現行正本との混同を防ぐ。

---

# 7. 版更新

理論の意味が変化する更新は版番号を上げる。

誤字脱字・リンク修正等の意味非変更修正でも、公開履歴上必要ならパッチ版または改訂履歴を残す。

現在の正本を過去版へ無言上書きしない。

---

# 8. 著者表記

公開文書の著者表記は、原則として次に統一する。

```text
がっちむち♂
```

英語翻訳部でも著者名を `Gacchimuchi` 等へ置換せず、`がっちむち♂` を保持する。

---

# 9. 参照文献の位置づけ

外部参考文献は、座標合わせ、既存用語、歴史的背景、工学上の隣接概念を確認するために利用する。

本理論群の正しさを権威によって証明するためのものではない。

---

# 10. 現行正本順

```text
00_認知工学とは何か_v0_2_ja_en.md
01_情報工学における言語基底論_v0_2_ja_en.md
02_Umami_Gap_v0_9_ja_en.md
03_トリニティ原理_v0_9_ja_en.md
04_閉包位相Ψ_v0_8_ja_en.md
05_神の領域原理（仮）_v0_9_ja_en.md
```

---

# English Translation

## Publication / Language / Naming Policy

Japanese is the sole base and normative language of this theoretical system.

The required order is:

```text
Generate in Japanese
→ Define and audit in Japanese
→ Establish Japanese original
→ Translate only when practically necessary
```

Translations are projections from the Japanese original, not independent originals.

Canonical names:

```text
神の領域原理（仮） / 神域原理（仮）
トリニティ原理 / Trinity Principle
閉包位相Ψ / Closure Phase Ψ
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

Only 神の領域原理（仮） and HDS carry `（仮）` as part of their current names.

For HDS, only the names are public. Internal structure, phases, loops, evaluation design, operation, implementation, reproducible recipes, thresholds, and equivalent reconstructive details are outside the current public scope.

The repository root contains only current canonical public documents. Superseded material is stored under `archive/`.

The public author name is `がっちむち♂` in all language sections.
