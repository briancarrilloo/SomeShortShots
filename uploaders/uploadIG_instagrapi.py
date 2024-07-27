# pip3 install instagrapi Pillow moviepy python-dotenv

from instagrapi import Client
import os
import argparse
from dotenv import load_dotenv

# Cargar variables de entorno del archivo .env
load_dotenv()

# Obtener credenciales de las variables de entorno
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

def uploadFile(sourceVideo):
    try:
        cl = Client()
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

        # Ruta del video y configuración
        video_path = sourceVideo
        caption = "Follow for more! #fyp #shorts"

        # Publicación del reel
        cl.clip_upload(video_path, caption)

        os.remove(sourceVideo)
        print(f"Reel publicado con éxito. {sourceVideo}")
    except:
        print(f"Error al publicar el reel. {sourceVideo}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Subir un archivo a instagram y eliminar el original.')
    parser.add_argument('source_file', type=str, help='Ruta del archivo a subir y eliminar.')
    args = parser.parse_args()

    sourceVideo = args.source_file

    if os.path.exists(sourceVideo):
        uploadFile(sourceVideo)
    else:
        print(f"El archivo {sourceVideo} no existe.")