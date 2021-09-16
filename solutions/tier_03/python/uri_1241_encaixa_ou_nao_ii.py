# -*- coding: utf-8 -*-
qntCasos = int(input())

for indiceCaso in range(qntCasos):
    listInputNum = list(map(str, input().split()))
    print("encaixa" if listInputNum[0][len(listInputNum[0]) - len(listInputNum[1]):] == listInputNum[1] else "nao encaixa")