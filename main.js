const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const say = require('say');

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
  console.log('wzw4ejf');

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

app.whenReady().then(createWindow);
