from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def open_youtube(params=None):

    options = Options()
    options.add_argument("--start-maximized")


    driver = webdriver.Chrome(options=options) 
    try:    
        print("abriendo youtube")

        driver.get("https://www.youtube.com/")

        wait= WebDriverWait(driver,10)

        find_box =wait.until(EC.presence_of_element_located((By.NAME,"search_query")))

        print("cargando")

    except Exception as e:
        print("error:",e)

    finally:   
        print("mantener youtube abierto")
        time.sleep(10)
        driver.quit()

if __name__== "__main__":
    open_youtube("tutorial de python")

