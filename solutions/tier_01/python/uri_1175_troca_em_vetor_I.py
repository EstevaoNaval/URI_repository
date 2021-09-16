# -*- coding: utf-8 -*-
vetorI = [0] * 20

for indiceVetor in range(0, 20): vetorI[indiceVetor] = int(input())

countIndiceVetor = 0
for indiceVetorFimMeio in range(19, 11, -1): 
    print("N[{}] = {}".format(countIndiceVetor, vetorI[indiceVetorFimMeio]))
    countIndiceVetor += 1

for indiceVetorInicioMeio in range(11,-1,-1):
    print("N[{}] = {}".format(countIndiceVetor, vetorI[indiceVetorInicioMeio]))
    countIndiceVetor += 1