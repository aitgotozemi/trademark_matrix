# 商標データベース (trademark_db)

## テーブル情報

| 項目                           | 値                                                                                                   |
|:-------------------------------|:-----------------------------------------------------------------------------------------------------|
| システム名                     |                                                                                                      |
| サブシステム名                 |                                                                                                      |
| 物理エンティティ名             | trademark_db                                                                                         |
| 論理エンティティ名             | 商標データベース                                                                                     |
| 作成者                         |                                                                                                      |
| 作成日                         | 2026/05/14                                                                                           |
| タグ                           |                                                                                                      |



## カラム情報

| No. | 論理名                         | 物理名                         | データ型                       | Not Null | デフォルト           | 備考                           |
|----:|:-------------------------------|:-------------------------------|:-------------------------------|:---------|:---------------------|:-------------------------------|
|   1 | 発行国・地域                   | publication-country            | text                           |          |                      |                                |
|   2 | 発行日                         | publication-date               | character varying(23)          | Yes (PK) |                      |                                |
|   3 | 公報種別                       | kind-of-official-gazette       | text                           | Yes (PK) |                      |                                |
|   4 | 登録番号                       | registration-number            | character varying(41)          | Yes (PK) |                      |                                |
|   5 | 登録日                         | registration-date              | character varying(23)          |          |                      |                                |
|   6 | 商標種別                       | trademark                      | character varying(19)          |          |                      |                                |
|   7 | 商品及び役務の区分の数         | number-of-goods-service-class  | integer                        |          |                      |                                |
|   8 | 指定商品又は指定役務名とコード | goods-and-service-name-and-code | text                           |          |                      |                                |
|   9 | 出願番号                       | application-number             | character varying(27)          | Yes (PK) |                      |                                |
|  10 | 出願日                         | filing-date                    | character varying(32)          |          |                      |                                |
|  11 | 商標権利者識別番号             | right-holder-group-identification-number | integer                        |          |                      |                                |
|  12 | 商標権者氏名                   | right-holder-group-name        | text                           |          |                      |                                |
|  13 | 商標権利者オリジナルネーム     | right-holder-group-original-name | text                           |          |                      |                                |
|  14 | 商標権者住所                   | right-holder-group-address     | text                           |          |                      |                                |
|  15 | 代理人識別番号                 | proxy-identification-number    | integer                        |          |                      |                                |
|  16 | 代理人団体、および氏名         | proxy-name                     | text                           |          |                      |                                |
|  17 | 法区分                         | distinction-of-the-law         | character varying(7)           |          |                      |                                |
|  18 | 審査官氏名                     | examiner-group                 | text                           |          |                      |                                |
|  19 | 称呼                           | pronunciation                  | text                           |          |                      |                                |
|  20 | 検索用文字商標                 | trademark-for-indication       | text                           |          |                      |                                |
|  21 | 類似群区別及びコード           | similar-group-classification-and-code | text                           |          |                      |                                |
|  22 | ウィーン分類                   | vienna-figure-classification   | text                           |          |                      |                                |
|  23 | 書換登録申請番号               | replaced-application-number    | text                           | Yes (PK) |                      |                                |
|  24 | 訂正要旨                       | gist-of-correction             | text                           | Yes (PK) |                      |                                |



## インデックス情報

| No. | インデックス名                 | カラムリスト                             | ユニーク   | オプション                     | 
|----:|:-------------------------------|:-----------------------------------------|:-----------|:-------------------------------|



## リレーションシップ情報

| No. | 動詞句                         | カラムリスト                             | 参照先                         | 参照先カラムリスト                       | ON DELETE    | ON UPDATE    |
|----:|:-------------------------------|:-----------------------------------------|:-------------------------------|:-----------------------------------------|:-------------|:-------------|



## リレーションシップ情報(PK側)

| No. | 動詞句                         | カラムリスト                             | 参照元                         | 参照元カラムリスト                       | ON DELETE    | ON UPDATE    |
|----:|:-------------------------------|:-----------------------------------------|:-------------------------------|:-----------------------------------------|:-------------|:-------------|


