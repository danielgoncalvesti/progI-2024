"""
Exercício 03 – Peça ao usuário três números inteiros
e exiba qual é o maior e qual é o menor entre eles.
Defina as funções: encontrar_maior e encontrar_menor.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8

Saída:
O maior número é 10.
O menor número é 5.

"""
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Encontrando o maior e o menor número
maior = encontrar_maior(numero1, numero2, numero3)
menor = encontrar_menor(numero1, numero2, numero3)

# Exibindo o resultado
print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")
