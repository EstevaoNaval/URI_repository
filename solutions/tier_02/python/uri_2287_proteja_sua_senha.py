# -*- coding: utf-8 -*-
qntLetterAssociation = int(input())

dictAssociationLetterNumber = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
countTest = 1
while qntLetterAssociation != 0:
    matrixDigitCounter = [10 * [0] for column in range(6)]

    for indexAssociation in range(qntLetterAssociation):
        listInput = list(map(str, input().split()))
        listDigit = [list(map(int, listInput[x:x+2])) for x in range(0,10,2)]
        listLetter = list(map(str, listInput[10:16]))
        
        for column in range(6):
            matrixDigitCounter[column][listDigit[dictAssociationLetterNumber[listLetter[column]]][0]] += 1
            matrixDigitCounter[column][listDigit[dictAssociationLetterNumber[listLetter[column]]][1]] += 1
        
    strSenha = ""
    for column in range(6):
        strSenha += "{} ".format(matrixDigitCounter[column].index(max(matrixDigitCounter[column])))

    print(f"Teste {countTest}"
          f"\n{strSenha}"
          f"\n")

    qntLetterAssociation = int(input())
    countTest += 1