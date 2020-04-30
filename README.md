# いろんな会社のコーポレートサイトを取得
## Wantedly
https://www.wantedly.com

事前にアカウント取得が必要

### 現状の検索条件
- エンジニアリング
- 副業・契約・委託
- 関東

今後、ここを可変にしていきたい

## How to use
`wantedlyEmailID` と `WantedlyPassword` は変えてください
```
$ tag_name=scrape
$ docker build --tag=$tag_name .
$ docker run --rm -v $(pwd):/scrape $tag_name python main.py 'wantedlyEmailID' 'WantedlyPassword'
```