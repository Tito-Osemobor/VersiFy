import json
from flask import Flask, redirect,url_for,render_template,request
from dotenv import load_dotenv
import os
from lyricsgenius import Genius

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_token = os.getenv("CLIENT_TOKEN")

app = Flask("__name__",template_folder='/templates')


@app.route("/")
def home():
  return render_template("index.html")

@app.route("/lyrics", methods=['GET','POST'])
def lyrics():
  genius = Genius(client_token)
  title = request.form['song']
  singer = request.form['artist']
  song = genius.search_song(title, singer)
  if song.lyrics:
    data = {"lyrics": song.lyrics}
    json_data = json.dumps(data)
    with open("../scripts/song_lyrics.json", "w") as outfile:
      outfile.write(json_data)
      return render_template("login.html")
  else:
    return render_template("practice2.html")


if __name__ == '__main__':
  app.run()
