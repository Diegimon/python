def escreva(palavra):
    for letra in palavra:
        print("-", end="")
    print(f"\n{palavra}")
    for letra in palavra:
        print("-", end="")


d = (input("Digite uma palavra: "))
escreva(d)
