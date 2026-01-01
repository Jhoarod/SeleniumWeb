from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_test(): # definicion de la funcion
    driver = webdriver.Chrome() #seteo de variables
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.saucedemo.com") #acceder a la url

        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user") #envio de credenciales de acceso
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()


        wait.until(EC.url_contains("inventory")) #exception de acceso a inventario
        print("Login exitoso")
        
        input("ENTER para cerrar")

    finally:
        driver.quit()

login_test()
