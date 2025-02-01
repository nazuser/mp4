from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Directory to store MP3 files
MUSIC_DIR = "/var/www/html/mp4/static/music"

@app.route("/")
def index():
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("index.html", songs=songs)

@app.route("/play/<song>")
def play(song):
    return send_from_directory(MUSIC_DIR, song)

@app.route('/tetris')
def tetris():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("tetris.html", songs=songs)

@app.route('/v')
def v():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("v.html", songs=songs)



@app.route('/tetris2')
def tetris2():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("tetris2.html", songs=songs)

@app.route('/brickver1')
def brickver1():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("brickver1.html", songs=songs)

@app.route('/brick2')
def brick2():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("brick2.html", songs=songs)




@app.route('/tic')
def tic():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("tic.html", songs=songs)

@app.route('/one')
def one():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("one.html", songs=songs)

@app.route('/star')
def star():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("star.html", songs=songs)



@app.route('/indexmath')
def indexmath():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("indexmath.html", songs=songs)

@app.route('/indexeng')
def indexeng():
    """
    Render the browse page.
    """
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return render_template("indexeng.html", songs=songs)


if __name__ == "__main__":
    app.run(debug=True)

