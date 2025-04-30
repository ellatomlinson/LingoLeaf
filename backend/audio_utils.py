import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

# Transcribe the recorded audio to text using Whisper
def transcribe_audio(filename="output.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result["text"]

def start_recording(fs=44100):
    global stream, buffer
    buffer = []

    def callback(indata, frames, time, status):
        if status:
            print(status)
        buffer.append(indata.copy())

    stream = sd.InputStream(samplerate=fs, channels=1, callback=callback)
    stream.start()

def stop_recording(filename="output.wav", fs=44100):
    global stream, buffer
    stream.stop()
    stream.close()

    # Convert the buffer to a numpy array and save it as a WAV file
    audio_data = np.concatenate(buffer, axis=0)
    write(filename, fs, audio_data)