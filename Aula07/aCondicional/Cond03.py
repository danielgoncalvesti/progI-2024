"""
Crie um programa que verifica se um número é positivo, negativo ou zero.
Utilize elif.
"""
num1 = int(input("Digite um numero inteiro: "))

if num1>0:
    print(f"O número {num1} é positivo")
elif num1<0:
    print(f"O número {num1} é negativo")
else:
    print(f"O número {num1} é igual a 0")
