from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def findElement():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.google.com")

        search_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        search_input.send_keys("Selenium" + Keys.ENTER)

        wait.until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        input("Presiona ENTER para cerrar...")

    finally:
        driver.quit()

findElement()
