from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "loginBtn"))).click()

    def validate_error_contains(self, expected_text):
        try:
            error = self.wait.until(
                EC.visibility_of_element_located((By.ID, "errorMessage"))
            )
            assert expected_text.lower() in error.text.lower()
            return True
        except (TimeoutException, AssertionError):
            return False

    def enter_userid(self, userid):
        field = self.wait.until(EC.presence_of_element_located((By.ID, "userid")))
        field.clear()
        field.send_keys(userid)

    def enter_password(self, password):
        field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        field.clear()
        field.send_keys(password)
