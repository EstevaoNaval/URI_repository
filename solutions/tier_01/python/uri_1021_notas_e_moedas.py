valOriginal = float(input()) + 0.00001

numFloat = valOriginal

qntNotaCem = numFloat//100
numFloat -= qntNotaCem * 100

qntNotaCinquenta = numFloat//50
numFloat -= qntNotaCinquenta * 50

qntNotaVinte = numFloat//20
numFloat -= qntNotaVinte * 20

qntNotaDez = numFloat//10
numFloat -= qntNotaDez * 10

qntNotaCinco = numFloat//5
numFloat -= qntNotaCinco * 5

qntNotaDuas = numFloat//2
numFloat -= qntNotaDuas * 2

qntMoedaUm = numFloat//1
numFloat -= qntMoedaUm

qntMoedaCinquentaCent = numFloat//0.5
numFloat -= qntMoedaCinquentaCent * 0.5

qntMoedaVinteCincoCent = numFloat//0.25
numFloat -= qntMoedaVinteCincoCent * 0.25

qntMoedaDezCent = numFloat//0.10
numFloat -= qntMoedaDezCent * 0.1

qntMoedaCincoCent = numFloat//0.05
numFloat -= qntMoedaCincoCent * 0.05

qntMoedaUmCent = numFloat//0.01

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(qntNotaCem)))
print("{} nota(s) de R$ 50.00".format(int(qntNotaCinquenta)))
print("{} nota(s) de R$ 20.00".format(int(qntNotaVinte)))
print("{} nota(s) de R$ 10.00".format(int(qntNotaDez)))
print("{} nota(s) de R$ 5.00".format(int(qntNotaCinco)))
print("{} nota(s) de R$ 2.00".format(int(qntNotaDuas)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(qntMoedaUm)))
print("{} moeda(s) de R$ 0.50".format(int(qntMoedaCinquentaCent)))
print("{} moeda(s) de R$ 0.25".format(int(qntMoedaVinteCincoCent)))
print("{} moeda(s) de R$ 0.10".format(int(qntMoedaDezCent)))
print("{} moeda(s) de R$ 0.05".format(int(qntMoedaCincoCent)))
print("{} moeda(s) de R$ 0.01".format(int(qntMoedaUmCent)))