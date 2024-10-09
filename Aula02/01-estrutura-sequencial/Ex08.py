"""
Exercício 08 – Crie um programa que solicita dois números para o usuário,
e exibe a soma, subtração, multiplicação, divisão e resto da divisão entre eles.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 3

Saída:
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 * 3.0 = 30.0
10.0 / 3.0 = 3.33
10.0 % 3.0 = 1.0
"""
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

print(f"{num1} + {num2} = {num1+num2}\n"
      f"{num1} - {num2} = {num1-num2}\n"
      f"{num1} * {num2} = {num1*num2}\n"
      f"{num1} / {num2} = {num1/num2}\n"
      f"{num1} % {num2} = {num1%num2}\n")

