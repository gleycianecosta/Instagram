from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import time


class instaBot:
    def __init__(self):
    # navegar para a página de login do Instagram
      
        firefox_options = Options()
        firefox_options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\devgl\\OneDrive\\Área de Trabalho\\geckodriver\\geckodriver.exe", options=firefox_options)
        self.driver.get("https://www.instagram.com/accounts/login/")

    # espera para página carregar
        time.sleep(2)    
    # preencher campos de login    
    def login(self):    
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        username_field.send_keys('SEU_USUÁRIO')
        password_field.send_keys('SUA_SENHA')
    # envia o formulário
        password_field.submit()
    # espera o processo de login completar
        time.sleep(19)  

        self.curtir_fotos('pitmonster')

    # Navegar até a página DA HASHTAG
    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 3):   
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        #total de fotos carregadas    
        hrefs = driver.find_elements(By.TAG_NAME, 'a')
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs] 
        (href for href in pic_hrefs if hashtag in href)
        print(hashtag + ' fotos ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element(By.CLASS_NAME,'_abl-').click()
                time.sleep(19)
            except Exception as e:
                time.sleep(5)    


devBot = instaBot()
devBot.login()
