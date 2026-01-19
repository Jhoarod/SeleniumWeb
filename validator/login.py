from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Abrir sitio
        driver.get("https://www.saucedemo.com")

        # 2. Usuario
        username = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")

        # 3. Password
        password = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password.send_keys("secret_sauce")

        # 4. Click login
        login_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_btn.click()

        # 5. Validación
        wait.until(EC.url_contains("inventory"))
        assert "inventory" in driver.current_url

        print(" Login exitoso")

        input("ENTER para cerrar")

    finally:
        driver.quit()

test_login()
