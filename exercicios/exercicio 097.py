from time import sleep


def add(ini, fim, inter):
    lista = list()
    if inter == 0:
        inter = 1
    elif inter < 0:
        if ini < fim:
            x = ini
            ini = fim
            fim = x
    if ini > fim:
        if inter > 0:
            inter = -inter
            fim -= 1
    else:
        fim += 1

    for c in range(ini, fim, inter):
        sleep(0.3)
        print(f"[{c}]", end="")


n = int(input("Digite o inicio: "))
n2 = int(input("Digite o final: "))
n3 = int(input("Digite o intervalo: "))
print(f"Comçando de {n} até {n2} de {n3} em {n3}")
print('=*'*30)
add(n, n2, n3)
print("")
print('=*'*30)
