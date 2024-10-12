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
count = n
expressao = ""
while n>0:
    for i in range(n,1, -1):
        fatorial = i*fatorial
        expressao = expressao + str(count) + " * "
        count -= 1
    break
print(f"{fatorial} ({n}! = {expressao}", end ="1)")

