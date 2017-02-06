
class Song:
    def __init__(self, title, artist, lyrics=None, path=None):
        self.title = title
        self.artist = artist
        self.path = path
        self.lyrics = lyrics

    def __str__(self):
        return "<Song Object | {} by {}>".format(
            self.title, self.artist
        )

    def set_path(self, path):
        self.path = path

    def set_lyrics(self, lyrics):
        self.lyrics = lyrics
