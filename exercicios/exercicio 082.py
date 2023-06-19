lista_numero = []
pares = []
impares = []
while True:
    numero = int(input("Digite um numero(0 para sair): "))
    if numero == 0:
        print("progama finalizado")
        break
    lista_numero.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(
    f"Total {lista_numero}\nOs numeros pares ditados são {pares} \nOs numeros impares{impares} ")
