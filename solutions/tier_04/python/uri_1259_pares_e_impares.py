# -*- coding: utf-8 -*-
qntNum = int(input())

listInput = list()
for num in range(qntNum): listInput.append(int(input()))

listNumPar = list()
listNumImpar = list()

for numList in listInput:
    if numList % 2 == 0:
        listNumPar.append(numList)
    else:
        listNumImpar.append(numList)

listNumPar.sort()
listNumImpar.sort(reverse=True)

for numPar in listNumPar: print(numPar)
for numImpar in listNumImpar: print(numImpar)