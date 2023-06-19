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
        jogador['gols'] = gols.copy()
        jogador['total'] = sum(gols)
        lista.append(jogador.copy())
        gols.clear()
for p in lista:
    print(
        f"O jogador [{p['nome']}] fez um total de {p['total']} Gol(s) em {p['partidas']} partida(s)")
op = int(input('[1]Pesquisar [2]Inserir [3]Retirar '))
if op == 1:

    for p in lista:
        if p['nome'] == nome:
            print(f'Aproveitamento do jogador [{nome}] : ')
            for j, n in enumerate(p['gols']):
                print(f'Na  partida {j+1} {nome} marcou {n} gols')
if op == 3:
    nome = str(input('Quem deseja retirar da lista: '))
    for p in lista:
        if p['nome'] == nome:
            lista.pop(p['nome'])
