from math import sqrt

def isPrime(number):
    raiz = int(sqrt(number))

    if number != 2 and (number % 2 == 0 or number == 1): return False

    for indiceI in range(3, raiz+1, 2):
        if number % indiceI == 0: return False
    return True

while True:
    try:
        QntMoedaComValor = int(input())
        listMoedaComValor = [int(input()) for indiceMoeda in range(0,QntMoedaComValor)]
        listMoedaComValor.reverse()
        
        tamanhoSalto = int(input())
        listMoedaConsideradaSalto = [listMoedaComValor[indiceMoeda] for indiceMoeda in range(0,QntMoedaComValor,tamanhoSalto)]

        print("You’re a coastal aircraft, Robbie, a large silver aircraft." if isPrime(sum(listMoedaConsideradaSalto)) else "Bad boy! I’ll hit you.")
    except EOFError:
        break