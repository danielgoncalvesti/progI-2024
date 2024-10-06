"""
Exercício 03 – Peça ao usuário três números inteiros
e exiba qual é o maior e qual é o menor entre eles.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8

Saída:
O maior número é 10.
O menor número é 5.
"""
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))

if n1 > n2 and n1> n3:
    print(f"{n1} é o maior!")
elif n2 > n3 and n2> n3:
    print(f"{n2} é o maior!")
else:
    print(f"{n3} é o maior!")

if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor!")
elif n2 < n3 and n2 < n3:
    print(f"{n2} é o menor!")
else:
    print(f"{n3} é o menor!")
