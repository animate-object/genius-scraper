
class Song:
    def __init__(self, title, artist, lyrics=None, path=None):
        self.title = title
        self.artist = artist
        self.path = path
        self.lyrics = lyrics

    def setPath(self, path):
        self.path = path

    def setLyrics(self, lyrics):
        self.lyrics = lyrics
