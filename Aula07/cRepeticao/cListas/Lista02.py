"""
Dada uma lista de números (lista_numeros = [15, 5, 10, 60 , 50, 40]),
escreva um programa que percorre a lista e exiba o maior elemento.

Obs: Não é permitido usar a função max() para encontrar o maior elemento.
"""
lista_numeros = [15, 5, 10, 60, 50, 40]
verify = lista_numeros[0]
for x in lista_numeros[0:]:
    if x > verify:
        verify = x
print(f"O maior elemento da lista é: {verify}")