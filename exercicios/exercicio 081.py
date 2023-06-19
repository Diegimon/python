numero_lista = []
while True:
    numero = int(input("Digite um numero(0 para sair): "))
    if numero == 0:
        print("progama encerrado")
        break
    else:
        numero_lista.append(numero)
print(sorted(numero_lista, reverse=True))
