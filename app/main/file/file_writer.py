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

    def write_to_file(self, song):
        artist_dir_name = self._replace_forbidden(
            '-'.join(song.artist.lower().split())
        )

        song_file_name = self._replace_forbidden(
            '-'.join(song.title.lower().split())[:20]
        ) + ".txt"

        artist_path = os.path.join(self.lyrics_directory, artist_dir_name)

        if not os.path.isdir(artist_path):
            os.mkdir(artist_path)

        full_path = os.path.join(artist_path, song_file_name)

        with open(full_path, "w") as out:
            out.write("## ARTIST: " + song.artist + "\n")
            out.write("## TITLE: " + song.title + "\n")
            out.write("\n\n")

            out.write(song.lyrics)

    def _replace_forbidden(self, path_part, replace_with="#"):
        ret = ""
        for char in path_part:
            if char in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
                ret += replace_with
            else:
                ret += char

        return ret

# # Working test code
# f = CustomFileWriter()
# #  print(f.lyrics_directory)
#
# #
# # print(
# #     f._replace_forbidden("abc*<>def")
# # )
#
# s = Song(title="test song", artist="the testers")
# s.setLyrics("""\
# this is a song
# a testing song
# we love to test our code
# """)
#
# f.write_to_file(s)
