# pip3 install instaloader

import instaloader
import requests

def get_instagram_video_url(post_url):
    L = instaloader.Instaloader()
    shortcode = post_url.split("/")[-2]
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    
    if post.is_video:
        return post.video_url
    else:
        return None

def download_video(video_url, output_path):
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
    else:
        print(f"Error al descargar el video: {response.status_code}")

def main(instagram_post_url, output_path):
    video_url = get_instagram_video_url(instagram_post_url)
    if video_url:
        download_video(video_url, output_path)
        print(f"Video descargado y guardado en {output_path}")
    else:
        print("No se pudo encontrar el video o la publicación no contiene un video.")

if __name__ == "__main__":
    # URL de la publicación de Instagram (Reels)
    instagram_post_url = 'https://www.instagram.com/reel/C9MUIP9yxEw/?igsh=Y2t0bXIwZTdlMzRq'
    
    # Ruta completa donde se guardará el video
    output_path = './video.mp4'
    
    main(instagram_post_url, output_path)