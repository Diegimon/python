lista = [[],[]]

for p in range(0, 7):
    n = int(input(f"Digite o {p+1}º listaero: "))
    if n%2==0:
      lista[0].append(n)
    else:
      lista[1].append(n)
print(f"Pares = {lista[0]}\nImpares = {lista[1]}")

