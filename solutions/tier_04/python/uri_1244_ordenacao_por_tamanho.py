# -*- coding: utf-8 -*-
qntCaso = int(input())

for caso in range(qntCaso):
    listStrTamanhoStr = list()
    listStr = list(map(str, input().split()))

    for indiceStr in range(len(listStr)): listStrTamanhoStr.append([listStr[indiceStr], len(listStr[indiceStr])])
    
    strSequenciaOrdenadaTamanho = ""
    for chave, valor in sorted(listStrTamanhoStr, key=lambda x: x[1],reverse=True): strSequenciaOrdenadaTamanho += "{} ".format(chave)
    print(strSequenciaOrdenadaTamanho.strip())