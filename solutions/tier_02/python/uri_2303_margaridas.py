totalLinhaMatrizMargarida, totalColunaMatrizMargarida, totalLinhaLote, totalColunaLote = map(int, input().split())

matrizMargaridas = list()

for linhaMargarida in range(totalLinhaMatrizMargarida):
    matrizMargaridas.append(list(map(int, input().split())))

maiorSomaLoteMargaridas = -1
totalMargaridasLote = 0

for linhaMatrizMargaridas in range(0,totalLinhaMatrizMargarida, totalLinhaLote):
    for colunaMatrizMargaridas in range(0, totalColunaMatrizMargarida, totalColunaLote):
        for linhaLoteMargaridas in range(linhaMatrizMargaridas, linhaMatrizMargaridas + totalLinhaLote):
            for colunaLoteMargaridas in range(colunaMatrizMargaridas, colunaMatrizMargaridas + totalColunaLote):
                totalMargaridasLote += matrizMargaridas[linhaLoteMargaridas][colunaLoteMargaridas]
        maiorSomaLoteMargaridas = totalMargaridasLote if totalMargaridasLote > maiorSomaLoteMargaridas else maiorSomaLoteMargaridas
        totalMargaridasLote = 0

print(maiorSomaLoteMargaridas)