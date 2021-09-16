# -*- coding: utf-8 -*-
qntCaso = int(input())

for caso in range(qntCaso):
    listInputMeN = list(map(int, input().split()))
    dictPalavraBR_JP = dict()

    for indicePalavra in range(listInputMeN[0]):
        inputPalavraJP = input()
        inputPalavraBR = input()
        dictPalavraBR_JP.update({inputPalavraJP: inputPalavraBR})
    for indiceLetraMusica in range(listInputMeN[1]):
        listInputPalavrasJP = list(map(str, input().split()))
        
        strSequenciaTraduzida = ""
        for palavra in listInputPalavrasJP:
            try:
                strSequenciaTraduzida += "{} ".format(dictPalavraBR_JP[palavra])
            except KeyError:
                strSequenciaTraduzida += "{} ".format(palavra)
        print(strSequenciaTraduzida.strip())
    print("")