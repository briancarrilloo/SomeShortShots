# Script de python que elige un .mp4 al azar de la carpeta de descargas de cada red social, lo publica y elimina la copia local.

# pip3 install instagrapi Pillow moviepy python-dotenv

import os
import random
import subprocess
from dotenv import load_dotenv
from instagrapi import Client
from youtubeUploader import upload_video_to_youtube


# Cargar variables de entorno del archivo .env
load_dotenv()
# Obtener credenciales de las variables de entorno
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
instagram_caption = """No problem! Here the information about Mercedes CLS GTR:

The Mercedes CLS GTR is a remarkable racing car celebrated for its outstanding performance and sleek design. Powered by a potent 6.0-liter V12 engine, it delivers over 600 horsepower. 🔧

Accelerated from 0-100 km/h takes approximately 3.7 seconds, with a remarkable top speed surpassing 320hm/h. 🥇

Incorporating advanced aerodynamics features and cutting-edge stability technologies, the CLS GTR ensures exceptional stability and control, particularly high-speed maneuvers. 💨

Originally priced around 1.5 million, the Mercedes CLS GTR is considered one of the most exclusive and prestigious racing cars ever produced. 💰

Its limited production run of just five units adds to its rarity, making it highly sought after by racing enthusiasts and collectors worldwide. 🌎

Join my Instagram, there are regular quizzes about cars and automotive news📱

I invite you to my Telegram channel #fyp
"""

youtube_title = '🤣 Funniest Memes & Viral Fails 2024! 😂 #Shorts'
youtube_description = """Get ready to laugh out loud with the funniest memes and epic fails of 2024! 😂🔥 

Don't forget to subscribe and hit the bell icon to never miss a hilarious video. 

Love our content? Make sure to like, share, and comment on your favorite moments! We upload new videos every day to keep you entertained!

Follow us on other platforms for exclusive content and updates:
Instagram: @SomeShortShots

#Shorts #Funny #Meme #Fails #Humor #Comedy #Entertainment #Laughs
"""
youtube_category = '24'
youtube_keywords = 'Shorts, Funny, Meme, Fails, Humor, Laughs, Comedy, Pranks, Funny videos, Viral clips, 2024 Memes, Epic fails, Hilarious moments, Entertainment'
youtube_privacyStatus = 'public'

def GetRandomFile(relative_folder_path, extension=None):
    # Obtener la ruta absoluta de la carpeta
    absolute_folder_path = os.path.abspath(relative_folder_path)
    
    # Listar todos los archivos en la carpeta, filtrando por extensión si se especifica
    if extension:
        files = [os.path.join(absolute_folder_path, f) for f in os.listdir(absolute_folder_path) 
                 if os.path.isfile(os.path.join(absolute_folder_path, f)) and f.endswith(extension)]
    else:
        files = [os.path.join(absolute_folder_path, f) for f in os.listdir(absolute_folder_path) 
                 if os.path.isfile(os.path.join(absolute_folder_path, f))]
    
    # Seleccionar un archivo al azar
    if not files:
        raise FileNotFoundError(f"No se encontraron archivos con la extensión {extension} en la carpeta {relative_folder_path}")
    
    random_file = random.choice(files)
    return random_file


def UploadToInstagram(sourceVideo):
    try:
        cl = Client()
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

        # Ruta del video y configuración
        video_path = sourceVideo

        # Publicación del reel
        cl.clip_upload(video_path, instagram_caption)

        os.remove(sourceVideo)
        print(f"Instagram: Reel publicado con éxito. {sourceVideo}")
    except:
        print(f"Instagram: Error al publicar el reel. {sourceVideo}")
    
def main():
    # Obtener el directorio del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    

    # - - Instagram - -
    # Construir las rutas absolutas a las carpetas y scripts necesarios
    instagram_folder = os.path.join(script_dir, 'downloads', 'instagram')
    instagram_script = os.path.join(script_dir, 'uploaders', 'uploadIG_instagrapi.py')
    
    try:
        # Obtener un archivo al azar de la carpeta ./downloads/instagram
        random_file = GetRandomFile(instagram_folder, '.mp4')
        print(f"Archivo seleccionado para Instagram: {random_file}")
        UploadToInstagram(random_file)
    except Exception as e:
        print(f"Instagram error: {e}")
    

    # - - Youtube - - 
    youtube_folder = os.path.join(script_dir, 'downloads', 'youtube')
    random_file = GetRandomFile(youtube_folder, '.mp4')
    upload_video_to_youtube(
        file=random_file,
        title=youtube_title,
        description=youtube_description,
        category=youtube_category,
        keywords=youtube_keywords,
        privacyStatus=youtube_privacyStatus
    )
    os.remove(random_file)
    

    #TODO: TikTok

if __name__ == "__main__":
    main()
