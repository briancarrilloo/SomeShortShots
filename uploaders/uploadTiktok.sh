#!/bin/bash
# Nombre del script: tu_script.sh

echo "Script ejecutado en: $(date)" >> /home/briancarrillo/SomeShortShots/uploaders/play.log
source /home/briancarrillo/SomeShortShots/downloaderEnv/bin/activate
cd /home/briancarrillo/SomeShortShots/uploaders
python3 play_Tiktok_Upload.py >> /home/briancarrillo/SomeShortShots/uploaders/play.log 2>&1
echo "Script finalizado en: $(date)" >> /home/briancarrillo/SomeShortShots/uploaders/play.log
