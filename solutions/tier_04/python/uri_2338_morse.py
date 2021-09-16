# -*- coding: utf-8 -*-
qntTextoMorse = int(input())
dictCodMorse = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z"}

for textoMorse in range(qntTextoMorse):
    listPalavraMorse = list(map(str, input().split("...")))
    textoTraduzido = ""
    for palavra in listPalavraMorse:
        listCodLetras = palavra.split(".")
        codMorse = ""

        for codLetra in listCodLetras:
            if codLetra == "=": codMorse += "."
            elif codLetra == "===": codMorse += "-"
        try: textoTraduzido += dictCodMorse[codMorse]
        except KeyError: textoTraduzido += " "
    print(textoTraduzido)