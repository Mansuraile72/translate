from flask import Flask, render_template, request, jsonify, send_from_directory
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
    speed = float(data.get('speed', 1.0))

    if not text:
        return jsonify({'error': 'No text provided'})

    # Generate unique filename
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join('static', filename)

    # Generate TTS audio (speed adjustment)
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(filepath)

    # Return full URL to the audio
    full_url = request.host_url + 'static/' + filename
    return jsonify({'audio_url': full_url})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
