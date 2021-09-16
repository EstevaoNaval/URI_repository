from collections import Counter

qntCaso = int(input())
for caso in range(qntCaso):
    frase = input()
    counterAlfabetoFrase = Counter(frase)
    del counterAlfabetoFrase[" "]
    del counterAlfabetoFrase[","]

    if len(counterAlfabetoFrase) >= 13 and len(counterAlfabetoFrase) < 26: estadoFrase = "frase quase completa"
    elif len(counterAlfabetoFrase) == 26: estadoFrase = "frase completa"
    else: estadoFrase = "frase mal elaborada"

    print(estadoFrase)