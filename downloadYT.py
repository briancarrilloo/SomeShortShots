import yt_dlp
from datetime import datetime
import argparse

def main(url):
    # Opciones para la descarga
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Descargar la mejor calidad de video y audio
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Nombre del archivo de salida
        'noplaylist': True,  # No descargar listas de reproducción
    }

    # Descargar el video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Descargar y convertir un video de YouTube.')
    parser.add_argument('url', type=str, help='URL del video de YouTube que deseas descargar')
    args = parser.parse_args()
    main(args.url)
