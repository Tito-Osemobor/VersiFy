import json
from flask import Flask, request
from dotenv import load_dotenv
import os
from lyricsgenius import Genius

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_token = os.getenv("CLIENT_TOKEN")

app = Flask(__name__)


@app.route("/lyrics", methods=['POST'])
def lyrics():
  print("hi")
  genius = Genius(client_token)
  title = request.form['song']
  singer = request.form['artist']
  song = genius.search_song(title, singer)
  if song.lyrics:
    data = {"lyrics": song.lyrics}
    json_data = json.dumps(data)
    with open("../scripts/song_lyrics.json", "w") as outfile:
      outfile.write(json_data)
      return "Lyrics successfully retrieved and stored in song_lyrics.json"
  else:
    print("This song doesn't have lyrics.")


if __name__ == '__main__':
  app.run()
