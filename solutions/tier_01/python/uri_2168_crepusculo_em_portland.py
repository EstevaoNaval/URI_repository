# -*- coding: utf-8 -*-
tamanhoMatrizNxN = int(input())
matrizNxN = [list(map(int, input().split())) for coluna in range(tamanhoMatrizNxN + 1)]

sequenciaStrSafeUnsafe = ""
for linha in range(tamanhoMatrizNxN):
    for coluna in range(tamanhoMatrizNxN):
        sequenciaStrSafeUnsafe += "S" if matrizNxN[linha][coluna]+matrizNxN[linha][coluna+1]+matrizNxN[linha+1][coluna]+matrizNxN[linha+1][coluna+1] > 1 else "U"
    print(sequenciaStrSafeUnsafe)
    sequenciaStrSafeUnsafe = ""