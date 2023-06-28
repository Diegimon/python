from openpyxl import load_workbook


def validate_credentials(name, password):
    workbook = load_workbook("planilha.xlsx")
    sheet_main = workbook['main']

    # Procurar na primeira coluna (nome)
    for row in sheet_main.iter_rows(min_row=2, min_col=1, max_col=1, values_only=True):
        if row[0] == name:
            # Obter o índice da linha correspondente
            row_index = row[0].row

            # Procurar na segunda coluna (senha)
            for cell in sheet_main.iter_cols(min_row=row_index, max_row=row_index, min_col=2, max_col=2, values_only=True):
                if cell[0] == password:
                    print("Credenciais válidas")
                    return True
                else:
                    print("Senha incorreta")
                    return False

    # Se não encontrar o nome fornecido
    print("Nome de usuário não encontrado")
    return False


# Exemplo de uso
name = input("Nome de usuário: ")
password = input("Senha: ")
validate_credentials(name, password)
