"""
Exercício 04 - Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.
Entrada:
Digite um número inteiro: 5

Saída:
5 é um número positivo.
"""
n1 = int(input("Digite um número inteiro: "))

if n1>0:
    print(f"{n1} é um número positivo.")
elif n1<0:
    print(f"{n1} é um número negativo.")
else:
    print(f"{n1} é igual a zero.")