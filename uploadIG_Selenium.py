# pip3 install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración del WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Abre Instagram
driver.get("https://www.instagram.com")
driver.fullscreen_window()

# Espera que la página cargue
time.sleep(3)

links = driver.find_elements("xpath", "//button")
for link in links:
    if "Rechazar cookies" in link.get_attribute("innerHTML"):
        print("Rechazar cookies")
        link.click()
        break

time.sleep(5)

# Inicia sesión
try:
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')

    print("Login")
    username.send_keys('someshortshots')
    password.send_keys('gk6PLvQyltFwQrTWd')
    password.send_keys(Keys.RETURN)
except:
    print("Sesión estaba iniciada")

# Espera para que se realice el login
time.sleep(5)

links = driver.find_elements("xpath", "//span")
for link in links:
    if "Crear" in link.get_attribute("innerHTML"):
        print("Crear")
        link.click()
        break


time.sleep(5)

# # Carga el archivo de video
# upload_button = driver.find_element(By.XPATH, '//input[@type="file"]')
# upload_button.send_keys('/path/to/tu_video.mp4')  # Cambia el path a tu video

# # Espera que el video se cargue
# time.sleep(10)

# # Introduce la descripción del Reel (opcional)
# description_area = driver.find_element(By.XPATH, '//textarea[@aria-label="Descripción"]')
# description_area.send_keys('Tu descripción del Reel')

# # Publica el Reel
# share_button = driver.find_element(By.XPATH, '//button[text()="Compartir"]')
# share_button.click()

# # Espera para que la publicación se realice
# time.sleep(5)

# # Cierra el navegador
time.sleep(60)
driver.quit()
