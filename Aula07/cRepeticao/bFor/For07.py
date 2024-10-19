"""
Exercício 02: Calculadora de Fatorial
Peça ao usuário um número inteiro positivo e calcule o fatorial desse número usando while.

Entrada: 4
Saída: 24 (4! = 4 * 3 * 2 * 1
Entrada: 5
Saída: 120 (5! = 5 * 4 * 3 * 2 * 1)
"""
n = int(input("Digite um número inteiro positivo: "))
fatorial = 1
cont = n
expressao = ""
while cont>0:
    fatorial = fatorial * cont
    expressao += str(cont) + " * " if cont > 1 else str(cont) + " "
    cont -= 1
print(f"{fatorial} ({n}! = {expressao.strip()})")



