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
    speed_mode = data.get('speed', 'normal')  # normal or slow

    if not text:
        return jsonify({'error': 'No text provided'})

    try:
        # Generate unique filename
        filename = f"audio_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join('static', filename)

        # gTTS with slow mode
        tts = gTTS(text=text, lang='en', slow=(speed_mode == 'slow'))
        tts.save(filepath)

        # Full URL for audio
        full_url = request.host_url + 'static/' + filename
        return jsonify({'audio_url': full_url})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
