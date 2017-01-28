import requests

from app.main.songs.Song import Song
from app.main.util import AccessUtil
import pprint

from app.main.util.exceptions import SongNotFoundException

defaultBase = "https://api.genius.com"


class Client:

    def __init__(self, base_url=defaultBase):
        self.BASE_URL = base_url
        self.SEARCH_URL = self.BASE_URL + "/search"

    def find_song(self, song):
        api_response = requests.get(url=self.SEARCH_URL, data={'q': song.title}, headers=self._get_headers())
        response_json = api_response.json()
        try:
            hits = response_json["response"]["hits"]
        except KeyError:
            print("Error retrieving hits")

        song_info = self._find_match(hits, song.artist)
        if not song_info:
            raise SongNotFoundException("Could not find song", song.title, song.artist)
        return song_info

    def _find_match(self, hits, artist):
        song_info = None
        try:
            for hit in hits:
                if hit["index"] == "song" and hit["result"]["primary_artist"]["name"] == artist:
                    song_info = hit['result']
                    break

        except KeyError:
            # TODO might be good to add a check artist alternative names
            # TODO might be good to check 'non primary artists' if API allows
            print("Error matching artist")
            pprint.pprint(hits)
        return song_info

    def _get_headers(self):
        return {"Authorization": 'Bearer {}'.format(AccessUtil.getAccessToken())}

# some test data
# song1 = Song("1979", "Smashing Pumpkins")
# song2 = Song("The Lung", "Dinosaur Jr.")
# client = GeniusClient()
# pprint.pprint(client.find_song(song1))
# pprint.pprint(client.find_song(song2))

