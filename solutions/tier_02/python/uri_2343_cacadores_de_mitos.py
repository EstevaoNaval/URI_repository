# -*- coding: utf-8 -*-
qntOcorrenciaRaio = int(input())

caiuMesmoLugar = 0
dictCoordRaio = [501 * [0] for x in range(501)]
for indexOcorrencia in range(qntOcorrenciaRaio):
    listCoordRaioCaiu = list(map(int, input().split()))
    if caiuMesmoLugar == 0:
        if dictCoordRaio[listCoordRaioCaiu[0]][listCoordRaioCaiu[1]] == 0:
            dictCoordRaio[listCoordRaioCaiu[0]][listCoordRaioCaiu[1]] = 1
        else:
            caiuMesmoLugar = 1
    else:
        break
    
print(caiuMesmoLugar)