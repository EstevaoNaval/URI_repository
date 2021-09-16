# -*- coding: utf-8 -*-
qntAluno = int(input())

while qntAluno != 0:
    dictAlunoTurma = dict()

    for alunoAssOriginal in range(qntAluno):
        inputNomeAlunoAssOriginal = list(map(str, input().split()))
        dictAlunoTurma.update({inputNomeAlunoAssOriginal[0]:inputNomeAlunoAssOriginal[1]})
    
    qntAlunoCompareceuAula = int(input())
    qntAssFalsa = 0
    for alunoCompareceu in range(qntAlunoCompareceuAula):
        qntLetraDiferente = 0
        inputNomeAlunoAss = list(map(str, input().split()))
        for indiceLetra in range(len(inputNomeAlunoAss[1])):
            if inputNomeAlunoAss[1][indiceLetra] != dictAlunoTurma[inputNomeAlunoAss[0]][indiceLetra]: qntLetraDiferente += 1
        if qntLetraDiferente > 1: qntAssFalsa += 1
    
    print(qntAssFalsa)

    qntAluno = int(input())