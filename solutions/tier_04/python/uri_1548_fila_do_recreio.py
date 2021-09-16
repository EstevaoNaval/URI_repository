qntCaso = int(input())

for indiceCaso in range(0,qntCaso):
    qntAlunoNaFila = int(input())
    
    filaNotaAluno = list(map(int, input().split()))
    filaNotaAlunoSorted = sorted(filaNotaAluno[:],reverse=True)

    qntNotaAlunoLugarCerto = 0

    for notaAluno in range(qntAlunoNaFila): qntNotaAlunoLugarCerto += 1 if filaNotaAluno[notaAluno] == filaNotaAlunoSorted[notaAluno] else 0

    print(qntNotaAlunoLugarCerto)