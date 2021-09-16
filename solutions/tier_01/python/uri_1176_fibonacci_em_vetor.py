# -*- coding: utf-8 -*-
numCasoTest = int(input())

for indice in range(numCasoTest):
    indiceFibonacci = int(input())

    ultimoNum = 1
    penultimoNum = 1
    soma2NumAnterior = 0

    count = 0
    for indice in range(indiceFibonacci):
        if indice == 0 or indice == 1:
            soma2NumAnterior = 1
        else:
            soma2NumAnterior = ultimoNum + penultimoNum
            penultimoNum = ultimoNum
            ultimoNum = soma2NumAnterior
    
    print("Fib({}) = {}".format(indiceFibonacci, soma2NumAnterior))