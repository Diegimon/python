class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura


c1 = ControleRemoto('preto', '10cm', '2cm', '2cm')
c2 = ControleRemoto('verde', '5cm', '2cm', '2cm')
print("Printando caracteristicas...")
for d in c1.__dict__.values():
    print(d)
