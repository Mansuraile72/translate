async function convertText() {
    const text = document.getElementById('text-input').value;
    const speed = parseFloat(document.getElementById('speed-input').value);

    const response = await fetch('/tts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text, speed })
    });

    const result = await response.json();

    if (result.audio_url) {
        const audioPlayer = document.getElementById('audio-player');
        audioPlayer.src = result.audio_url;
        audioPlayer.play();
    } else {
        alert('Error: ' + result.error);
    }
}

