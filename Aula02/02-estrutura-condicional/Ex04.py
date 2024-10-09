"""
Exercício 04 - Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.
Definir as funções eh_positivo, eh_negativo e eh_zero.
Digite um número inteiro: 5

Saída:
5 é um número positivo.

"""
numero = int(input("Digite um número inteiro: "))

def eh_positivo(n):
    return n > 0
def eh_negativo(n):
    return n < 0
def eh_zero(n):
    return n == 0

if eh_positivo(numero):
    print(f"{numero} é um número positivo.")
elif eh_negativo(numero):
    print(f"{numero} é um número negativo.")
elif eh_zero(numero):
    print(f"{numero} é igual a zero.")


