# -*- coding: utf-8 -*-
while True:
    try:
        listDimensaoMatriz = list(map(int, input().split()))
        matrizTabuleiro = [list(map(int, input().split())) for linha in range(listDimensaoMatriz[0])]

        qntPaoDeQueijoAdjacente = 0
        for linha in range(listDimensaoMatriz[0]):
            strConfigTabuleiro = ""
            for coluna in range(listDimensaoMatriz[1]):
                if matrizTabuleiro[linha][coluna] == 1: strConfigTabuleiro += "9"
                else:
                    if linha < listDimensaoMatriz[0] - 1 and matrizTabuleiro[linha + 1][coluna] != 0: qntPaoDeQueijoAdjacente += 1
                    if linha > 0 and matrizTabuleiro[linha - 1][coluna] != 0: qntPaoDeQueijoAdjacente += 1
                    if coluna < listDimensaoMatriz[1] - 1 and matrizTabuleiro[linha][coluna + 1] != 0: qntPaoDeQueijoAdjacente += 1
                    if coluna > 0 and matrizTabuleiro[linha][coluna - 1] != 0: qntPaoDeQueijoAdjacente += 1
                    strConfigTabuleiro += str(qntPaoDeQueijoAdjacente)
                    qntPaoDeQueijoAdjacente = 0
            print(strConfigTabuleiro)
    except EOFError:
        break