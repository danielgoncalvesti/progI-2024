"""
Exercício 02 – Peça ao usuário dois números inteiros e exiba as comparações:
maior, menor, igual, diferente, maior ou igual, menor ou igual.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5

Saída:
10 é maior que 5.
10 não é menor que 5.
10 não é igual a 5.
10 é diferente de 5.
10 é maior ou igual a 5.
10 não é menor ou igual a 5.
"""
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))

if n1>n2:
    print(f"{n1} é maior que {n2}.")
else:
    print(f"{n1} não é maior que {n2}.")

if n1 < n2:
    print(f"{n1} é menor que {n2}.")
else:
    print(f"{n1} não é menor que {n2}.")

if n1==n2:
    print(f"{n1} é igual a {n2}.")
else:
    print(f"{n1} não é igual a {n2}.")

if n1!=n2:
    print(f"{n1} é diferente de {n2}.")
else:
    print(f"{n1} não é diferente de {n2}.")

if n1>=n2:
    print(f"{n1} é maior ou igual a {n2}.")
else:
    print(f"{n1} não é maior ou igual a {n2}.")

if n1<=n2:
    print(f"{n1} é menor ou igual a {n2}.")
else:
    print(f"{n1} não é menor ou igual a {n2}.")
