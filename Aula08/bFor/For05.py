#Ex. 05: Contar Caracteres em uma Lista de Palavras
# Dada uma lista de palavras, use um laço `for` para contar o número total de caracteres em todas as palavras.
# Dica: Use a função `len()` para contar o número de caracteres em cada palavra.

strings = ["uva","abacaxi","maça","banana"]
soma = 0

for i in strings:
    soma += len(i)

print(soma)
