nomes = []
numeros = []

while True:
    n = input("Digite seu nome: ")
    if n == "0":
        break
    nomes.append(n)
    a = int(input("Digite um numero: "))


for nome, numero in zip(nomes, numeros):
    print("{:<10}{}{:>10}".format(nome, "*" * 10, numero))
