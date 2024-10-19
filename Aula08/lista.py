lista = [0,-1,4,-3,5,-2,0,7]
negativos = []
positivos = []
zeros = []

for i in lista:
    if i == 0:
        zeros.append(i)
    elif i > 0:
        positivos.append(i)
    else:
        negativos.append(i)

print(f"{negativos}\n{positivos}\n{zeros}\n")