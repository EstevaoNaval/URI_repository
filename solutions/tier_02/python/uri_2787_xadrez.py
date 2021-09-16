# -*- coding: utf-8 -*-
linha = int(input())
coluna = int(input())
if linha == coluna: corCasaInferiorDireito = 1
elif linha % 2 == 0:
    if coluna % 2 != 0: corCasaInferiorDireito = 0
    else: corCasaInferiorDireito = 1
elif linha % 2 != 0:
    if coluna % 2 != 0: corCasaInferiorDireito = 1
    else: corCasaInferiorDireito = 0
print(corCasaInferiorDireito)