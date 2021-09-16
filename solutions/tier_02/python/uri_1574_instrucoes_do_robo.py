# -*- coding: utf-8 -*-
qntCasos = int(input())

for indiceCaso in range(qntCasos):
    qntInstrucoes = int(input())
    
    listLogInstrucao = []
    posicaoNumericaRobo = 0
    for indiceInstrucao in range(qntInstrucoes):
        inputInstrucao = input()
        if inputInstrucao == "LEFT": 
            posicaoNumericaRobo -= 1
            listLogInstrucao.append(inputInstrucao)
        elif inputInstrucao == "RIGHT": 
            posicaoNumericaRobo += 1
            listLogInstrucao.append(inputInstrucao)
        else: 
            if listLogInstrucao[int(inputInstrucao[8:]) - 1] == "LEFT": posicaoNumericaRobo -= 1
            else: posicaoNumericaRobo += 1
            listLogInstrucao.append(listLogInstrucao[int(inputInstrucao[8:]) - 1])
    print(posicaoNumericaRobo)