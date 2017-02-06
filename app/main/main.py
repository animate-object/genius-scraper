from app.main.file.file_writer import CustomFileWriter
from app.main.file.tracklist_reader import songs_from_tracklist
from app.main.genius.client import Client
from app.main.genius.scraper import Scraper
from app.main.songs.song_service import SongService
from app.paths import DATA_DIR
import os.path

# Proof of concept code for testing

test_track_list_path = os.path.join(
    DATA_DIR, *['tracklists', 'test-tracklists.txt']
)

f = CustomFileWriter()
client = Client()
scraper = Scraper()

service = SongService(genius_client=client, genius_scraper=scraper)

songs = songs_from_tracklist(test_track_list_path)

service.populate_songs_with_lyrics(songs)

f.write_songs(songs)
