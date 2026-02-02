import os

from flask import Flask, jsonify, render_template, request, send_file
from yt_dlp import YoutubeDL

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json(force=True)
    url = data.get("url")
    if not url:
        return jsonify({"message": "No URL provided"}), 400

    # Temporary output filename
    output_file = "downloaded_audio.mp3"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "audio")
            filename = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"
            return send_file(filename, as_attachment=True, download_name=f"{title}.mp3")

    except Exception as e:
        return jsonify({"message": "Failed to download: " + str(e)})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
