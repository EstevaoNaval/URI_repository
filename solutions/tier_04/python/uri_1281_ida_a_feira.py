# -*- coding: utf-8 -*-
qntCasoTeste = int(input())

for caso in range(qntCasoTeste):
    dictPrecoProduto = dict()

    qntPrecoProd = int(input())
    for indicePrecoProd in range(qntPrecoProd): 
        inputProd = list(map(str, input().split()))
        dictPrecoProduto.update({inputProd[0]:float(inputProd[1])})
    
    qntProdutoLista = int(input())
    precoTotal = 0
    for indiceListaProd in range(qntProdutoLista):
        inputProd = list(map(str, input().split()))
        precoTotal += dictPrecoProduto[inputProd[0]] * int(inputProd[1])

    print("R$ {:.2f}".format(precoTotal)) 