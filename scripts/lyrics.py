import json
from dotenv import load_dotenv
import os
from lyricsgenius import Genius

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_token = os.getenv("CLIENT_TOKEN")

genius = Genius(client_token)
singer = "The Weeknd"
title = "In the night"
# artist = genius.search_artist(singer, max_songs=3)
song = genius.search_song(title, singer)
if song.lyrics:
    data = {"lyrics":song.lyrics}
    json_data = json.dumps(data)
    with open("song_lyrics.json", "w") as outfile:
        outfile.write(json_data)
else:
    print("This song doesn't have lyrics.")