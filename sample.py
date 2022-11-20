#おまじない 使用する道具をここで宣言します
from os import getenv
import requests
import zoneinfo
import datetime
import random

#←これはコメント 里々や華和梨と一緒ですね
#投稿するメッセージを返す関数の定義
def get_message():
	#現在時刻の取得サンプル
	jst = zoneinfo.ZoneInfo('Asia/Tokyo')
	now = datetime.datetime.now(jst)
	mes1 = now.strftime('%H時%M分') #年から秒まで出力するには '%Y-%m-%d %H:%M:%S' とする
	#配列からランダムで選択するサンプル
	gobi = ['をお知らせします', 'ですわ', 'やで']
	mes2 = random.choice(gobi)
	#if文のサンプル
	if now.hour < 6:
		mes3 = 'こんばんは'
	elif now.hour < 10:
		mes3 = 'おはようございます'
	elif now.hour < 18:
		mes3 = 'こんにちは'
	else:
		mes3 = 'こんばんは'
	#ハッシュタグを加えてみる
	mes4 = '#ukadon_bot'
	#文字列を結合するには+でつなぐ \nは改行 伺かと一緒ですね
	mes = mes1 + mes2 + '\n' + mes3 + ' ' + mes4
	#完成した文字列を返す
	return mes

#mastodonに投稿する関数 ここは読み飛ばしてください
def post_entry(mastodon_url, access_token, status, visibility='unlisted'):
	url = f'{mastodon_url}api/v1/statuses'
	headers = {'Authorization': f'Bearer {access_token}'}
	payload = {'status': status, 'visibility': visibility}
	r = requests.post(url, data=payload, headers=headers)
	r.raise_for_status()

#ここからスタートします
if __name__ == '__main__':
	#投稿先のMastodonのURL
	mastodon_url = 'https://ukadon.shillest.net/'
	#アクセストークン これはGitHubのSettingでActions secretsを設定しておきます ナイショの文字列なので
	access_token = getenv('MASTODON_ACCESS_TOKEN')
	#投稿するメッセージ
	status = get_message()
	#公開範囲 public(公開), unlisted(未収載), private(フォロワーのみ), direct(指定された相手のみ) (directは宛先も必要)
	visibility = 'unlisted'
	#投稿
	post_entry(mastodon_url, access_token, status, visibility)
	#ログメッセージ
	print(f'正常に {status} と投稿できました。')
