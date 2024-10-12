"""
Ocorrências de um número:
Crie um programa que percorre a lista_numeros
e exiba quantas vezes cada número aparece na lista.
"""
lista = [5,1,2,3,3,4,3,2,5]
ocorrencias = {}
for x in lista[0:]:
    if x in ocorrencias:
        ocorrencias[x] += 1
    else:
        ocorrencias[x] = 1
for x, contagem in ocorrencias.items():
    print(f" A quantidade de ocorrencias do numero: {x} foi: {contagem}")




