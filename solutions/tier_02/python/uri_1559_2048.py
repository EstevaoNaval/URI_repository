# -*- coding: utf-8 -*-
qntCasoTeste = int(input())

for caso in range(qntCasoTeste):
    matriz4x4 = [list(map(int, input().split())) for linha in range(4)]
    setAcaoPossivel = set()
    
    for linha in range(4):
        if sum(matriz4x4[linha]) == 0: continue
        elif matriz4x4[linha].count(2048) > 0:
            setAcaoPossivel = {} 
            break
        for coluna in range(4):
            if matriz4x4[linha][coluna] != 0:
                if linha > 0 and (matriz4x4[linha - 1][coluna] == 0 or matriz4x4[linha - 1][coluna] == matriz4x4[linha][coluna]): setAcaoPossivel.add("UP")
                if linha < 3 and (matriz4x4[linha + 1][coluna] == 0 or matriz4x4[linha + 1][coluna] == matriz4x4[linha][coluna]): setAcaoPossivel.add("DOWN")
                if coluna > 0 and (matriz4x4[linha][coluna - 1] == 0 or matriz4x4[linha][coluna - 1] == matriz4x4[linha][coluna]): setAcaoPossivel.add("LEFT")
                if coluna < 3 and (matriz4x4[linha][coluna + 1] == 0 or matriz4x4[linha][coluna + 1] == matriz4x4[linha][coluna]): setAcaoPossivel.add("RIGHT")
    
    if not setAcaoPossivel: strAcao = "NONE"
    else:
        strAcao = ""
        for acao in sorted(setAcaoPossivel): strAcao += "{} ".format(acao) 
    print(strAcao.strip())