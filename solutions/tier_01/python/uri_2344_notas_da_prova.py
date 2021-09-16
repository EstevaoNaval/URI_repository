# -*- coding: utf-8 -*-
notaNumerica = int(input())

if notaNumerica == 0: notaConceito = "E"
elif notaNumerica >= 1 and notaNumerica <= 35: notaConceito = "D"
elif notaNumerica >= 36 and notaNumerica <= 60: notaConceito = "C"
elif notaNumerica >= 61 and notaNumerica <= 85: notaConceito = "B"
else: notaConceito = "A"

print(notaConceito)