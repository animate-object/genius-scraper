import pprint

from app.main import genius
from app.main.songs.song import Song
from app.main.util.exceptions import *


class SongService:
    def __init__(self, genius_client, genius_scraper):
        self.client = genius_client
        self.scraper = genius_scraper

    def create_song(self, title, artist):
        return Song(title=title, artist=artist)

    def create_songs(self, titles, artist):
        return [Song(title, artist) for title in titles]

    def populate_song_with_lyrics(self, song):
        song.path = self._get_path_for_song(song)
        song.lyrics = self.scraper.scrape_lyrics(song.path)

    def populate_songs_with_lyrics(self, songs):
        l = len(songs)
        for i, song in enumerate(songs):
            try:
                print("Finding lyrics for song {} of {}: {} by {}".format(i + 1, l, song.title, song.artist))
                self.populate_song_with_lyrics(song)
            except (SongNotFoundException, LyricsNotFoundException, SongPathNotFoundException) as e:
                print("Failed to find lyrics for {} by {}".format(song.title, song.artist))
                print(e.errors)

    def _get_path_for_song(self, song):
        song_meta_data = self.client.find_song(song)
        path = None
        try:
            path = song_meta_data["path"]
        except TypeError:
            pprint.pprint(song_meta_data)
        if not path:
            raise SongPathNotFoundException("Error retrieving path for song", song.title, song.artist)
        return path

    def _get_paths_for_songs(self, songs):
        songs_meta_data = [self.client.find_song(song) for song in songs]
        return [smd["path"] for smd in songs_meta_data]
