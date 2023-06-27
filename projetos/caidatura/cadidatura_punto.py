import os
from random import randint
from openpyxl import Workbook, load_workbook

planilha = None

# Função para criar a planilha


def criar_planilha():
    # Verifica se a planilha já existe
    if os.path.exists("planilha.xlsx"):
        print("Planilha already exists")
        return
    
    # Cria uma nova planilha
    planilha = Workbook()

    # Seleciona a planilha ativa
    planilha_ativa = planilha.active

    # Define os títulos das colunas
    planilha_ativa["A1"] = "Name"
    planilha_ativa["B1"] = "Password"
    planilha_ativa["C1"] = "Account"
    planilha_ativa["D1"] = "Balance"

    # Exemplo de dados
    dados = [
        ["Pedro Fernández", "123456", "PD201819HASRTR07", 1],
        ["Juan Pérez", "abcdef", "JP201819HASRTR06", 1],
        ["Pepito Limón", "qwerty", "PL211819HASRTR06", 1]
    ]

    # Preenche as células com os dados
    for linha, registro in enumerate(dados, start=2):
        planilha_ativa.cell(row=linha, column=1).value = registro[0]  # Name
        planilha_ativa.cell(row=linha, column=2).value = registro[1]  # Password
        planilha_ativa.cell(row=linha, column=3).value = registro[2]  # Account
        planilha_ativa.cell(row=linha, column=4).value = registro[3]  # Balance
    
    # Salva a planilha em um arquivo
    planilha.save("planilha.xlsx")

    # Cria a planilha "history" e preenche as colunas com os dados da coluna "Account"
    history = planilha.create_sheet(title="History")
    accounts = [registro[2] for registro in dados]  # Extrai os números de conta
    for coluna, account in enumerate(accounts, start=1):
        history.cell(row=1, column=coluna).value = account

    # Salva as alterações no arquivo
    planilha.save("planilha.xlsx")

    print("Planilhas created successfully.")



# Função para exibir o menu


def menu():
    valid = ["1", "2", "3"]
    m = input("[1] Create Account\n[2] Login\n[3] Close\n: ")
    while m not in valid:
        print("Invalid option!")
        m = input("[1] Create Account\n[2] Login\n[3] Close\n: ")
    return m

# Função para criar uma conta


def create_account():
    print("Create Account with your data")
    while True:
        name = input("Full name: ")

        # Verificar se o name contém apenas letras
        if not name.isalpha():
            print("Invalid name! The name must contain only letters!")
            continue

        # Verificar se o name possui pelo menos um name
        elif len(name.split()) < 1:
            print("Invalid name! Enter at least one name")
            continue

        # name válido
        break

    while True:
        password = input("Enter your password: ")
        confirm = input("Confirm Password: ")
        if password != confirm:
            print("Password confirmation incorrect")
        elif password.strip() == '':
            print("Invalid password")
        else:
            account = randint(1000000000, 9999999999)
            print("ID generated")
            break

    first_deposit = True  # Variável de controle
    while True:
        if first_deposit:
            r = input(
                "Do you want to enter the first deposit of the account? [y/n]: ")
            if r == 'y':
                while True:
                    balance = float(input("Deposit amount: "))
                    if balance < 1:
                        print("Invalid value!")
                    else:
                        first_deposit = False  # Atualiza a variável de controle
                        break
            elif r == 'n':
                balance = 1
                break
            else:
                print("Invalid value!")
        else:
            
            break

    planilha = load_workbook("planilha.xlsx")
    planilha_ativa = planilha.active

    # Consulta a última linha ocupada na planilha
    ultima_linha = planilha_ativa.max_row

    # Insere os dados da nova conta na próxima linha vazia
    nova_linha = ultima_linha + 1
    planilha_ativa.cell(row=nova_linha, column=1).value = name
    planilha_ativa.cell(row=nova_linha, column=2).value = password
    planilha_ativa.cell(row=nova_linha, column=3).value = account
    planilha_ativa.cell(row=nova_linha, column=4).value = balance

    # Salva as alterações na planilha
    planilha.save("planilha.xlsx")
    
    # Adicionar ao histórico
    if "History" not in planilha.sheetnames:
        planilha.create_sheet("History")  # Cria a planilha "history" se não existir
    
    planilha_history = planilha["History"]
    ultima_coluna = planilha_history.max_column

    nova_coluna = ultima_coluna + 1

    planilha_history.cell(row=1, column=nova_coluna).value = account
    planilha_history.cell(row=2, column=nova_coluna).value = "account created"

    planilha.save("planilha.xlsx")

    print(f"Account created successfully!")



# Função para preencher o history
from openpyxl import load_workbook

def update_history(column_title, value):
    planilha = load_workbook("planilha.xlsx")
    planilha_history = planilha["History"]

    # Procura o título da coluna na primeira linha
    coluna = None
    for cell in planilha_history[1]:
        if cell.value == column_title:
            coluna = cell.column_letter
            break

    if coluna is None:
        print(f"Column '{column_title}' not found in the 'history' sheet.")
        return

    # Obtém a última linha ocupada na coluna
    ultima_linha = planilha_history.max_row

    # Atualiza o valor na última linha da coluna
    planilha_history[f"{coluna}{ultima_linha}"] = value

    # Salva as alterações no arquivo
    planilha.save("planilha.xlsx")

    print(f"Value '{value}' added to column '{column_title}' in the 'history' sheet.")



# Função para validar o login
def validate_login(name, password):
    planilha = load_workbook("planilha.xlsx")
    planilha_ativa = planilha.active

    for linha in planilha_ativa.iter_rows(min_row=2, values_only=True):
        account_name, account_password, account_number, account_balance = linha

        if account_name == name and account_password == password:
            return account_number, account_balance

    return None, None

# Função para realizar um depósito


def deposit_amount(account_number):
    planilha = load_workbook("planilha.xlsx")
    planilha_ativa = planilha['Sheet']

    linhas_atualizadas = []
    for linha in planilha_ativa.iter_rows(min_row=2, values_only=True):
        current_account_number = linha[2]  # Número da conta na planilha

        if current_account_number == account_number:
            current_balance = linha[3]  # Saldo atual da conta
            deposit = float(input("Enter the deposit amount: "))
            new_balance = current_balance + deposit

            linha_atualizada = list(linha)
            linha_atualizada[3] = new_balance  # Atualiza o saldo na linha
            linhas_atualizadas.append(linha_atualizada)
        else:
            linhas_atualizadas.append(list(linha))

    # Remove todas as linhas existentes
    planilha_ativa.delete_rows(2, planilha_ativa.max_row)

    # Adiciona as linhas atualizadas
    for linha_atualizada in linhas_atualizadas:
        planilha_ativa.append(linha_atualizada)
    reg = (f'deposit of {deposit} reais made')
    update_history(account_number,reg)

    planilha.save("planilha.xlsx")

    print("Deposit successfully!")


# Função para realizar um saque
def withdrawal_amount(account_number):
    planilha = load_workbook("planilha.xlsx")
    planilha_ativa = planilha['Sheet']

    linhas_atualizadas = []
    for linha in planilha_ativa.iter_rows(min_row=2, values_only=True):
        current_account_number = linha[2]  # Número da conta na planilha

        if current_account_number == account_number:
            current_balance = linha[3]  # Saldo atual da conta
            withdrawal = float(input("Enter the withdrawal amount: "))
            if withdrawal > current_balance:
                print("Insufficient funds!")
                return
            new_balance = current_balance - withdrawal

            linha_atualizada = list(linha)
            linha_atualizada[3] = new_balance  # Atualiza o saldo na linha
            linhas_atualizadas.append(linha_atualizada)
        else:
            linhas_atualizadas.append(list(linha))

    # Remove todas as linhas existentes
    planilha_ativa.delete_rows(2, planilha_ativa.max_row)

    # Adiciona as linhas atualizadas
    for linha_atualizada in linhas_atualizadas:
        planilha_ativa.append(linha_atualizada)

    planilha.save("planilha.xlsx")
    reg = (f'Loot of {withdrawal} reais successfully carried out!')
    update_history(account_number,reg)

    print("Withdrawal successfully!")


def delete_account(account_number):
    planilha = load_workbook("planilha.xlsx")
    planilha_ativa = planilha.active

    linhas_atualizadas = []
    for linha in planilha_ativa.iter_rows(min_row=2, values_only=True):
        current_account_number = linha[2]  # Número da conta na planilha

        if current_account_number != account_number:
            linhas_atualizadas.append(list(linha))

    # Remove todas as linhas existentes
    planilha_ativa.delete_rows(2, planilha_ativa.max_row)
    planilha.save("planilha.xlsx")
    print("Account deleted successfully!")

# Função para exibir o menu e retornar a opção escolhida


def menu():
    valid = ["1", "2", "3"]
    m = input("[1] Create Account\n[2] Login\n[3] Close\n: ")
    while m not in valid:
        print("Invalid option!")
        m = input("[1] Create Account\n[2] Login\n[3] Close\n: ")

    return m

# Função principal


def main():
    criar_planilha()
    while True:
        m = menu()
        if m == '1':
            create_account()
        elif m == '2':
            print("Login to your account")
            name = input("Name: ")
            password = input("Password: ")

            account_number, account_balance = validate_login(name, password)

            if account_number:
                print("Login successful!")
                print("Account Information:")
                print("Name:", name)
                print("Account:", account_number)
                print("Balance:", account_balance)

                while True:
                    print("=" * 20)
                    menu_option = input(
                        "[1] Deposit\n[2] Withdrawal\n[3] History\n[4] Delete\n[5] Close\n: ")

                    if menu_option == '1':
                        deposit_amount(account_number)
                    elif menu_option == '2':
                        withdrawal_amount(account_number)
                    elif menu_option == '3':
                        show_history(account_number)
                    elif menu_option == '4':
                        delete_account(account_number)
                        break
                    elif menu_option == '5':
                        break
                    else:
                        print("Invalid option!")
            else:
                print("Login failed! Invalid name or password.")
        elif m == '3':
            break


main()
