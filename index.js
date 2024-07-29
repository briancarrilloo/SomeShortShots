// Script de node que inicia una API que recibe una URL de youtube o instagram, la separa y ejecuta los scripts de descarga

const express = require('express');
const morgan = require('morgan');
const { exec } = require('child_process');
const path = require('path');

const app = express();
app.use(express.json());
// Middleware
app.use(morgan('dev'));

const rootDir = path.resolve(__dirname);
const venvActivate = path.join(rootDir, 'downloaderEnv', 'bin', 'activate');

// Downloader
const downloadFromYoutube = async (URL) => {
  console.log(`Ejecutando: . ${venvActivate} && python3 downloadYT.py ${URL}`);
  exec(`bash -c ". ${venvActivate} && python3 downloadYT.py ${URL}"`, { cwd: rootDir }, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error ejecutando el script de Python: ${error.message}`);
      console.error(`stderr: ${stderr}`);
    } else {
      console.log(`Salida del script de Python: ${stdout}`);
    }
  });
}

const downloadFromInstagram = async (URL) => {
  console.log(`Ejecutando: . ${venvActivate} && python3 downloadIG.py ${URL}`);
  exec(`bash -c ". ${venvActivate} && python3 downloadIG.py ${URL}"`, { cwd: rootDir }, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error ejecutando el script de Python: ${error.message}`);
      console.error(`stderr: ${stderr}`);
    } else {
      console.log(`Salida del script de Python: ${stdout}`);
    }
  });
}

// Routes 
app.post('/getVideo', async (req, res) => {
  const URL = req.body.URL;
  console.log(`Processing ${URL}`);

  try {
    if (URL.includes("youtube")) {
      downloadFromYoutube(URL);
    } else if (URL.includes("instagram")) {
      downloadFromInstagram(URL);
    } else {
      console.log(`Unknown social network ${URL}`);
      res.status(400).send(`Unknown social network ${URL}`);
      return;
    }

    res.status(200).send('Video download initiated!');
  } catch (error) {
    console.error('Error iniciando la descarga del video:', error);
    res.status(500).send('Error initiating video download');
  }
});

// Start server
const PORT = process.env.PORT || 3000;
const HOST = '0.0.0.0'; // Escuchar en todas las interfaces de red
app.listen(PORT, HOST, () => {
  console.log(`Server is running on http://${HOST}:${PORT}`);
});
