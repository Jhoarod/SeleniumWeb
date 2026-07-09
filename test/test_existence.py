from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def check_button_exists():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.youtube.com")
        wait = WebDriverWait(driver, 10)
        
        # Method 1: Using expected_conditions (Best)
        try:
            button = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "ytSearchboxComponentSearchButton"))
            )
            print(" Button exists!")
        except:
            print(" Button NOT found")
        
    finally:
        time.sleep(10)
        driver.quit()

check_button_exists()