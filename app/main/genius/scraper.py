import requests
from bs4 import BeautifulSoup as soup

defaultBase = "http://genius.com"


class Scraper:
    def __init__(self, base_url=defaultBase):
        self.BASE_URL = base_url

    def scrape_lyrics(self, path):
        page = requests.get(self.BASE_URL + path)
        html = soup(page.text, "html.parser")
        [h.extract() for h in html('script')]
        lyrics = html.find("lyrics").get_text()

        return lyrics
