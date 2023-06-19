def encontrar_maior(*lista):
    cont = 0
    maior = lista[0]
    for i in lista:
        cont += 1
        if i > maior:
            maior = i
    print(f"Foram passados {cont} numeros e o maior é {maior}")


lista = []
while True:
    n = float(input("Digite o numero que deseja inserir [0]sair: "))
    if n == 0:
        break
    else:
        lista.append(n)
print(f"Lista = {lista}")
encontrar_maior(*lista)
