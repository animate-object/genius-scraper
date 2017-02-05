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


class NoSuchPropertyException(Exception):
    def __init__(self, message, property_name):
        super(NoSuchPropertyException, self).__init__(message)
        self.errors = "Could not find property <{}> in app-config".format(property_name)


class HttpException(Exception):
    def __init__(self, message, status_code, response):
        super(HttpException, self).__init__(message)
        self.errors = "Request failed with code {},\n" \
                      "api response:\n" \
                      "{}".format(status_code, response)
