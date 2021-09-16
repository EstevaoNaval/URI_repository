# -*- coding: utf-8 -*-
indiceElementoSeqFibonot = int(input())

ultimoNum = 1
penultimoNum = 1
somaDoisNumAnterior = 0

countIndiceElementoSeqFibonot = 0
counter = 0
while countIndiceElementoSeqFibonot != indiceElementoSeqFibonot:
    if counter <= 1: 
        somaDoisNumAnterior = penultimoNum
        counter += 1
    else:
        somaDoisNumAnterior = ultimoNum + penultimoNum
        if somaDoisNumAnterior != ultimoNum + 1:
            for indiceNumFibonot in range(ultimoNum+1, somaDoisNumAnterior):
                ultimoElementoSeqFibonot = indiceNumFibonot 
                countIndiceElementoSeqFibonot += 1
                if countIndiceElementoSeqFibonot == indiceElementoSeqFibonot: break

        penultimoNum = ultimoNum
        ultimoNum = somaDoisNumAnterior

print(ultimoElementoSeqFibonot)