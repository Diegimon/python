import random
n = int(input("Quantos jogos você deseja fazer?: "))
lista = list()
jogo = list()


for jg in range(0, n+1):
    lista.append(jogo[:])
    jogo.clear()

    for i in range(0, 6):
        numero = random.randint(0, 60)
        jogo.append(numero)
for j in range(0, n):
    print(f"jogada {j}: {lista[j+1]}")
