"""
Exercício 01 – Peça ao usuário dois números e verifique se ambos são pares, se ambos são ímpares e se um é par e o outro ímpar.
Defina uma função chamada ehPar.
"""
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

def eh_par(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return "Os números são pares!"
    elif n1 % 2 == 1 and n2 % 2 == 1:
        return "São impares!"
    else:
        return "um é par e o outro ímpar"
print(eh_par(numero1, numero2))