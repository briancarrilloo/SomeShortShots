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

caption = """No problem! Here the information about Mercedes CLS GTR:

The Mercedes CLS GTR is a remarkable racing car celebrated for its outstanding performance and sleek design. Powered by a potent 6.0-liter V12 engine, it delivers over 600 horsepower. 🔧

Accelerated from 0-100 km/h takes approximately 3.7 seconds, with a remarkable top speed surpassing 320hm/h. 🥇

Incorporating advanced aerodynamics features and cutting-edge stability technologies, the CLS GTR ensures exceptional stability and control, particularly high-speed maneuvers. 💨

Originally priced around 1.5 million, the Mercedes CLS GTR is considered one of the most exclusive and prestigious racing cars ever produced. 💰

Its limited production run of just five units adds to its rarity, making it highly sought after by racing enthusiasts and collectors worldwide. 🌎

Join my Instagram, there are regular quizzes about cars and automotive news📱

I invite you to my Telegram channel where you c
"""

def uploadFile(sourceVideo):
    try:
        cl = Client()
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

        # Ruta del video y configuración
        video_path = sourceVideo

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