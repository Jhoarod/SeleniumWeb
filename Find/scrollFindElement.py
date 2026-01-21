from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://ejemplo.com")

wait = WebDriverWait(driver, 10)

# Espera a que el elemento exista en el DOM
elemento = wait.until(
    EC.presence_of_element_located((By.ID, "id_del_elemento"))
)

# Hace scroll hasta el elemento
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elemento)

# Ejemplo de acción
elemento.click()
