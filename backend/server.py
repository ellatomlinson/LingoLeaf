from flask import Flask, jsonify
from audio_utils import start_recording, stop_recording, transcribe_audio

app = Flask(__name__)

stream = None
buffer = []
fs = 44100 

@app.route('/start', methods=['POST'])
def start():
    global stream, buffer
    print("Starting recording... farts")
    start_recording()
    return jsonify({"status": "recording started"})

@app.route('/stop', methods=['POST'])
def stop():
    global stream, buffer
    stop_recording()

    return jsonify({"status": "recording stopped"})

@app.route('/transcribe', methods=['POST'])
def transcribe():
    result = transcribe_audio()
    return jsonify({"transcription": result})

if __name__ == "__main__":
    app.run(port=5001)
