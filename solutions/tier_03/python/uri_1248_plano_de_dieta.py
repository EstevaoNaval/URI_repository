# -*- coding: utf-8 -*-
qntCasos = int(input())

for caso in range(qntCasos):
    strDieta = input()
    strCafeDaManha = input()
    strAlmoco = input()

    EhCheater = False
    for indice in range(len(strCafeDaManha)):
        if strCafeDaManha[indice] in strDieta: strDieta = strDieta.replace(strCafeDaManha[indice], "")
        else: EhCheater = True
    for indice in range(len(strAlmoco)):
        if strAlmoco[indice] in strDieta: strDieta = strDieta.replace(strAlmoco[indice], "")
        else: EhCheater = True

    if EhCheater == True: print("CHEATER")
    else: print("".join(sorted(strDieta))) 