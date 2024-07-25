# pip3 install selenium
# pip3 install pyautogui  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle
import os
import pyautogui

# Configuración del WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Ruta del archivo de cookies
cookies_file = 'instagram_cookies.pkl'

# Función para cargar cookies
def load_cookies(driver, cookies_file):
    if os.path.exists(cookies_file):
        driver.get("https://www.instagram.com")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.fullscreen_window()

# Función para guardar cookies
def save_cookies(driver, cookies_file):
    cookies = driver.get_cookies()
    pickle.dump(cookies, open(cookies_file, "wb"))

# Abre Instagram
driver.get("https://www.instagram.com")
driver.fullscreen_window()

# Espera que la página cargue
time.sleep(3)

# Rechaza cookies si es necesario
links = driver.find_elements(By.XPATH, "//button")
for link in links:
    if "Rechazar cookies" in link.get_attribute("innerHTML"):
        print("Rechazar cookies")
        link.click()
        time.sleep(3)
        break


# Cargar cookies si existen
load_cookies(driver, cookies_file)

# Verifica si es necesario iniciar sesión
try:
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')

    print("Login")
    username.send_keys('someshortshots')
    password.send_keys('gk6PLvQyltFwQrTWd')
    password.send_keys(Keys.RETURN)

    # Espera para que se realice el login
    time.sleep(5)

    # Guarda las cookies después de iniciar sesión
    save_cookies(driver, cookies_file)
except Exception as e:
    print("Skip login")

# Navega a la página de creación de contenido
links = driver.find_elements(By.XPATH, "//span")
for link in links:
    if "Crear" in link.get_attribute("innerHTML"):
        print("Crear")
        link.click()
        break

time.sleep(5)

# Carga el archivo de video
links = driver.find_elements(By.XPATH, "//button")
for link in links:
    if "Seleccionar del ordenador" in link.get_attribute("innerHTML"):
        print("Seleccionar del ordenador")
        link.click()
        break

time.sleep(3)

# Mapea cada carácter a una combinación de teclas si es necesario
def type_path(path):
    for char in path:
        if char == '/':
            pyautogui.keyDown('shift')
            pyautogui.press('7')
            pyautogui.keyUp('shift')
        else:
            pyautogui.write(char)

# Usa la función para ingresar la ruta
videopath = '/Usuarios/briancarrillo/Descargas/instagramreel.mp4'
type_path(videopath)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')

# Espera que el video se cargue
time.sleep(3)

# Confirma warning video ahora son reels
links = driver.find_elements(By.XPATH, "//button")
for link in links:
    if "Aceptar" in link.get_attribute("innerHTML"):
        print("Aceptar")
        link.click()
        time.sleep(3)
        break


# Seleccionar recorte
links = driver.find_elements(By.XPATH, "//button")
for link in links:
    if "Seleccionar recorte" in link.get_attribute("innerHTML"):
        print("Seleccionar recorte")
        link.click()
        time.sleep(1)
        break

# Recorte original
links = driver.find_elements(By.XPATH, "//span")
for link in links:
    if "Original" in link.get_attribute("innerHTML"):
        print("Original")
        link.click()
        time.sleep(1)
        break

# Encuentra el <div> con role="button" y el texto "Siguiente"
try:
    button = driver.find_element(By.XPATH, "//div[@role='button' and contains(text(), 'Siguiente')]")
    print("Botón 'Siguiente' encontrado.")
    button.click()
    time.sleep(2)  # Espera después de hacer clic
except Exception as e:
    print("Error al encontrar o hacer clic en el botón:", e)

# Encuentra el <div> con role="button" y el texto "Siguiente"
try:
    button = driver.find_element(By.XPATH, "//div[@role='button' and contains(text(), 'Siguiente')]")
    print("Botón 'Siguiente' encontrado.")
    button.click()
    time.sleep(2)  # Espera después de hacer clic
except Exception as e:
    print("Error al encontrar o hacer clic en el botón:", e)

# time.sleep(200)
# Escribe
# links = driver.find_elements(By.XPATH, "//div")
# for link in links:
#     if "Escribe un pie" in link.get_attribute("innerHTML"):
#         print("Escribe un pie")
#         link.click()
#         time.sleep(0.5)
#         pyautogui.write('Follow for more!')
#         time.sleep(0.5)
#         break

# try:
#     button = driver.find_element(By.XPATH, "//div[@editor='true']")
#     print("Botón 'Escribe un pie' encontrado.")
#     button.click()
#     time.sleep(0.5)  # Espera después de hacer clic
#     pyautogui.write('Follow for more!')
#     time.sleep(0.5)
# except Exception as e:
#     print("Error al encontrar o hacer clic en el botón:", e)

# Compartir
try:
    button = driver.find_element(By.XPATH, "//div[@role='button' and contains(text(), 'Compartir')]")
    print("Botón 'Compartir' encontrado.")
    button.click()
except Exception as e:
    print("Error al encontrar o hacer clic en el botón:", e)

# Cierra el navegador
time.sleep(60)
driver.quit()
