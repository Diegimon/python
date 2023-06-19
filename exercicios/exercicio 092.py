lista = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    if jogador['nome'] == '':
        break
    else:
        jogador['partidas'] = int(input('Quantas partidas jogadas: '))
        for g in range(0, jogador['partidas']):
            gol = int(input(f'Quantos gols na partida {g+1}: '))
            gols.append(gol)
        jogador['gols'] = gols
        jogador['total'] = sum(gols)
        lista.append(jogador.copy())
        gols.clear()
for p in lista:
    print(
        f"O jogador [{p['nome']}] fez um total de {p['total']} Gol(s) em {p['partidas']} partida(s)")
