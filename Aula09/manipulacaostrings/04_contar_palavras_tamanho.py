# def contar_palavras_por_tamanho(frase):
#     return ""


# contar_palavras_por_tamanho("Python é uma linguagem de programação incrível")

#resultado esperado:
# Python: 6
# é: 1
# uma: 3
# linguagem: 9
# de: 2
# programação: 11
# incrível: 8

texto = "Python e uma linguagem de programação incrível"

nova_lista = texto.replace(",","").split(" ")

for palavra in nova_lista:
    tamanho = len(palavra)
    print(f"{palavra}: {tamanho}")