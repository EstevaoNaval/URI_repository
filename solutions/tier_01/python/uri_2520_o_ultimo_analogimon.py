# -*- coding: utf-8 -*-
while True:
    try:
        listDimensaoMatriz = list(map(int, input().split()))
        listCoordTreinadorPokemon = list()

        for linha in range(listDimensaoMatriz[0]):
            listColunaMatriz = list(map(int, input().split()))
            if listColunaMatriz.count(1) > 0: listCoordTreinadorPokemon.append([linha, listColunaMatriz.index(1)])
            if listColunaMatriz.count(2) > 0: listCoordTreinadorPokemon.append([linha, listColunaMatriz.index(2)])

        menorTempoNecessario = abs(listCoordTreinadorPokemon[0][0] - listCoordTreinadorPokemon[1][0]) + abs(listCoordTreinadorPokemon[0][1] - listCoordTreinadorPokemon[1][1])
        print(menorTempoNecessario)
    except EOFError:
        break