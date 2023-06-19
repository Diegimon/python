lista = list()
maior = menor = []
while True:
    dado = []
    dado.append(str(input("Digite o nome da pessoa: ")))

    if dado[0] == "" or dado[0] == " ":
        break

    dado.append(int(input("Digite o peso da pessoa: ")))

    if not lista:
        maior = menor = dado[:]
    else:
        if dado[1] > maior[1]:
            maior = dado[:]
        elif dado[1] < menor[1]:
            menor = dado[:]

    lista.append(dado[:])

print(lista)
print(f"O mais pesado é {maior[0]} com {maior[1]} kg")
print(f"O mais leve é {menor[0]} com {menor[1]} kg")
print(f"Foi cadastrado um total de {len(lista)} pessoas")
