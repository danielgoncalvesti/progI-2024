def contar_palavras_por_tamanho(frase):
    frase_separada = frase.split(" ")
    lista = [(palavra, len(palavra)) for palavra in frase_separada]  # Lista de tuplas
    return lista

resultado = contar_palavras_por_tamanho("Python é uma linguagem de programação incrível")

# Imprimindo no formato esperado:
for palavra, tamanho in resultado:
    print(f"{palavra}: {tamanho}")

#resultado esperado:
# Python: 6
# é: 1
# uma: 3
# linguagem: 9
# de: 2
# programação: 11
# incrível: 8