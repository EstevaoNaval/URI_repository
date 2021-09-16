from math import floor
qntCaso = int(input())

for caso in range(qntCaso):
    listLetraStr = list(input())
    
    # Primeira passada
    for indiceChr in range(len(listLetraStr)):
        if (ord(listLetraStr[indiceChr]) >= 65 and ord(listLetraStr[indiceChr]) <= 90) or (ord(listLetraStr[indiceChr]) >= 97 and ord(listLetraStr[indiceChr]) <= 122):
            listLetraStr[indiceChr] = chr(ord(listLetraStr[indiceChr]) + 3)
    # Segunda passada
    listLetraStr.reverse()
    # Terceira passada
    for indiceChr in range(floor(len(listLetraStr)/2), len(listLetraStr)): listLetraStr[indiceChr] = chr(ord(listLetraStr[indiceChr]) - 1)

    print("".join(listLetraStr))