from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def components():# definicion de la funcion
    driver  = webdriver.Chrome()  #seteo de variables
    driver.get("https://google.com")


    try:
        titulo = driver.title
        assert titulo == "Google"
        print("Titulo encontrado")
    except:
        pass

    input("presiona Enter")    
    driver.quit()
    
components()# inovacion de funcion
