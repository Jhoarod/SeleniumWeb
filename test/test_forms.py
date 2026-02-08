from selenium import webdriver

def test_forms():
    driver = webdriver.Chrome
    try:
        driver.get()
    except:
        pass 