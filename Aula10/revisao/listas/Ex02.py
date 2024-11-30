"""
Contagem de Elementos Únicos
Receba uma lista e conte quantos elementos únicos ela contém.

Entrada: [1, 2, 2, 3, 4, 4, 5]
Saída: 5
"""

elementos = [1, 2, 2, 3, 4, 4, 5]
elementos_nao_repetidos = []
contador = 0

for e in elementos:
    if e not in elementos_nao_repetidos:
        elementos_nao_repetidos.append(e)
        contador += 1
        
print(contador)     