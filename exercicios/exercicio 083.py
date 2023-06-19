pilha = []
expressao = input("Digite a expressão a ser analisada: ")
for caractere in expressao:
    if "(" in caractere:
        pilha.append("(")
    elif ")" in caractere:
        if len(pilha) == 0:
            print("Expressão incorreta!")
            break
        pilha.pop()
if len(pilha) > 0:
    print("Expressão incorreta!")
else:
    print("Expressão correta!")
