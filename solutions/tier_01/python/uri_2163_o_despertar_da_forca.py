# -*- coding: utf-8 -*-
def verifica42NoMeio(linha, coluna, maximaCoordLinha, maximaCoordColuna, valorPonto):
    if valorPonto == 42:
        if coluna > 0 and coluna < maximaCoordColuna - 1:
            if linha > 0 and linha < maximaCoordLinha - 1:
                return True
    return False
def verificar7AoRedor(linha, coluna, matriz):
    if matriz[linha - 1][coluna - 1] == 7 and matriz[linha - 1][coluna] == 7 and matriz[linha - 1][coluna + 1] == 7:
        if matriz[linha][coluna - 1] == 7 and matriz[linha][coluna + 1] == 7:
            if matriz[linha + 1][coluna - 1] == 7 and matriz[linha + 1][coluna] == 7 and matriz[linha + 1][coluna + 1] == 7:
                return True
    return False

listDimensaoMatriz = list(map(int, input().split()))
matriz = [list(map(int, input().split())) for linha in range(listDimensaoMatriz[0])]

for linha in range(listDimensaoMatriz[0]):
    for coluna in range(listDimensaoMatriz[1]):
        if verifica42NoMeio(linha, coluna, listDimensaoMatriz[0],listDimensaoMatriz[1], matriz[linha][coluna]):
            if verificar7AoRedor(linha, coluna, matriz):
                print("{} {}".format(linha + 1, coluna + 1))
                exit()

print("0 0")