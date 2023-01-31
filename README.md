# mastodon-bot  

MastodonでBOTを稼働させるサンプルです。  
主に[うかどん](https://ukadon.shillest.net/)を例とした解説をしますが、  
他のサーバーでも応用可能なはずです。  

## 事前準備  

### BOTアカウントの作成  

自身が利用するMastodonサーバーでBOTアカウントを作成してください。  
まず、お試しで自分のアカウントで投稿するのも良いと思います。  

### アクセストークンの取得  

投稿したいアカウントで[こちら](https://ouvill.net/from_twitter_to_mastdon/#i-4)を参考にアクセストークンを取得してください。  
readとwriteの権限があればOKです。  

## リポジトリの作成

現在見ているリポジトリをテンプレートとして自分のリポジトリを作成します。  

1. 右上の `Use this template` から `create a new repository` を選択してください。
   ![Use this template](https://user-images.githubusercontent.com/1221423/169618716-fb17528d-f332-4fc5-a11a-eaa23562665e.png)
2. 適当な名前を付けて `Create repository from template` を押してください。
   ![Create a new repository](https://user-images.githubusercontent.com/1221423/169618722-406dc508-add4-4074-83f0-c7a7ad87f6f3.png)

自身のリポジトリが作成されます。  
(スクショ: [skills/introduction-to-github](https://github.com/skills/introduction-to-github)より)

## Actions secrets の設定

1. 現在はcodeタブを開いていると思います。  
   一番右のSettingsタブを開いてください。(歯車マークが付いています)
2. 左カラムの Secrets -> Actions と進みます。
3. 右上の New repository secret を押してください。
4. Name: `MASTODON_ACCESS_TOKEN`  
   Secret: 【事前準備で用意したアクセストークン】

## 動作確認

1. Actionsタブを開いてください。(再生マークが付いています)
2. 左カラムの Satori Sample を選択してください。(里々を使用する場合)
3. 右の方の `Run workflow` ボタンを押してください。
4. 緑の `Run workflow` を選択してください。

正常に動作すればMastodonに時報が投稿されます。

## cronの設定

先程は手動でGitHub Actionsを実行して投稿しましたが、  
毎時0分にGitHub Actionsが実行されるよう設定します。

1. code タブから .github/workflows -> sample_satori.yml を開きます。(里々を使用する場合)
2. 右上の方に鉛筆マーク(Edit this file)を押します。
3. `on:` のところを以下の通り加筆します。
```
on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:
```
4. 右上の `Start commit` -> 何か適当な履歴メッセージを記入して `Commit Changes` を押してください。

これで毎時0分に実行されます。`cron: '30 0 * * *'` とすれば毎日9時30分(UTC時刻0時30分)になります。[参照](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onschedule)  

## 投稿メッセージの編集

投稿メッセージは里々・YAYA・華和梨で書かれています。  

### 里々

1. code タブから shiori/satori/dic_OnMastodon.txt を開きます。
2. `OnMastodonTootRequest` の戻り値を適宜編集し、先程と同じ要領でcommitします。

### YAYA

1. code タブから shiori/yaya/OnMastodon.dic を開きます。
2. `OnMastodonTootRequest` の戻り値を適宜編集し、先程と同じ要領でcommitします。

### 華和梨

1. code タブから shiori/kawari/kawarirc.kis を開きます。
2. `OnMastodonTootRequest` の戻り値を適宜編集し、先程と同じ要領でcommitします。

## ライセンスファイルの削除

LICENSEを削除してください。  
これは元々のテンプレートのリポジトリに対するライセンスファイルであり、あなたのリポジトリのコピーライトはあなたのものですので不要です。
