vogais = ['a', 'e', 'i', 'o', 'u']
palavras_vogais = []
while True:
    palavra = input("\ninsira uma palavra: ")
    if palavra == '':
        break

    vogais_palavra = ""
    for letra in palavra:
        if letra.lower() in vogais:
            vogais_palavra += letra + " "

    palavras_vogais.append((palavra, vogais_palavra))

print("\nPalavras e suas vogais:")
for palavra, vogais in palavras_vogais:
    print(f'Na palavra "{palavra}" as vogais são: {vogais}')
