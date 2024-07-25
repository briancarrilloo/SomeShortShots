const express = require('express');
const morgan = require('morgan');
const { exec } = require('child_process');

const app = express();
app.use(express.json());
// Middleware
app.use(morgan('dev'));

// Routes 
app.post('/getVideoYoutube', async (req, res) => {
  const URL = req.body.URL;
  console.log(`Downloading video ${URL}`);

  try {
    // Ejecutar el script de Python de manera asincrónica
    console.log(`Ejecutando: python3 downloadYT.py ${URL}`);
    exec(`python3 downloadYT.py ${URL}`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error ejecutando el script de Python: ${error.message}`);
        console.error(`stderr: ${stderr}`);
      } else {
        console.log(`Salida del script de Python: ${stdout}`);
      }
    });

    // Responder inmediatamente con 200 OK
    res.status(200).send('YouTube video download initiated!');
  } catch (error) {
    console.error('Error iniciando la descarga del video de YouTube:', error);
    res.status(500).send('Error initiating YouTube video download');
  }
});

// Start server
const PORT = process.env.PORT || 3000;
const HOST = '0.0.0.0'; // Escuchar en todas las interfaces de red
app.listen(PORT, HOST, () => {
  console.log(`Server is running on http://${HOST}:${PORT}`);
});
