def fatorial(num, show=False):
    from time import sleep
    ft = []
    fato = 1
    for i in range(1, num+1):
        fato *= i
        ft.append(fato)
    print(f"O faotiral de {num} é {fato}")
    if show == True:
        for n in ft:
            print(f"[{n}]", end="=")
            sleep(0.2)


print("=_"*10, "Calculo fatorial", "=_"*10)
n = int(input("Digite o numero que deseja saber o fatorial: "))
ver = input("Você deseja vizualizar a sequencia do fatorial? [1]sim [2]não\n:")
if ver == "1":
    fatorial(n, True)
elif ver == "2":
    fatorial(n)
else:
    print("Escolha invalida")
