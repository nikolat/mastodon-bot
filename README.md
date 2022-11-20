# mastodon-bot  

MastodonでBOTを稼働させるサンプルです。  
主に[うかどん](https://ukadon.shillest.net/)を例とした解説をしますが、  
他のサーバーでも応用可能なはずです。  

## 事前準備  

### BOTアカウントの作成  

自身が利用するMastodonサーバーでBOTアカウントを作成してください。  
まず、お試しで自分のアカウントで投稿するのも良いと思います。  

### アクセストークンの取得  

投稿したいアカウントで[こちら](https://ukadon.shillest.net/@nikolat/109364410054265227)を参考にアクセストークンを取得してください。  
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
2. 左カラムの Exec Sample を選択してください。
3. 右の方の `Run workflow` ボタンを押してください。
4. 緑の `Run workflow` を選択してください。

正常に動作すればMastodonに時報が投稿されます。

## cronの設定

先程は手動でGitHub Actionsを実行して投稿しましたが、  
毎時0分にGitHub Actionsが実行されるよう設定します。

1. code タブから .github/workflows -> sample.ymal を開きます。
2. 右上の方に鉛筆マーク(Edit this file)を押します。
3. `on:` のところを以下の通り加筆します。
```
on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:
```
4. 右上の `Start commit` -> 何か適当な履歴メッセージを記入して `Comitt Changes` を押してください。

これで毎時0分に実行されます。`cron: '30 0 * * *'` とすれば毎日9時30分(UTC時刻0時30分)になります。[参照](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onschedule)  

## 投稿メッセージの編集

投稿プログラムはPythonというプログラミング言語で書かれています。  
参考: [Python入門](https://www.javadrive.jp/python/)  
ここでは複雑な解説はしません。  
メッセージの編集方法だけ案内します。  

1. code タブから sample.py を開きます。
2. `def get_message():` 行を以下の通り編集し、先程と同じ要領でcommitします。

```
def get_message():
	return '固定メッセージ'
```
これで毎回固定メッセージが投稿されます。  
現在時刻の取得、ランダム選択、if文の分岐、文字列処理の方法など  
初期状態では簡単なサンプルだけ載せてあります。  
より複雑なことを行う場合は Python を習得する必要があります。  

未熟な私の作ったBOTでよければ[こちら](https://github.com/nikolat/potiboard-update-checker)にありますので参考にしてください。
