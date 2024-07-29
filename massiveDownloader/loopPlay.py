import subprocess
import time
import random

# Define el comando que deseas ejecutar
command = 'python3 IG_reels_play.py'
iterations = 1200

time.sleep(10)
# Ejecuta el comando X veces
for i in range(iterations):
    print(f'Ejecutando el comando {i+1}/{iterations}')
    subprocess.run(command, shell=True)
    time.sleep(random.uniform(0.5, 2.5))
