# -*- coding: utf-8 -*-
qte = int(input())
lista = {}
for i in range(qte):
	v = int(input())
    
	if(v in lista):
		lista[v] += 1
	else:
		lista[v] = 1


chaves = lista.keys()
chaves = sorted(chaves)

for k in chaves:
	print("{} aparece {} vez(es)".format(k,lista[k]))