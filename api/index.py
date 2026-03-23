from flask import Flask, jsonify
from api.spotify import get_now_playing  # atau fungsi yg ada di repo

app = Flask(__name__)

@app.route("/")
def home():
    return "Spotify API is running"

@app.route("/api/spotify")
def spotify():
    data = get_now_playing()
    return jsonify(data)

# WAJIB untuk Vercel
handler = app
