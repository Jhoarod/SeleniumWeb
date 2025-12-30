from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def validation():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.google.com")

        input("Presiona ENTER para salir:")
    except:
        pass
    driver.quit()
validation()
