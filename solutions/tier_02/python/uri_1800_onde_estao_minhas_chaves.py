# -*- coding: utf-8 -*-
qntEscritorioUltimaSemana, qntEscritorioUltimoDia = map(int, input().split())
listIdEscritorioUltimoDia = list(map(str, input().split()))
dictEscritorioUltimosDias = dict()

for escritorio in listIdEscritorioUltimoDia: dictEscritorioUltimosDias.update({escritorio:1})

for registroEscritorio in range(qntEscritorioUltimaSemana):
    idEscritorio = input()
    try: 
        if dictEscritorioUltimosDias[idEscritorio] == 1: print(0) 
    except KeyError:
        dictEscritorioUltimosDias.update({idEscritorio:1})
        print(1)