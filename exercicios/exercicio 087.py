# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                A) A soma de todos os valores pares digitados.                                                                         B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spa = maior = soma = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f"Digite um valor para tabela[{linha}][{coluna}]: "))
print('*='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}] ", end='')
        if matriz[l][c] % 2 == 0:
            spa += matriz[l][c]
    print()
print('*='*30)
print(f"Soma dos pares {spa}")
for l in range(0, 3):
    soma += matriz[l][2]
print(f"Soma da terceira coluna= {soma}")
print(f"O maior valor da segunda linha = {max(matriz[1])}")
