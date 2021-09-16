# -*- coding: utf-8 -*-
qntCaso = int(input())

for caso in range(qntCaso):
    str01,str02 = input().split()
    finalPalavra = ""
    contMaiorPalavra = 0

    while contMaiorPalavra < len(str01) and contMaiorPalavra < len(str02):
        finalPalavra += str01[contMaiorPalavra] + str02[contMaiorPalavra]
        contMaiorPalavra += 1 
    
    if contMaiorPalavra < len(str01): finalPalavra += str01[contMaiorPalavra:]

    if contMaiorPalavra < len(str02): finalPalavra += str02[contMaiorPalavra:]
    
    print(finalPalavra)