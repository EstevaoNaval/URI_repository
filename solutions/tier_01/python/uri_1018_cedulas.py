# -*- coding: utf-8 -*-
valOriginal = int(input())

numInt = valOriginal

qntNotaCem = numInt//100
numInt -= qntNotaCem * 100

qntNotaCinquenta = numInt//50
numInt -= qntNotaCinquenta * 50

qntNotaVinte = numInt//20
numInt -= qntNotaVinte * 20

qntNotaDez = numInt//10
numInt -= qntNotaDez * 10

qntNotaCinco = numInt//5
numInt -= qntNotaCinco * 5

qntNotaDuas = numInt//2
numInt -= qntNotaDuas * 2

qntNotaUm = numInt

print(valOriginal)
print("{} nota(s) de R$ 100,00".format(qntNotaCem))
print("{} nota(s) de R$ 50,00".format(qntNotaCinquenta))
print("{} nota(s) de R$ 20,00".format(qntNotaVinte))
print("{} nota(s) de R$ 10,00".format(qntNotaDez))
print("{} nota(s) de R$ 5,00".format(qntNotaCinco))
print("{} nota(s) de R$ 2,00".format(qntNotaDuas))
print("{} nota(s) de R$ 1,00".format(qntNotaUm))