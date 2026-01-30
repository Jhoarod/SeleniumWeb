from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración básica 
options = Options()
options.add_argument("--start-maximized")          

driver = webdriver.Chrome(options=options)

url = "https://www.Rustdesk.com"          

driver.get(url)

try:
    
    accept_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    accept_button.click()
    print("¡Cookies aceptadas!")

except Exception as e:
    print("No se encontró o no se pudo clickear el botón de cookies.",e)

   
time.sleep(4)

print("Título de la página después de aceptar cookies:", driver.title)


driver.quit()