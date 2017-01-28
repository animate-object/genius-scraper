import requests
from bs4 import BeautifulSoup as soup
from app.main.util.AccessUtil import *
import pprint

BASE_URL = "https://api.genius.com"
SEARCH_URL = BASE_URL + "/search"
song_title = "Stayin Alive"
artist_name = "The Bee Gees"
data = {'q': song_title}
headers = {'Authorization': 'Bearer {}'.format(getAccessToken())}

response = requests.get(SEARCH_URL, data=data, headers=headers)

json = response.json()

song_info = None
for hit in json["response"]["hits"]:
    if hit["result"]["primary_artist"]["name"] == artist_name:
        song_info = hit["result"]
        break
path = song_info["path"]
print(path)

PAGE_URL = "http://genius.com" + path

page = requests.get(PAGE_URL)

html = soup(page.text, "html.parser")

[h.extract() for h in html('script')]
lyrics = html.find("lyrics").get_text()

print(lyrics)