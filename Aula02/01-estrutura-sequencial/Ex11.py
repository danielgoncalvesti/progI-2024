"""
Exercício 11 – Peça ao usuário dois números e verifique se ambos são pares,
se ambos são ímpares e se um é par e o outro ímpar.

Entrada:
Digite o primeiro número: 4
Digite o segundo número: 7

Saída:
Ambos são pares? False
Ambos são ímpares? False
Um é par e o outro ímpar? True
"""
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

print(f"Ambos são pares: {num1%2==0 and num2%2 == 0}")
print(f"Ambos são impares: {num1%2 == 1 and num2%2 == 1}")
print(f"Um par e o outro é impar: {num1%2==0 and num2%2 == 1 or num1%2 == 1 and num2%2 == 0}")
