# -*- coding: utf-8 -*-
from fractions import Fraction

listNumeradorDivisor = list(map(int, input().split()))
somaDivisor = str(Fraction(listNumeradorDivisor[0],listNumeradorDivisor[1]) + Fraction(listNumeradorDivisor[2],listNumeradorDivisor[3]))
if "/" in somaDivisor: print(somaDivisor.replace("/"," "))
else: print(somaDivisor + " 1")