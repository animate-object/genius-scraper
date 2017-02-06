from app.main.songs.song import Song
from app.paths import DATA_DIR
import os.path


def read_track_list(path):
    artist_tracks_map = {}
    with open(path, 'r') as fin:
        artist_name = "UNKNOWN"
        for line in fin:
            line = line.rstrip()
            if line:
                if line.startswith("~ARTIST"):
                    artist_name = ' '.join(line.split()[1:])
                elif line.startswith("#"):  # comment syntax
                    continue
                else:
                    if artist_name in artist_tracks_map:
                        artist_tracks_map[artist_name] += [line]
                    else:
                        artist_tracks_map[artist_name] = [line]
    return artist_tracks_map


def songs_from_tracklist(path):
    songs = []
    artist_tracks_map = read_track_list(path)
    for artist_key in artist_tracks_map:
        for song_name in artist_tracks_map[artist_key]:
            songs.append(Song(song_name, artist_key))
    return songs
