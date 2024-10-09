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
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

ambos_pares = (num1 % 2 == 0) and (num2 % 2 == 0) 
ambos_impares = (num1 % 2 != 0) and (num2 % 2 != 0)
um_par_outro_impar = ((num1 % 2 == 0) and (num2 % 2 != 0)) or ((num1 % 2 != 0) and (num2 % 2 == 0))

print(f"Ambos são pares? {ambos_pares}")
print(f"Ambos são ímpares? {ambos_impares}")
print(f"Um é par e o outro ímpar? {um_par_outro_impar}")
