lista = []
while True:
    numero = input("Digite um numero: ")
    if numero == "":
        break
    lista.append(numero)
maior = lista[0]
menor = lista[0]
for numero in lista[1:]:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'sua lista é:{lista} ')
print(f'O maior numero é {maior}\nO menor numero é {menor}')
