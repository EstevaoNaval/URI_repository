# -*- coding: utf-8 -*-
qntIndividuoNaLista = int(input())
countCasos = 1

while qntIndividuoNaLista != 0:
    listaConvidadoFesta = list(map(int, input().split()))
    for indiceConvidado in range(qntIndividuoNaLista):
        if indiceConvidado + 1 == listaConvidadoFesta[indiceConvidado]:
            print("Teste {}".format(countCasos))
            print(listaConvidadoFesta[indiceConvidado])
            print("")
            break
    
    countCasos += 1
    qntIndividuoNaLista = int(input())