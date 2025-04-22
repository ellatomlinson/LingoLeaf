import whisper
import sounddevice as sd
import numpy as np

# Record audio from the microphone for a specified duration
def record_audio(filename="output.wav", duration=3, fs=44100):
    print("🎤 Recording... Speak now!")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("✅ Done recording!\n")

# Transcribe the recorded audio to text using Whisper
def transcribe_audio(filename="output.wav"):
    print("🧠 Transcribing with Whisper...")
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    print(f"📝 You said: \"{result['text']}\"\n")
    return result["text"]
