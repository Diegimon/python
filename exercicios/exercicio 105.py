def anota(*nota):
    notas = []
    for n in nota:
        if notas[0]:
            maior = menor = n
        else:
