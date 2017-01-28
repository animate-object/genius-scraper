class SongPathNotFoundException(Exception):
    def __init__(self, message, title, artist):
        super(SongPathNotFoundException, self).__init__(message)
        self.errors = "Could not retrieve path for song <{}> by artist <{}>".format(title, artist)


class SongNotFoundException(Exception):
    def __init__(self, message, title, artist):
        super(SongNotFoundException, self).__init__(message)
        self.errors = "Could not locate song <{}> by artist <{}>".format(title, artist)


class LyricsNotFoundException(Exception):
    def __init__(self, message, title, artist, path):
        super(SongNotFoundException, self).__init__(message)
        self.errors = "Could not locate song <{}> by artist <{}> at path {}>".format(
            title, artist, path
        )

