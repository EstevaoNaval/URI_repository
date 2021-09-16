# -*- coding: utf-8 -*-
matriz12x12 = [[0] * 12 for coluna in range(12)]

tipoOperacao = input()

for linha in range(12):
    for coluna in range(12):
        matriz12x12[linha][coluna] = float(input())

diminuidor, somador, somaAreaInferiorMatriz = 0,0,0
for linha in range(7,12):
    for coluna in range(5 - diminuidor, 7 + somador):
        somaAreaInferiorMatriz += matriz12x12[linha][coluna]

        diminuidor += 1
        somador += 2

print(somaAreaInferiorMatriz if tipoOperacao == "S" else somaAreaInferiorMatriz/30)