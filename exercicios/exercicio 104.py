def verifica(n):
    numero = n
    if numero.isdigit():
        numero_inteiro = int(numero)
        print("O número inserido é inteiro.")
    else:
        print("O número inserido não é inteiro.")


numero = input("Digite um número inteiro: ")
verifica(numero)
