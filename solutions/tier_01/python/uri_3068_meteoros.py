# -*- coding: utf-8 -*-
inputCoordInicialFinalFazenda = list(map(int, input().split()))

countTest = 1
while sum(inputCoordInicialFinalFazenda) != 0:
    qntOcorrenciaMeteoro = int(input())

    qntOcorrenciaMeteoroDentroFazenda = 0

    tamanhoFazendaCoordX = abs(inputCoordInicialFinalFazenda[0] - inputCoordInicialFinalFazenda[2])
    tamanhoFazendaCoordY = abs(inputCoordInicialFinalFazenda[1] - inputCoordInicialFinalFazenda[3])

    for indiceOcorrenciaMeteoro in range(0,qntOcorrenciaMeteoro):
        listInputCoordMeteoro = list(map(int, input().split()))
        if listInputCoordMeteoro[0] >= inputCoordInicialFinalFazenda[0] and abs(listInputCoordMeteoro[0] - inputCoordInicialFinalFazenda[0]) <= tamanhoFazendaCoordX:
            if listInputCoordMeteoro[1] <= inputCoordInicialFinalFazenda[1] and abs(listInputCoordMeteoro[1] - inputCoordInicialFinalFazenda[1]) <= tamanhoFazendaCoordY:
                qntOcorrenciaMeteoroDentroFazenda += 1
    
    print("Teste {}".format(countTest))
    print("{}".format(qntOcorrenciaMeteoroDentroFazenda))

    countTest += 1

    inputCoordInicialFinalFazenda = list(map(int, input().split()))