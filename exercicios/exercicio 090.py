from time import sleep
verde = '\033[0;49;32m'
vermelho = '\033[0;49;91m'
aluno = dict()
aprovados = list()
reprovados = list()
while True:
    aluno['nome'] = str(input("Digite o nome do aluno: "))
    if aluno['nome'] == '' or aluno['nome'] == ' ':
        break
    aluno['média'] = int(input("digite a média do aluno: "))
    if aluno['média'] > 6:
        aprovados.append(aluno.copy())
    else:
        reprovados.append(aluno.copy())
print(verde, "=*"*10, '\n Alunos aprovados!\n', '=*'*10)
for alunos in aprovados:
    print(alunos)
print(vermelho, "=*"*10, '\n Alunos reprovados\n', '=*'*10)
for alunos in reprovados:
    print(alunos)
sleep(10)
