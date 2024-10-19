# Ex. 03: Encontrar o Menor Número em uma Lista
# Dada a lista `numeros`, use um laço `for` para encontrar o menor número na lista.

numeros = [1,10,100,100000]
menor = 100


for i in numeros:
    if i <= menor:
        menor = i
        print(f"O menor é o {i}")
    pass
