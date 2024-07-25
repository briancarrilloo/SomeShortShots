import instaloader
import requests
import os
import argparse
from datetime import datetime
from moveDownload import moveDownload

def get_instagram_video_info(post_url):
    L = instaloader.Instaloader()
    shortcode = post_url.split("/")[-2]
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    
    if post.is_video:
        return post.video_url, post.title
    else:
        return None, None

def download_video(video_url, output_path):
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
    else:
        print(f"Error al descargar el video: {response.status_code}")

def main(instagram_post_url):
    video_url, title = get_instagram_video_info(instagram_post_url)
    if video_url:
        downloads_folder = 'downloads'
        os.makedirs(downloads_folder, exist_ok=True)
        
        # Limpieza del título para que sea un nombre de archivo válido
        if title:
            safe_title = "".join([c if c.isalnum() else "_" for c in title])
        else:
            time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            safe_title = f"IG_{time}"
        
        output_path = os.path.join(downloads_folder, f"{safe_title}.mp4")
        
        download_video(video_url, output_path)
        moveDownload(output_path);
        print(f"Video descargado y guardado {safe_title}.mp4")
    else:
        print("No se pudo encontrar el video o la publicación no contiene un video.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Descargar y convertir un video de YouTube.')
    parser.add_argument('url', type=str, help='URL del video de YouTube que deseas descargar')
    args = parser.parse_args()
    main(args.url)
