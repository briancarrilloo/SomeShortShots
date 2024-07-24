const express = require('express');
const morgan = require('morgan');
const { exec } = require('child_process');
const fs = require('fs');

const app = express();
app.use(express.json());
// Middleware
app.use(morgan('dev'));

// Routes 
app.post('/getVideoYoutube', async (req, res) => {
  const URL = req.body.URL;
  console.log(`Downloading video ${URL}`);

  try {
    // Ejecutar el script de Python
    console.log(`Ejecutando: python3 downloadYT.py ${URL}`);
    exec(`python3 downloadYT.py ${URL}`, (error, stdout, stderr) => {
      console.log(`Salida del script de Python: ${stdout}`);
      return res.status(200).send('YouTube video downloaded successfully!');
    });
  } catch (error) {
    console.error('Error descargando el video de YouTube:', error);
    res.status(500).send('Error downloading YouTube video');
  }
});

// Start server
const PORT = process.env.PORT || 3000;
const HOST = '0.0.0.0'; // Escuchar en todas las interfaces de red
app.listen(PORT, HOST, () => {
  console.log(`Server is running on http://${HOST}:${PORT}`);
});
