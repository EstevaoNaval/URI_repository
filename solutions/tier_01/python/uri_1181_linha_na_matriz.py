# -*- coding: utf-8 -*-
matriz12x12 = [[0] * 12 for coluna in range(12)]

indiceLinhaConsiderarOperacao = int(input())
tipoOperacao = input()

for linha in range(12):
    for coluna in range(12):
        matriz12x12[linha][coluna] = float(input())

print(sum(matriz12x12[indiceLinhaConsiderarOperacao]) if tipoOperacao == "S" else sum(matriz12x12[indiceLinhaConsiderarOperacao])/12)