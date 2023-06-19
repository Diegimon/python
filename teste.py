from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ano = 2023
anos = []
resultado = []
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)
nav.get('https://www.google.com')
sleep(1)

sleep(1)
nav.find_element(
    "xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').click()
nav.find_element(
    "xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(f'Resultado da mega sena {ano}')
nav.find_element(
    "xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)
classe = nav.find_element(By.CLASS_NAME, 'MDTDab')
spans = classe.find_elements(By.TAG_NAME, 'span')
print('Executado com sucesso!')
