padrao = '\033[0m'


def voto(ano):
    import datetime
    verde = '\033[0;49;32m'
    vermelho = '\033[0;49;91m'
    obrigado = False
    pode = False
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano
    if idade >= 16 and idade < 18:
        pode = True
    elif idade >= 18 and idade < 70:
        obrigado = True
        pode = True
    if pode == True:
        if obrigado == True:
            print(f"Com {idade} anos o voto é {vermelho}obrigatório ")
        else:
            print(f"Com {idade} anos o voto é {verde}opcional")

    else:
        print(f"{vermelho}Você não possui os requisistos para votar")


print(f"{padrao}Validação de voto")
ano = int(input("Digite o ano de nascimento desta pessoa: "))
voto(ano)
