from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text')
    speed = data.get('speed', 1.0)

    if not text:
        return jsonify({'error': 'No text provided'})

    # Generate unique filename
    filename = f"static/audio_{uuid.uuid4().hex}.mp3"

    # Generate TTS with Google Text-to-Speech
    tts = gTTS(text=text, lang='en', slow=(speed < 1.0))
    tts.save(filename)

    return jsonify({'audio_url': '/' + filename})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
