const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

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

app.whenReady().then(createWindow);
