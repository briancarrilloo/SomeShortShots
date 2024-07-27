import os
import random
import subprocess

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


def RunUploader(script_path, file_path):
    # Ejecutar el script con el archivo seleccionado como parámetro
    result = subprocess.run(['python', script_path, file_path], capture_output=True, text=True)
    
    # Imprimir la salida del script
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
def main():
    # Obtener el directorio del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construir las rutas absolutas a las carpetas y scripts necesarios
    instagram_folder = os.path.join(script_dir, 'downloads', 'instagram')
    instagram_script = os.path.join(script_dir, 'uploaders', 'uploadIG_instagrapi.py')
    
    try:
        # Obtener un archivo al azar de la carpeta ./downloads/instagram
        random_file = GetRandomFile(instagram_folder, '.mp4')
        print(f"Archivo seleccionado para Instagram: {random_file}")
        RunUploader(instagram_script, random_file)
    except Exception as e:
        print(f"Instagram error: {e}")
    
    #TODO: Youtube
    #TODO: TikTok

if __name__ == "__main__":
    main()
