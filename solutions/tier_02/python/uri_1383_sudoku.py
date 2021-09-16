# -*- coding: utf-8 -*-
qntInstancias = int(input())

for instancia in range(qntInstancias):
    matriz9x9Sudoku = [[0] * 9 for linha in range(9)]
    EhSolucaoProblemaSoduko = "SIM"

    for linha in range(9): matriz9x9Sudoku[linha] = list(map(int, input().split()))

    # Analisa se as linhas da matriz estão numerados de 1 a 9
    for coluna in range(9):
        if len(matriz9x9Sudoku[coluna]) != len(set(matriz9x9Sudoku[coluna])): EhSolucaoProblemaSoduko = "NAO"

    # Analisa se as colunas da matriz estão numerados de 1 a 9
    if EhSolucaoProblemaSoduko != "NAO":
        for coluna in range(9):
            listValores = []
            for linha in range(9): listValores.append(matriz9x9Sudoku[linha][coluna]) 
            if len(listValores) != len(set(listValores)): 
                EhSolucaoProblemaSoduko = "NAO"
                break
        
        if EhSolucaoProblemaSoduko != "NAO":
            # Analisa se cada sub-bloco 3x3 da matriz estão numerados de 1 a 9
            listValores = []
            tamanhoAvancoIndiceBlocoEsquerda = 0
            tamanhoAvancoIndiceBlocoAbaixo = 0
            for sub_bloco in range(9):
                for linha in range(0 + tamanhoAvancoIndiceBlocoAbaixo , 3 + tamanhoAvancoIndiceBlocoAbaixo):
                    for coluna in range(0 + tamanhoAvancoIndiceBlocoEsquerda, 3 + tamanhoAvancoIndiceBlocoEsquerda):
                        listValores.append(matriz9x9Sudoku[linha][coluna])
                
                if len(listValores) != len(set(listValores)):
                    EhSolucaoProblemaSoduko = "NAO"
                    break
                listValores = []

                tamanhoAvancoIndiceBlocoEsquerda += 3

                if tamanhoAvancoIndiceBlocoEsquerda >= 9:
                    tamanhoAvancoIndiceBlocoEsquerda = 0
                    tamanhoAvancoIndiceBlocoAbaixo += 3
                
    print("Instancia {}".format(instancia + 1))
    print("{}\n".format(EhSolucaoProblemaSoduko))