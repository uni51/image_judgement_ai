from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの種類

key = "XXXX" # FlickerAPIで取得したkeyに置き換えること
secret = "XXXX" # FlickerAPIで取得したsecretに置き換えること
wait_time = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance', # 検索の関連順に並べる
    safe_search = 1, # コンテンツは表示しない
    extras = 'url_q, license'
)

photos = result['photos']
# 返り値を表示する
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath) # URL で表されるネットワークオブジェクトをローカルファイルにコピーする
    time.sleep(wait_time)
