"""
Exercício 07 – Crie um programa que solicita ao usuário
um número inteiro e verifica se é
positivo, negativo ou zero.
Utilize a estrutura elif.

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
elif n1==0:
    print(f"{n1} é igual a zero.")