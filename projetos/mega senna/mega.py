# %%
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from collections import Counter
# %%
atual = 2598
anos = []
resultado = []
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)
while atual >= 2551:
    print('Abrindo google')
    nav.get('https://www.google.com')
    sleep(1)
    print('Clicando na barra de pesquisa')

    nav.find_element(
        "xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').click()
    print(f'inserindo pesquisa {atual}')
    nav.find_element(
        "xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(f'Resultado da mega sena concurso {atual}')
    print('Pressionando enter')
    nav.find_element(
        "xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)
    print('Procurando primeiro resultado da pesquisa')
    classe = nav.find_element(By.CLASS_NAME, 'MDTDab')
    spans = classe.find_elements(By.TAG_NAME, 'span')
    i = 0
    for span in spans:
        resultado.append(span.text)
        i += 1
    print(f'Salvando resultado {i}')

    anos.append(resultado.copy())
    resultado.clear()
    atual -= 1

# %%
print('Encerrando navegador')
nav.quit()
print("Iniciando analise de dados...")

tot = []
for jogo in anos:
    tot += jogo
print(tot)
contagem = Counter(tot)
repetidos = [numero for numero, ocorrencias in contagem.items()
             if ocorrencias > 1]
nao_repetidos = tot - repetidos

print("Números repetidos:", repetidos)
print("Números não repetidos:", nao_repetidos)
# %%
