from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#create chromeoptions instance
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

#provide location where chrome stores profiles
options.add_argument(r"--user-data-dir=/Users/briancarrillo/Library/Application Support/Google/Chrome/Default")

#provide the profile name with which we want to open browser
options.add_argument(r'--profile-directory=Brian')

#specify where your chrome driver present in your pc
driver = webdriver.Chrome(options=options)

#provide website url here
driver.get("https://youtube.com/")

#find element using its id
print(driver.find_element("id","home").text)