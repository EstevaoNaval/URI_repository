# -*- coding: utf-8 -*-
qntMedidaVelocidadeMotor = int(input())
listMedidaVelocidade = list(map(int, input().split()))

indiceMedidaMenor = 0
for indiceMedida in range(1, qntMedidaVelocidadeMotor):
    if listMedidaVelocidade[indiceMedida] < listMedidaVelocidade[indiceMedida - 1]: 
        indiceMedidaMenor = indiceMedida + 1
        break

print(indiceMedidaMenor)