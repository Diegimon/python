numeros_lista = []
nomes_lista = []
while True:
    pessoa = input("Digite o nome: ")
    numero = int(input("Digite um número: "))
    if pessoa == "0":
        print("Progama encerrado")
        break
    if numero in numeros_lista:
        print(f"O número de {pessoa} já está cadastrado!")
    else:
        print(f"{pessoa} Cadastrado com sucesso!")
        numeros_lista.append(numero)
        nomes_lista.append(pessoa)

for numero, nome in zip(numeros_lista, nomes_lista):
    numero_lista.sort()
    print(f"{nome:<5}{'*'*10}{numero:>5}")
c
