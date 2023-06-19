from random import randint


def sorteio():
    lista = []
    for i in range(0, 5):
        sorte = randint(0, 5)
        lista.append(sorte)
    print(f"Foram sorteados os numeros: {lista}")
    return lista


def soma_par(l):
    pares = []
    for n in l:
        if (n % 2) == 0:
            pares.append(n)
    soma = sum(pares)
    print(
        f"Os numeros pares obtidos são {pares}\nA soma dos valores é [{soma}]")


n = sorteio()
soma_par(n)
