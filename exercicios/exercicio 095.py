def area(l, c):
    area = l*c
    print(f"A area do terreno é  {area:.0f}m²")


largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
area(largura, comprimento)
