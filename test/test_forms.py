from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_forms(take_screenshot):
    driver = webdriver.Chrome()
    wait= WebDriverWait(driver, 10)

    try:
        driver.get("https://kick.com")
        take_screenshot("01_pagina_login")
    except:
        pass 
    driver.quit()