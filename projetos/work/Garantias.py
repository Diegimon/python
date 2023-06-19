# %%
import win32com.client as win32
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# ================================= cores =================================
padrao = '\033[0m'
verde = '\033[0;49;32m'
vermelho = '\033[0;49;91m'
amarelo = '\033[1;49;33m'
azul = '\033[0;49;34m'
# ==================================================================
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)
modelo = int(
    input("Qual o modelo do certificado \n[1]A1\n[2]A3\n[3]A3-SafeID\n: "))
if modelo == 1:
    driver = "////////"
elif modelo == 2:
    dv = int(
        input(f"{amarelo}Qual o driver do certificado \n[1]SafeSing\n[2]SafeNet\n[3]AWP manager\n: {padrao}"))
    if dv == 1:
        driver = "SafeSing"
        print(verde, f"{driver} Selecionado", padrao)
    elif dv == 2:
        driver = "SafeNet"
        print(verde, f"{driver} Selecionado", padrao)
    elif dv == 3:
        driver = "AWP-Manager"
        print(verde, f"{driver} Selecionado", padrao)
    else:
        driver = f"{vermelho}Não inserido {padrao}"
elif modelo == 3:
    print("modelo certificado em nuvem selecionado")
else:
    while modelo != 1 or modelo != 2 or modelo != 3:
        print("Escolha invalida")
        modelo = int(
            input("Qual o modelo do certificado \n[1]A1\n[2]A3\n[3]A3-SafeID\n: "))


Motivo = input("Motivo da garantia: ")
protocolo = int(input("Protocolo da garantia: "))


# %%
# ======== Abrindo Gerenciamento ========
print("Abrindo gerenciamento")
print(
    f"Atenção!\n{vermelho}Faça o login com seu certificado antes de prosseguir{padrao}")
nav.get("https://acconsulti.safewebpss.com.br/gerenciamentoac/#/pages/relatorios/relatorio-emissao")
print("Aguardando login com o certificado...")
sleep(5)
valida = input("Tecle [enter] quando terminar de carregar\n: ")

# %%
#  abre o relatorio de emissão
print("Abrindo relátorio de emissão")
nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/app-sidebar/div/app-vertical-menu/div/div[1]/div/div/div[3]/a/span').click()

# %%
# insere o protocolo
print("Inserindo protocolo...")
nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[4]/div[1]/input').send_keys(protocolo)
sleep(5)

# %%
# pesquisando
print("Pesquisando...")
nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[9]/div/div/div/button[1]').click()
sleep(5)
# %%
# ===== Abrindo dados do certificado =====
print("Abrindo informações do certificado...")
nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-lista/form/div/div/div[2]/table/tbody/tr/td[2]/i[1]').click()
sleep(10)

# %%
# ===== Indentificando dados ====
print("Coletando dados...")
produto_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[1]/div[3]/input')

ambiente_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[1]/div[1]/input')

razao_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[3]/div[1]/input')

doc_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[3]/div[2]/input')

nome_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[3]/div[3]/input')

cpf_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[3]/div[4]/input')

email_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[4]/div[1]/input')

nascimento_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[4]/div[4]/input')
fone_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[4]/div[2]/input')
# ==================================================== endereço ===============================================
endereco_busca = []
endereco = []
endereco_longra = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[5]/div[1]/input')
endereco_busca.append(endereco_longra)

endereco_num = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[5]/div[2]/input')
endereco_busca.append(endereco_num)

endereco_complemento = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[6]/div[2]/input')
endereco_busca.append(endereco_complemento)

endereco_bairro = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[5]/div[3]/input')
endereco_busca.append(endereco_bairro)

endereco_municipio = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[6]/div[3]/input')
endereco_busca.append(endereco_municipio)

endereco_estado = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[6]/div[4]/input')
endereco_busca.append(endereco_estado)

endereco_CEP = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[6]/div[1]/input')
endereco_busca.append(endereco_CEP)
# ==============================================================================================================
tipo_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[1]/div[2]/div[2]/div[3]/input')

inicio_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[2]/div[2]/div/div[2]/input')

fim_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[2]/div[2]/div/div[3]/input')

avp_busca = nav.find_element(
    'xpath', '/html/body/app-root/div/div/app-pages/div[1]/div/div/ng-component/app-relatorio-emissao-gestao/form/div/div/div[3]/div[2]/div[2]/div[1]/input')


print(f"{verde}Informações coletadas com sucesso!! {padrao}")

sleep(0.5)
# %%
# ===== Tratamento de strings =====
print("Tratando strings...")

produto = produto_busca.get_attribute('value')
ambiente = ambiente_busca.get_attribute('value')
razao = razao_busca.get_attribute('value')
doc = doc_busca.get_attribute('value')
nome = nome_busca.get_attribute('value')
cpf = cpf_busca.get_attribute('value')

for e in endereco_busca:
    x = e.get_attribute('value')
    endereco.append(x)
endereco_completo = f"""
Rua: {endereco[0]} numero: {endereco[1]} Complemento: {endereco[2]} Bairro:  {endereco[3]}
municipio: {endereco[4]} estado: {endereco[5]} CEP {endereco[6]}
"""


email = email_busca.get_attribute('value')
nascimento = nascimento_busca.get_attribute('value')
fone = fone_busca.get_attribute('value')
tipo = tipo_busca.get_attribute('value')
inicio = inicio_busca.get_attribute('value')
fim = fim_busca.get_attribute('value')
avp = avp_busca.get_attribute('value')


# ===== Montando garantia =====


garantia = f"""{azul}Modelo do certificado (produto):{produto}
Ambiente: {ambiente}
Protocolo (anterior da garantia): {protocolo}
Razão social/Nome: {razao}
CNPJ/CPF: {doc}

Dados do cliente (titular).:
Nome completo: {nome}
CPF: {cpf}
E-mail: {email}
Data de nascimento: {nascimento}
Telefone de contato: {fone}
Endereço: {endereco_completo}
Tipo de emissão: {tipo}
Motivo da garantia: {Motivo}
Data de Início de Validade: {inicio}
Data de Fim de Validade: {fim}
Drive: {driver}
E-mail do AVP: {avp}{padrao}
"""
print("=="*25)
print(garantia)
print("=="*25)

# %%
# Enviar email
print("Enviando email...")
outlook = win32.Dispatch("Outlook.Application")

# criação do objeto email
email = outlook.CreateItem(0)
# email.To = "diegodestroier@hotmail.com"
email.To = "olmir.severo@consultibrasil.com.br"
email.Subject = "Garantia de certificado"
email.HTMLBody = f"""

<p>=====================================================================<br>
Modelo do certificado (produto):{produto}<br>
Ambiente: {ambiente}<br>
Protocolo (anterior da garantia):{protocolo} <br>
Razão social/Nome: {razao}<br>
CNPJ/CPF: {doc}<br>
====================================Dados do cliente (titular)↓.: <br>
Nome completo: {nome}<br>
CPF: {cpf}<br>
E-mail: {email}<br>
Data de nascimento: {nascimento} <br>
Telefone de contato: {fone}<br>
endereço: {endereco}<br>
Tipo de emissão: {tipo}<br>
Motivo da garantia: {Motivo}<br>
Data de Início de Validade: {inicio}<br>
Data de Fim de Validade: {fim}<br>
Drive: {driver}<br>
E-mail do AVP: {avp}</p>
=====================================================================
"""

# enviar o email
email.Send()

# fechar a aplicação Outlook
outlook.Quit()
print(f"{verde}Email enviado com sucesso!{padrao}")

# %%
print("Encerrando programa ")
for c in range(0, 5):
    print(c,)
    sleep(0.3)
print("Programa encerrado!")
encerra = input("Tecle [enter] para encerrar")
sleep(1)
