from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_forms(take_screenshot):
    driver = webdriver.Chrome()
    wait= WebDriverWait(driver, 10)

    try:
        driver.get("https://kick.com")
        take_screenshot("01_pagina_login")
    except:
        pass 
    driver.quit()