from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Opera(options=options)
driver.implicitly_wait(10)

try:
    print(" Opening YouTube in Opera...")
    driver.get("https://www.youtube.com")
    
    wait = WebDriverWait(driver, 15)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    
    print(" YouTube loaded successfully!\n")
    
    user_input = input("What do you want to search on YouTube?: ").strip()
    
    if user_input:
        search_box.clear()
        search_box.send_keys(user_input)
        time.sleep(1.5)
        search_box.submit()
        
        print(" Search completed!")
        
except Exception as e:
    print(" Error:", e)
finally:
    time.sleep(8)
    driver.quit()