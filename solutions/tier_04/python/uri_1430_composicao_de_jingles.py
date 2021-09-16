# -*- coding: utf-8 -*-
dictTempoMusica = dict({"W":1,"H":1/2,"Q":1/4,"E":1/8,"S":1/16,"T":1/32,"X":1/64})
listSeqCompasso = list(map(str, input().split("/")))

while listSeqCompasso[0] != "*":
    listSeqCompasso.pop(0)
    listSeqCompasso.pop(-1)

    qntCompassoDuracaoCorreta = 0
    for compasso in listSeqCompasso:
        duracaoCompasso = 0
        for tempo in compasso: duracaoCompasso += dictTempoMusica[tempo]
        if duracaoCompasso == 1: qntCompassoDuracaoCorreta += 1
    
    print(qntCompassoDuracaoCorreta)

    listSeqCompasso = list(map(str, input().split("/")))