from flask import Flask, jsonify
from api.spotify import get_now_playing, is_configured

app = Flask(__name__)

@app.route("/")
def home():
    return "Spotify API Running"

@app.route("/api/spotify")
def spotify():
    if not is_configured():
        return jsonify({"error": "Spotify not configured"})

    try:
        data = get_now_playing()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

from flask import redirect

@app.route("/")
def home():
    return redirect("/api/spotify")
    
# WAJIB untuk Vercel
handler = app
