# -*- coding: utf-8 -*-
listNum = list(map(int, input().split()))

qntNumCrescendo = 0

for indiceNum in range(1, len(listNum)):
    if listNum[indiceNum - 1] < listNum[indiceNum]: qntNumCrescendo += 1
    elif listNum[indiceNum - 1] > listNum[indiceNum]: qntNumCrescendo -= 1

if qntNumCrescendo == len(listNum) - 1: situacaoLista = "C"
elif qntNumCrescendo == -(len(listNum) - 1): situacaoLista = "D"
else: situacaoLista = "N"

print(situacaoLista)