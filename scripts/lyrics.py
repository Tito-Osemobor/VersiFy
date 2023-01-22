import json
from flask import Flask
from dotenv import load_dotenv
import os
from lyricsgenius import Genius

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_token = os.getenv("CLIENT_TOKEN")

app = Flask(__name__)


@app.route("/lyrics")
def lyrics():
  genius = Genius(client_token)
  singer = "The Weeknd"
  title = "In the night"
  song = genius.search_song(title, singer)
  if song.lyrics:
    data = {"lyrics": song.lyrics}
    json_data = json.dumps(data)
    with open("song_lyrics.json", "w") as outfile:
      outfile.write(json_data)
      print("This works")
  else:
    print("This song doesn't have lyrics.")