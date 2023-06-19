# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as alunos de cada aluno individualmente.
boletim = list()
aluno = list()
print("Iniciando o progama [press enter to close]")
while True:
    média = 0
    aluno.append(input("Digite o nome do aluno: "))
    if aluno[0] == "" or aluno[0] == " ":
        break
    aluno.append(float(input("Digite a primeira nota do aluno: ")))
    aluno.append(float(input("Digite a segunda nota do aluno: ")))
    média = (aluno[1]+aluno[2])/2
    aluno.append(média)
    boletim.append(aluno[:])
    aluno.clear()

for n in range(0, len(boletim)):
    print(
        f"Aluno: [{boletim[n][0]}] notas: [{boletim[n][1]}][{boletim[n][2]}] Média:{boletim[n][3]} ")
