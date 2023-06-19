pessoas = list()
dados = dict()
mulheres = list()
acima_media = list()
tot_idade = media = 0
print('=*'*15)
print('Progama iniciado\nTecle [enter] para sair')
print('=*'*15)
while True:
    dados['nome'] = str(input('Nome: '))
    if dados['nome'] == '' or dados['nome'] == ' ':
        break
    dados['idade'] = int(input('idade: '))
    sexo = int(input('[1]feminino [2]Masculino : '))
    print('=*'*15)
    if sexo == 1:
        dados['sexo'] = 'feminino'
        mulheres.append(dados.copy())
    elif sexo == 2:
        dados['sexo'] = 'masculino'
    pessoas.append(dados.copy())

    tot_idade += dados['idade']
media = tot_idade/len(pessoas)
print('=*'*5, f'Total de pessoas cadastradas {len(pessoas)}', '*='*5)
print(f'Média de idades = {media}')
print(f'Foram cadastradas {len(mulheres)} Mulheres: ', end=' ')
for i in mulheres:
    print(i['nome'], end=' ')
print('\nestão acima da média: ', end=' ')
for p in pessoas:
    if p['idade'] > media:
        print(p['nome'])
