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


def RunUploader(relative_script_path, file_path):
    # Obtener la ruta absoluta del script
    absolute_script_path = os.path.abspath(relative_script_path)
    
    # Ejecutar el script con el archivo seleccionado como parámetro
    result = subprocess.run(['python', absolute_script_path, file_path], capture_output=True, text=True)
    
    # Imprimir la salida del script
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
def main():
    # - - - - Instagram - - - -
    try:
        # Obtener un archivo al azar de la carpeta ./downloads/instagram
        random_file = GetRandomFile('./downloads/instagram', '.mp4')
        print(f"Archivo seleccionado para Instagram: {random_file}")
        RunUploader('./uploaders/uploadIG_instagrapi.py', random_file)
    except Exception as e:
        print(f"Instagram error: {e}")
    
    #TODO: Youtube
    #TODO: TikTok

if __name__ == "__main__":
    main()  
