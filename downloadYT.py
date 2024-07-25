import yt_dlp
import os
import shutil
import argparse
from moveDownload import moveDownload

def main(url):
    # Opciones para la descarga
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Descargar la mejor calidad de video y audio
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Nombre del archivo de salida
        'noplaylist': True,  # No descargar listas de reproducción
        'merge_output_format': 'mp4',  # Formato de salida después de fusionar audio y video
    }

    # Descargar el video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
        # Obtener información del video descargado
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        video_extension = 'mp4'  # Ajustar la extensión al formato de salida

    # Ruta del archivo descargado
    downloaded_file = f'downloads/{video_title}.{video_extension}'

    moveDownload(downloaded_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Descargar y convertir un video de YouTube.')
    parser.add_argument('url', type=str, help='URL del video de YouTube que deseas descargar')
    args = parser.parse_args()
    main(args.url)
