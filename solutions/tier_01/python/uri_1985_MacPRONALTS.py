# -*- coding: utf-8 -*-
dictPrecoProd = {"1001":1.5,"1002":2.5,"1003":3.5,"1004":4.5,"1005":5.5}

qntProdConsumido = int(input())
precoTotal = 0
for prodConsumido in range(qntProdConsumido):
    inputCodProdQntConsumida = list(map(str, input().split()))
    precoTotal += dictPrecoProd[inputCodProdQntConsumida[0]] * int(inputCodProdQntConsumida[1])

print("{:.2f}".format(precoTotal))