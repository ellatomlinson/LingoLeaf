const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('api', {
  getRandomPhrase: () => ipcRenderer.invoke('get-random-phrase')
});