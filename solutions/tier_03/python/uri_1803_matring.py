# -*- coding: utf-8 -*-
matring = [input() for linha in range(4)]

F = int(matring[0][0] + matring[1][0] + matring[2][0] + matring[3][0])
L = int(matring[0][-1] + matring[1][-1] + matring[2][-1] + matring[3][-1])

strSeqCodificada = ""
for indice in range(1, len(matring[0]) - 1):
    I = int(matring[0][indice] + matring[1][indice] + matring[2][indice] + matring[3][indice])
    strSeqCodificada += chr((F * I + L) % 257)

print(strSeqCodificada)