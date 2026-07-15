from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)   # Implicit wait

try:
    print(" Opening YouTube in Brave...")
    driver.get("https://www.youtube.com")
    
    wait = WebDriverWait(driver, 15)
    
    # Wait for search box
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    
    print(" YouTube loaded successfully!\n")
    
    user_input = input("What do you want to search on YouTube?: ").strip()
    
    if user_input:
        print(f" Searching: {user_input}")
        search_box.clear()
        search_box.send_keys(user_input)
        time.sleep(1.5)
        
        # Try to click search button
        try:
            search_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ytSearchboxComponentSearchButton"))
            )
            search_button.click()
            print(" Search button clicked!")
        except:
            search_box.submit()
            print(" Enter pressed!")
        
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contents")))
        print(" Search completed!")
        
except Exception as e:
    print(" Error:", e)
finally:
    time.sleep(8)
    driver.quit()