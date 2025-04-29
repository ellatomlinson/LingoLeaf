const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const say = require('say');
const axios = require('axios');

let pythonServer;

// Create the window
function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    }
  });
  win.loadFile('frontend/index.html');
}

// Set up the IPC handler to get a random phrase
ipcMain.handle('get-random-phrase', async () => {
  return new Promise((resolve, reject) => {
    const py = spawn('python3', ['backend/get_random_phrase.py']);
    
    let result = '';
    py.stdout.on('data', data => result += data.toString());
    py.stderr.on('data', err => console.error(err.toString()));
    py.on('close', () => resolve(result.trim()));
  });
});

// Set up IPC to handle text-to-speech
ipcMain.handle('speak-text', (event, text) => {
  say.speak(text, null, 1.0, (err) => {
    if (err) {
      console.error('Text-to-speech error:', err);
    } else {
      console.log('Speech finished');
    }
  });
});

ipcMain.handle('start-recording', async () => {
  await axios.post('http://localhost:5001/start');
  return "Recording started";
});

ipcMain.handle('stop-and-process', async (event, targetPhrase) => {
  await axios.post('http://localhost:5001/stop');  // stop recording
  const response = await axios.post('http://localhost:5001/transcribe'); // transcribe recording
  const spokenPhrase = response.data.transcription;

  return new Promise((resolve, reject) => {
    const py = spawn('python3', ['backend/pronunciation_processing.py', targetPhrase, spokenPhrase]);
    
    let result = '';
    py.stdout.on('data', data => result += data.toString());
    py.stderr.on('data', err => console.error('Python error:', err.toString()));
    
    py.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(`Python process exited with code ${code}`));
      } else {
        try {
          const parsedResult = JSON.parse(result);
          resolve({ spokenPhrase, ...parsedResult });
        } catch (err) {
          reject(new Error('Failed to parse Python output: ' + err.message));
        }
      }
    });
  });
});


app.whenReady().then(() => {
  pythonServer = spawn('python3', ['backend/server.py']);

  pythonServer.stdout.on('data', (data) => {
    console.log(`PYTHON: ${data}`);
  });

  pythonServer.stderr.on('data', (data) => {
    console.error(`PYTHON ERROR: ${data}`);
  });

  pythonServer.on('close', (code) => {
    console.log(`Python server exited with code ${code}`);
  });

  createWindow();
});
