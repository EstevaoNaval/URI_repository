# -*- coding: utf-8 -*-
dictTraducaoFelizNatal = {}

qntTraducoes = int(input())
for indiceTraducao in range(qntTraducoes):
    linguaAlvoTraducao = input()
    traducaoFelizNatal = input()
    dictTraducaoFelizNatal.update({linguaAlvoTraducao:traducaoFelizNatal})

qntCriancaRegiao = int(input())
for indiceCrianca in range(qntCriancaRegiao):
    nomeCrianca = input()
    linguaAlvoTraducao = input()
    print(nomeCrianca)
    print(dictTraducaoFelizNatal[linguaAlvoTraducao])
    print("")