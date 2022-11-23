import subprocess
import os
import requests
import sys

#栞を呼び出して投稿メッセージを取得する
def get_message(shiori):
	dlldir = os.getcwd()
	if shiori == 'yaya':
		dllpath = r'shiori\yaya\yaya.dll'
		dlldir += r'\shiori\yaya\\'
		enc = 'utf-8'
	elif shiori == 'kawari':
		dllpath = r'shiori\kawari\shiori.dll'
		dlldir += r'\shiori\kawari\\'
		enc = 'shift_jis'
	else:
		dllpath = r'shiori\satori\satori.dll'
		dlldir += r'\shiori\satori\\'
		enc = 'shift_jis'
	s = ''
	subprocess.run(fr'shioricaller\shioricaller.exe {dllpath} {dlldir} < shioricaller\request.txt > shioricaller\response.txt', shell=True)
	with open(r'shioricaller\response.txt', encoding=enc) as f:
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
	#使用する栞
	shiori = sys.argv[1]
	#投稿先のMastodonのURL
	mastodon_url = 'https://ukadon.shillest.net/'
	#アクセストークン これはGitHubのSettingでActions secretsを設定しておきます ナイショの文字列なので
	access_token = os.getenv('MASTODON_ACCESS_TOKEN')
	#投稿するメッセージ
	status = get_message(shiori)
	#公開範囲 public(公開), unlisted(未収載), private(フォロワーのみ), direct(指定された相手のみ) (directは宛先も必要)
	visibility = 'unlisted'
	#投稿
	post_entry(mastodon_url, access_token, status, visibility)
	#ログメッセージ
	print(f'正常に {status} と投稿できました。')
