def ficha(nome, gols):
    if gols == 0:
        print(f"O jogador {nome} não marcou gols")
    else:
        print(f"O jogador {nome} marcou {gols} gols")


nome = input("Nome do jogador: ")
gols = input("Quantos gols ele marcou: ")
if nome == "" or nome == " ":
    nome = "<não definido>"
if gols == "" or gols == " ":
    gols = 0
ficha(nome, gols)
