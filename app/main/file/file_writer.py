import os.path
import os

from app.main.songs.song import Song
from app.main.util.config_util import ConfigUtil
from app.paths import DATA_DIR


class CustomFileWriter:
    def __init__(self):
        self.config = ConfigUtil()
        self.lyrics_directory = DATA_DIR
        self.use_default = self.config.get_property("use-default-data-store")

        if not self.use_default:
            raise NotImplementedError("haven't implemented non default data stores yet")

    def write_songs(self, songs):
        l = len(songs)
        for i, song in enumerate(songs):
            try:
                print("Writing to file {} of {}: {} by {}".format(i + 1, l, song.title, song.artist))
                self.write_to_file(song)
            except IOError as e:
                print("Failed to write {} by {}".format(song.title, song.lyrics))
                print(e.errors)

    def write_to_file(self, song):
        if song.lyrics:
            artist_dir_name = self._replace_forbidden(
                '-'.join(song.artist.lower().split())
            )

            song_file_name = self._replace_forbidden(
                '-'.join(song.title.lower().split())[:50]
            ) + ".txt"

            artist_path = os.path.join(self.lyrics_directory, artist_dir_name)

            if not os.path.isdir(artist_path):
                os.mkdir(artist_path)

            full_path = os.path.join(artist_path, song_file_name)

            with open(full_path, "w", encoding="utf-8") as out:
                out.write("#" + "-"*80 + "\n")
                out.write("~ARTIST " + song.artist + "\n")
                out.write("~TITLE " + song.title + "\n")
                out.write("#" + "-"*80 + "\n")
                out.write(song.lyrics)
        else:
            print('COULD NOT WRITE FILE\n\tNo lyrics to write for {}'.format(song))

    def _replace_forbidden(self, path_part, replace_with="#"):
        ret = ""
        for char in path_part:
            if char in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
                ret += replace_with
            else:
                ret += char

        return ret
