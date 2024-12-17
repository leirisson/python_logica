const { app, BrowserWindow } = require('electron');
const path = require('path');

let mainWindow;

app.on('ready', () => {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        icon: path.join(__dirname, 'assets', 'icon.png'), // Caminho para o ícone
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'), // Opcional
        },
    });

    // Carregue sua aplicação web (local ou remota)
    mainWindow.loadFile('index.html'); // Ou use `loadURL('http://localhost:3000')` para apps com servidor
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});
