import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

# Record audio from the microphone for a specified duration
# def record_audio(filename="output.wav", duration=3, fs=44100):
#     print("🎤 Recording... Speak now!")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
#     sd.wait()
#     write(filename, fs, audio)
#     print("✅ Done recording!\n")

# Transcribe the recorded audio to text using Whisper
def transcribe_audio(filename="output.wav"):
    print("🧠 Transcribing with Whisper...")
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    print(f"📝 You said: \"{result['text']}\"\n")
    return result["text"]

def start_recording(fs=44100):
    global stream, buffer
    buffer = []

    print("🎤 Recording... Speak now!")

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
    print("✅ Done recording!\n")