def IsOverflow(valOperacao, intMaximo): return True if valOperacao > intMaximo else False

numIntMaximo = int(input())
resultOperacao = eval(input())

print("OVERFLOW" if IsOverflow(resultOperacao, numIntMaximo) else "OK")