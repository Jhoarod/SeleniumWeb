from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_youtube_and_search():
    """
    Opens YouTube and asks the user what to search.
    """
    options = Options()
    options.add_argument("--start-maximized")
 
    # options.add_argument("--headless=new")


    driver = webdriver.Chrome( options=options)
    
    try:
        print(" Opening YouTube...")
        driver.get("https://www.youtube.com")
        
        wait = WebDriverWait(driver, 12)
        
        # Wait for search box
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        
        print(" YouTube loaded successfully!\n")
        
        # === Ask user inside the function and inside try ===
        user_input = input("What do you want to search on YouTube?: ").strip()
        
        if user_input:
            print(f" Searching for: {user_input}")
            
            search_box.clear()
            search_box.send_keys(user_input)
            
            # Click the real search button
            search_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ytSearchboxComponentSearchButton"))
            )
            search_button.click()
            
            print(" Search button clicked!")
            
            # Wait for results to load
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contents")))
            print(" Search results loaded!")
        else:
            print("No search term entered. Opening YouTube homepage.")
        
    except Exception as e:
        print(" Error occurred:", e)
    
    finally:
        print("\n Keeping browser open for 8 seconds...")
        time.sleep(8)
        driver.quit()


if __name__ == "__main__":
    open_youtube_and_search()