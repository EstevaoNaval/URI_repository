# -*- coding: utf-8 -*-
numPartida = int(input())

while numPartida != 0:
    qntPontoMaximoJogador01, qntPontoMaximoJogador02 = 0,0

    for indicePartida in range(0, numPartida):
        listInputNum = list(map(int, input().split()))

        qntPontoMaximoJogador01 += 1 if listInputNum[0] > listInputNum[1] else 0
        qntPontoMaximoJogador02 += 1 if listInputNum[0] < listInputNum[1] else 0
    print("{} {}".format(qntPontoMaximoJogador01, qntPontoMaximoJogador02))

    numPartida = int(input())