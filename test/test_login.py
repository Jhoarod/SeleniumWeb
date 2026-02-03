from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_con_capturas(driver, take_screenshot):
    wait = WebDriverWait(driver, 10)

 
    driver.get("https://example.com/login")
    take_screenshot("01_pagina_login")

    
    usuario = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    take_screenshot("02_inputs_visibles")

    
    usuario.send_keys("usuario_test")
    password.send_keys("123456")
    take_screenshot("03_credenciales_ingresadas")

   
    driver.find_element(By.ID, "login-btn").click()
    take_screenshot("04_click_login")

    
    mensaje = wait.until(
        EC.visibility_of_element_located((By.ID, "error-msg"))
    )
    take_screenshot("05_resultado_login")

    assert "obligatorios" in mensaje.text.lower()
