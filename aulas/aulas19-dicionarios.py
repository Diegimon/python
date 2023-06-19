estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input("Qual unidade federativa: "))
    estado['Nome: '] = str(input("Digite o nome do estado: "))
    brasil.append(estado.copy())
print(brasil)
