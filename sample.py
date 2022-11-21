import subprocess
import os
import requests

#里々を呼び出して投稿メッセージを取得する
def get_message():
	s = ''
	subprocess.run(fr'shioricaller\shioricaller.exe ghost\master\satori.dll {os.getcwd()}\ghost\master\ < shioricaller\request.txt > shioricaller\response.txt', shell=True)
	with open(r'shioricaller\response.txt', encoding='shift_jis') as f:
		for line in f:
			if line.startswith('Value: '):
				s = line[7:]
				break
	s = s.replace(r'\n', '\n')
	return s

#Mastodonへ投稿する
def post_entry(mastodon_url, access_token, status, visibility='unlisted'):
	url = f'{mastodon_url}api/v1/statuses'
	headers = {'Authorization': f'Bearer {access_token}'}
	payload = {'status': status, 'visibility': visibility}
	r = requests.post(url, data=payload, headers=headers)
	r.raise_for_status()

if __name__ == '__main__':
	#投稿先のMastodonのURL
	mastodon_url = 'https://ukadon.shillest.net/'
	#アクセストークン これはGitHubのSettingでActions secretsを設定しておきます ナイショの文字列なので
	access_token = os.getenv('MASTODON_ACCESS_TOKEN')
	#投稿するメッセージ
	status = get_message()
	#公開範囲 public(公開), unlisted(未収載), private(フォロワーのみ), direct(指定された相手のみ) (directは宛先も必要)
	visibility = 'unlisted'
	#投稿
	post_entry(mastodon_url, access_token, status, visibility)
	#ログメッセージ
	print(f'正常に {status} と投稿できました。')
