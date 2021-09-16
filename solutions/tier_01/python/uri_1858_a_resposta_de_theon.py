# -*- coding: utf-8 -*-
numPessoa = int(input())
listHitPointPorPessoa = list(map(int, input().split()))
print(listHitPointPorPessoa.index(min(listHitPointPorPessoa)) + 1)