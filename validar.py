from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def validation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.google.com")

        input("Presiona ENTER para salir:")

    except TimeoutException:
        print("ERROR: El elemento no apareció dentro del tiempo esperado")

    except Exception as e:
        print(f" ERROR inesperado: {e}")

    finally:
        driver.quit()
        print("Navegador cerrado correctamente")

validation()
