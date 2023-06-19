import datetime
data = datetime.date.today().year
carteira = dict()
trabalho = list()
print('=*'*10)
print('Iniciando progama!\nPara sair tecle [Enter]')
print('=*'*10)
while True:
    carteira['nome'] = str(input('seu nome: '))
    if carteira['nome'] == '':
        break
    carteira['ano'] = int(input("Ano de nascimento: "))
    carteira['ctps'] = (input("Numero ctps [caso não posua tecle enter]: "))
    if carteira['ctps'] == "" or carteira['ctps'] == ' ':
        carteira.__delitem__('ctps')
    else:
        carteira['cont'] = int(input("Ano de contratação: "))
        carteira['salario'] = (input("Salario: "))
    trabalho.append(carteira.copy())
    carteira.clear()
print("Progama encerrado!")
for t in trabalho:
    ctps = t.get('ctps')
    if ctps is None:
        print(f"{t['nome']} não trabalha")
    else:
        aposenta = t['cont']+40
        idade = aposenta - t['ano']
        print(f"Com {data - t['ano']} Anos ")
        print(
            f"{t['nome']} irá se aposentar em {aposenta} com {idade} Anos recebendo {t['salario']}R$")
