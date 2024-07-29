# Este script solicita la descarga de los reels contenidos en reels.txt

# pip install requests
import requests
import time

# Configura la URL del servidor y el número máximo de líneas a procesar
server_url = 'http://192.168.1.2:3000/getVideo'
max_lines_to_process = 20
input_file = 'reels.txt'

def process_urls():
    with open(input_file, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("El archivo está vacío.")
        return

    # Asegurarse de no procesar más líneas de las que hay en el archivo
    num_lines_to_process = min(max_lines_to_process, len(lines))

    for i in range(num_lines_to_process):
        url = lines[i].strip()
        if url:
            payload = {"URL": url}
            try:
                response = requests.post(server_url, json=payload, verify=False)  # `verify=False` para ignorar SSL
                if response.status_code == 200:
                    print(f"Solicitud POST exitosa para: {url}")
                else:
                    print(f"Error al enviar solicitud POST para: {url}. Código de estado: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error en la solicitud POST para: {url}. Detalles: {e}")

            # Espera 5 segundos antes de procesar la siguiente URL
            time.sleep(10)

    # Reescribir el archivo sin las líneas procesadas
    with open(input_file, 'w') as file:
        file.writelines(lines[num_lines_to_process:])

if __name__ == "__main__":
    process_urls()
