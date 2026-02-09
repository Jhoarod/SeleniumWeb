from selenium import webdriver
from selenium.webdriver.common.by import By
def test_forms():
    driver = webdriver.Chrome
    try:
        driver.get()
    except:
        pass 