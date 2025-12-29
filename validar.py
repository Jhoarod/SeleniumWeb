from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.google.com")

input("Presiona ENTER para salir:")
driver.quit()