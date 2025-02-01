from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Directory to store MP3 files
MUSIC_DIR = "/var/www/html/mp3/static/music"

@app.route("/")
def index():
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp4")]
    return render_template("index.html", songs=songs)

@app.route("/play/<song>")
def play(song):
    return send_from_directory(MUSIC_DIR, song)

if __name__ == "__main__":
    app.run(debug=True)
