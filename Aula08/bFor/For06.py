# Ex 06: Concatenar Strings com Separador
# Dada uma lista de palavras, use um laço `for` para concatená-las em uma única string, separadas por traços.

list = ["hello", "world"]
#palavras = "-".join(list)
resultado = ""
posicao = 0

for palavra in list:
    if posicao == 0:
        resultado = palavra
    else:
        resultado += "-" + palavra
    posicao += 1
print(resultado)