# 公開・言語・名称ポリシー

**版**：v1.0  
**著者**：がっちむち♂  
**基底言語**：日本語  

本ファイルは、本リポジトリにおける現行の公開・言語・名称方針を固定する。過去版文書に異なる運用記述が残る場合、本ポリシーを現行運用として優先する。

---

## 1. 日本語基底

本理論群の基底言語・規定言語は日本語とする。

運用順序は次である。

```text
日本語で思考・生成
→ 日本語で定義・構造化
→ 日本語で監査
→ 日本語原典成立
→ 実務上必要な場合のみ他言語へ翻訳
→ 日本語原典との差分監査
```

英語その他の言語は、国際公開、規格、API、共同作業その他、実務上やむを得ない場合にのみ使用する。

多言語版は日本語原典から生成された翻訳・射影であり、独立した正本ではない。意味が衝突する場合、日本語原典を優先する。

翻訳時に原典の欠陥が発見された場合、翻訳側で補完して閉じない。日本語原典を再監査・改訂した後、改訂版から再翻訳する。

---

## 2. 正式名称

現行名称は次のとおり。

- **神の領域原理（仮）**
  - 略称：**神域原理（仮）**
- **トリニティ原理**
- **閉包位相Ψ**
- **Human Decision-making System（仮）**
  - 和名：**人間意思決定理論（仮）**
  - 略称：**HDS**

`（仮）` を付すのは、神の領域原理（仮）／神域原理（仮）と HDS のみとする。

英語圏向けでも、日本語の正式名称を無理に置換名へ変えない。必要な英語は説明・翻訳として扱う。

---

## 3. HDS公開境界

HDSについて一般公開する情報は、原則として名称のみとする。

公開可能な名称：

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

本リポジトリでは、HDSの内部構造、運用手順、評価設計、判断機構、実装、再現可能なレシピその他の詳細を現行公開範囲に含めない。

過去版文書にHDSの役割・相・層・実装境界等に関する記述が残る場合、それらは当該版作成時点の履歴として扱い、現行HDSの公開仕様とはみなさない。

---

## 4. 既存バイリンガル版の扱い

2026-07-07以前に作成された既存バイリンガル文書には、英語を先に置くレイアウトが残っている。

これらは版履歴として保持する。

現行方針では、新規文書および次回改訂版から、必ず次の順序を採用する。

```text
Part I. 日本語原典
Part II. English Translation
```

---

## 5. 理論群の上位位置づけ

本リポジトリの理論群は、認知工学体系として整理する。

最初に読むべき基底文書は次の二本である。

1. `00_認知工学とは何か_v0_1_ja_en.md`
2. `01_情報工学における言語基底論_v0_1_ja_en.md`

その後、各公開原理・定義・適用例へ進む。

---

# English Translation

# Publication, Language, and Naming Policy

**Version**: v1.0  
**Author**: Gacchimuchi♂  
**Authoritative language**: Japanese  

This file defines the current publication, language, naming, and disclosure policy of the repository. If older versioned documents contain different operational wording, this file controls current repository practice.

## 1. Japanese-first rule

Japanese is the base and normative language of this theoretical system.

The required process is:

```text
Think and generate in Japanese
→ Define and structure in Japanese
→ Audit in Japanese
→ Establish Japanese original
→ Translate only when practically necessary
→ Audit differences against the Japanese original
```

Other languages are used only when practically required for international publication, standards, APIs, collaboration, or equivalent external needs.

Translations are projections generated from the Japanese original, not independent originals. If meaning conflicts, the Japanese original controls.

## 2. Current names

- **神の領域原理（仮）** — short name: **神域原理（仮）**
- **Trinity Principle / トリニティ原理**
- **Closure Phase Ψ / 閉包位相Ψ**
- **Human Decision-making System（仮）** — Japanese name: **人間意思決定理論（仮）** — abbreviation: **HDS**

The provisional marker `（仮）` is used only for 神の領域原理（仮）／神域原理（仮） and HDS.

## 3. HDS disclosure boundary

Public disclosure of HDS is limited, in principle, to the names:

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

Internal structure, operational procedures, evaluation design, judgment mechanisms, implementation, reproducible recipes, and related details are outside the current public scope.

Older versioned descriptions of HDS are retained only as historical artifacts of those versions and do not define current public HDS specifications.

## 4. Existing bilingual documents

Some documents created before the current Japanese-first policy retain an English-first bilingual layout. They are preserved as version history.

All new documents and future revisions must use:

```text
Part I. Japanese Original
Part II. English Translation
```

## 5. Upstream positioning

The repository is organized as a Cognitive Engineering theoretical system. The first two foundational documents are:

1. `00_認知工学とは何か_v0_1_ja_en.md`
2. `01_情報工学における言語基底論_v0_1_ja_en.md`

Readers should proceed from these foundations to the public principles, definitions, and applications.
