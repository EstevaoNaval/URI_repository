# -*- coding: utf-8 -*-
qntBandejas = int(input())

qntCopoQuebrado = 0
for indiceBandeja in range(0, qntBandejas):
    listInputLataCopo = list(map(int, input().split()))
    qntCopoQuebrado += listInputLataCopo[1] if listInputLataCopo[0] > listInputLataCopo[1] else 0

print(qntCopoQuebrado)