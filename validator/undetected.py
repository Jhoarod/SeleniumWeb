from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

"""
uso de undetected chromedriver que es una version 
parchada para engañar los servicios antibots
se instala asi pip install undetected-chromedriver
"""

def main():
    driver = uc.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        
        driver.get('https://google.com')
        wait.until(EC.visibility_of_element_located((By.NAME, "q"))).send_keys("selenium") #envio de credenciales de acceso
        wait.until(EC.element_to_be_clickable((By.NAME, "btnK"))).click()
    except:
        pass
    
    input("ENTER para cerrar el navegador")
if __name__ == "__main__":
    main()