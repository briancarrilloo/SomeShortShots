from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

mail_address = 'bcarrillo2302'
password = '123458'

# Configura las opciones de Chrome para modo headless
options = Options()
options.add_argument('--headless')  # Ejecuta Chrome en modo headless
options.add_argument('--disable-gpu')  # Desactiva la GPU (puede ser necesario en algunas configuraciones)
options.add_argument('--no-sandbox')  # Soluciona problemas de permisos en entornos aislados

# Inicializa el WebDriver de Chrome con las opciones configuradas
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navega a la página de inicio de sesión de Google
url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.co.jp/'
driver.get(url)

# Encuentra y completa los campos de inicio de sesión
driver.find_element(By.ID, "identifierId").send_keys(mail_address)
driver.find_element(By.ID, "identifierNext").click()

# Espera hasta que el campo de la contraseña esté disponible
driver.implicitly_wait(10)  # Espera hasta 10 segundos si es necesario

driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.ID, "passwordNext").click()

# Aquí puedes agregar más código para interactuar con la página después de iniciar sesión

# Cierra el navegador
driver.quit()
