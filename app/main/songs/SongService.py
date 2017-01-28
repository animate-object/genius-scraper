

class SongService:
    def __init__(self, geniusClient):
        self.geniusClient = geniusClient

    def createSong(self, title, artist):
        return Song(title=title, artist=artist)

    def createSongs(self, titles, artist):
        return [Song(title, artist) for title in titles]

    def getPathForSong(self, song):
        song_meta_data = self.geniusClient.findSong(song)
        path = song_meta_data["path"]
        return path

    def getPathsForSongs(self, songs):
        songs_meta_data = [self.geniusClient.findSong(song) for song in songs]
        return [smd["path"] for smd in songs_meta_data]


class Song:
    def __init__(self, title, artist, lyrics=None):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
