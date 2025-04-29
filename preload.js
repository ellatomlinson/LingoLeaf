const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('api', {
  getRandomPhrase: () => ipcRenderer.invoke('get-random-phrase'),
  speakText: (text) => ipcRenderer.invoke('speak-text', text),
  startRecording: () => ipcRenderer.invoke('start-recording'),
  stopAndProcessRecording: (targetPhrase) => ipcRenderer.invoke('stop-and-process', targetPhrase),
});