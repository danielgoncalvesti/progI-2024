# Ex. 01: Criar e Preencher uma Lista
# Crie uma lista chamada `numeros` e use um laço `while` para adicionar os números de 1 a 10 nela.

numeros = []
contador = 0

while len(numeros) < 10:
    contador += 1
    print(contador)
    numeros.append(contador)

print(numeros)