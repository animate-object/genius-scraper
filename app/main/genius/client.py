import requests

from app.main.genius.request_wrapper import RequestWrapper
from app.main.songs.song import Song
from app.main.util import access_util

from app.main.util.exceptions import SongNotFoundException, HttpException

defaultBase = "https://api.genius.com"


class Client:
    def __init__(self, base_url=defaultBase):
        self.BASE_URL = base_url
        self.SEARCH_URL = self.BASE_URL + "/search"
        self.wrapper = RequestWrapper()

    def find_song(self, song, retry=False):
        response_json = self.wrapper.get_with_headers(
            url=self.SEARCH_URL, payload={'q': song.title + " " + song.artist}, success_code=200
        )

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
        return song_info
