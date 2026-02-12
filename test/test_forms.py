from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_forms():
    driver = webdriver.Chrome()
    wait= WebDriverWait(driver, 10)

    try:
        webdriver.Chrome("https://kick.com")
    except:
        pass 
    driver.quit()