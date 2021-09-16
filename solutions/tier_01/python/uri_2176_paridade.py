# -*- coding: utf-8 -*-
mensagem = input()
print(mensagem + "0" if mensagem.count("1") % 2 == 0 else mensagem + "1")