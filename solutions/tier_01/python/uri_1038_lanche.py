# -*- coding: utf-8 -*-
dictTabelaPreco = {"1": 4, "2": 4.5, "3": 5, "4": 2, "5": 1.5}
inputListCodProdQnt = list(map(str, input().split()))

precoTotal = dictTabelaPreco[inputListCodProdQnt[0]] * int(inputListCodProdQnt[1])

print("Total: R$ {:.2f}".format(precoTotal))