listInputSetInicial = list(map(int, input().split()))

listValInicialCadaJogador = [listInputSetInicial[0]] * 3

for indiceOperacao in range(0, listInputSetInicial[1]):
    inputValOperacao = list(map(str, input().split()))
    if inputValOperacao[0] == "C":
        if inputValOperacao[1] == "D": listValInicialCadaJogador[0] -= int(inputValOperacao[2]) 
        elif inputValOperacao[1] == "E": listValInicialCadaJogador[1] -= int(inputValOperacao[2])
        else: listValInicialCadaJogador[2] -= int(inputValOperacao[2])
    elif inputValOperacao[0] == "V":
        if inputValOperacao[1] == "D": listValInicialCadaJogador[0] += int(inputValOperacao[2]) 
        elif inputValOperacao[1] == "E": listValInicialCadaJogador[1] += int(inputValOperacao[2])
        else: listValInicialCadaJogador[2] += int(inputValOperacao[2])
    else:
        if inputValOperacao[1] == "D":
            listValInicialCadaJogador[0] += int(inputValOperacao[3])
            if inputValOperacao[2] == "E": listValInicialCadaJogador[1] -= int(inputValOperacao[3])
            elif inputValOperacao[2] == "F": listValInicialCadaJogador[2] -= int(inputValOperacao[3])
        elif inputValOperacao[1] == "E":
            listValInicialCadaJogador[1] += int(inputValOperacao[3])
            if inputValOperacao[2] == "D": listValInicialCadaJogador[0] -= int(inputValOperacao[3])
            elif inputValOperacao[2] == "F": listValInicialCadaJogador[2] -= int(inputValOperacao[3])
        elif inputValOperacao[1] == "F":
            listValInicialCadaJogador[2] += int(inputValOperacao[3])
            if inputValOperacao[2] == "D": listValInicialCadaJogador[0] -= int(inputValOperacao[3])
            elif inputValOperacao[2] == "E": listValInicialCadaJogador[1] -= int(inputValOperacao[3])

print("{} {} {}".format(listValInicialCadaJogador[0],listValInicialCadaJogador[1],listValInicialCadaJogador[2]))
