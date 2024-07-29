# Script de python que recibe la URL de un archivo y lo mueve a las distintas carpetas de destino

import os
import shutil
import argparse

# Carpetas de destino
destination_folders = ['originals', 'instagram']

def moveDownload(source_file):
    # Crear las carpetas de destino si no existen y copiar el archivo
    for folder in destination_folders:
        destination_path = os.path.join('downloads', folder)
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        shutil.copy(source_file, destination_path)
    
    # Eliminar el archivo original
    os.remove(source_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copiar archivo a múltiples carpetas y eliminar el original.')
    parser.add_argument('source_file', type=str, help='Ruta del archivo a copiar y eliminar.')
    args = parser.parse_args()

    source_file = args.source_file

    if os.path.exists(source_file):
        moveDownload(source_file)
    else:
        print(f"El archivo {source_file} no existe.")
