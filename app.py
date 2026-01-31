from flask import Flask, request, jsonify, render_template
import yt_dlp as youtube_dl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    url = data['url']
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return jsonify({'message': 'Download complete!'})
    except Exception as e:
        return jsonify({'message': 'Failed to download: ' + str(e)})

if __name__ == '__main__':
    app.run(debug=True)
