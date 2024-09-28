"""
Crie um programa que verifica se um número é positivo, negativo ou zero.
Utilize elif.
"""
NUM1 = int(input("Digite um numero inteiro: "))

if NUM1>0:
    print(f"O número {NUM1} é positivo")
elif NUM1<0:
    print(f"O número {NUM1} é negativo")
else:
    print(f"O número {NUM1} é igual a 0")