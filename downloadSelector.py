import yt_dlp
import os
import shutil
import argparse

def list_formats(url):
    ydl_opts = {
        'listformats': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=False)

def download_video(url, format_code):
    # Opciones para la descarga
    ydl_opts = {
        'format': format_code,  # Descargar el formato seleccionado
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Nombre del archivo de salida
        'noplaylist': True,  # No descargar listas de reproducción
    }

    # Descargar el video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
        # Obtener información del video descargado
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        video_extension = info_dict.get('ext', None)
    
    # Ruta del archivo descargado
    downloaded_file = f'downloads/{video_title}.{video_extension}'

    # Carpetas de destino
    destination_folders = ['tiktok', 'youtube', 'instagram']

    # Crear las carpetas de destino si no existen y copiar el archivo
    for folder in destination_folders:
        destination_path = os.path.join('downloads', folder)
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
            os.makedirs(destination_path + '/processed')
        shutil.copy(downloaded_file, destination_path)
    
    os.remove(downloaded_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Descargar y convertir un video de YouTube.')
    parser.add_argument('url', type=str, help='URL del video de YouTube que deseas descargar')
    args = parser.parse_args()

    # Listar los formatos disponibles
    list_formats(args.url)
    
    # Solicitar al usuario que seleccione un formato
    format_code = input("Introduce el código del formato que deseas descargar: ")
    
    # Descargar el video en el formato seleccionado
    download_video(args.url, format_code)
