# -*- coding: utf-8 -*-
qntCaso = int(input())

for caso in range(qntCaso):
    numTotalRena, numTotalRenaPuxaraoTreno = map(int, input().split())
    listRena = [list(map(str, input().split())) for linha in range(numTotalRena)]
    
    listRena = sorted(listRena, key= lambda x: (-int(x[1]),int(x[2]),float(x[3]),x[0]))
    
    print("CENARIO {"+str(caso+1)+"}")
    for indiceRena in range(numTotalRenaPuxaraoTreno): print("{} - {}".format(indiceRena + 1, listRena[indiceRena][0]))