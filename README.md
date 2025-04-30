![README banner](https://github.com/user-attachments/assets/1bca164f-c34b-4b34-bbf3-dc8e3df9b136)

##

<p align="center">
LingoLeaf is an interactive desktop app made to help you improve your pronunciation!  
</p>

<p align="center">
Whether you're practicing for a test, trying to sound more fluent, or just having fun with language learning, LingoLeaf gives you instant, AI-powered feedback on your speaking!
</p>

##

### Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Demo](#-demo)
- [Future Roadmap](#-future-roadmap)
- [Contact](#-contact)

### 🌿 Features

- **Custom or random practice phrases**
  - Enter your own practice phrases, or click 'Random' to get a phrase selected for you.
  - Note: the random button currently only supports English.
- **Audio playback**
  - Hear the phrase spoken aloud so you can learn how it's pronounced.
  - Note: Audio playback currently only supports English.
- **Speech recording**
  - Record your pronunciation attempt with the microphone button.
- **AI-Powered Pronunciation Feedback**
  - LingoLeaf uses OpenAI's Whisper model to transcribe and analyze your speech.
- **Detailed Scoring**
  - Get an overall pronunciation score.
  - See what the AI heard you say.
  - Hover over individual words to view word-level scores and pinpoint exactly where you can improve!

### 🦾 Tech Stack

- **Electron** - Desktop application framework
- **Python + Flask** - Backend for speech processing and AI integration
- **JavaScript, HTML, CSS** - Frontend UI
- **Whisper (OpenAI)** - For speech transcription

### 🚀 Installation

1. Clone the repository
   `git clone https://github.com/ellatomlinson/LingoLeaf.git`
2. Install NPM packages
   `npm install`
3. Install the other requirements (Flask, Whisper, etc)
   `pip install -r requirements.txt`
4. Run the app
   `npm run start`

### 👀 Demo

![LingoLeafDemoGif](https://github.com/user-attachments/assets/5df0405b-23e8-4920-b4cc-4bdc97b6f8e8)

### 🧩 Future Roadmap

- **Better support for multiple-languages**
  - The 'Random' button and the audio playback currently only support English. In the future, I'd like users to be able to select their target language, so they can have these features as well!
- **Add a Spaced Repetition learning mode**
  - Add a database to log users scores with different practice phrases.
  - Then create a learning mode, which repeats phrases according to the spaced repetition technique, putting extra emphasis on phrases the user has trouble on, so they can better memorize and improve!
- **Save different phrase sets**
  - Allow users to group together phrases into study sets, which they can select and shuffle through.

### 👋 Contact

- [LinkedIn](www.linkedin.com/in/ella-tomlinson25)
