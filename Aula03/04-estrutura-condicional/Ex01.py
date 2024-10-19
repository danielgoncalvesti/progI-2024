"""
Exercício 01 – Crie um programa que solicita um número inteiro para o usuário.
Após isso, verifique se o número é par ou ímpar.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número ímpar.
"""
n1 = int(input("Digite o primeiro numero: "))
if n1 % 2 == 0:
    print(f"O número {n1} é par!")
else:
    print(f"O número {n1} é impar")