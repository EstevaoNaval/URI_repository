listInputDadoGasolinaAlcool = list(map(float, input().split()))

print("G" if listInputDadoGasolinaAlcool[0]/listInputDadoGasolinaAlcool[2] >= listInputDadoGasolinaAlcool[1]/listInputDadoGasolinaAlcool[3] else "A")