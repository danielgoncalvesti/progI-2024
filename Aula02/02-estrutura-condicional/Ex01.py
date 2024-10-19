"""
Exercício 01 – Crie um programa que solicita um número inteiro para o usuário.
Após isso, verifique se o número é par ou ímpar.
Crie uma função chamada eh_par que recebe um número inteiro e retorna True se o número for par e False se for ímpar.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número ímpar.
"""
numero = int(input("Digite um número: "))

def eh_par(n):
    if n % 2 == 0:
        print(f"O número {n} é par!")
        return True
    else:
        print(f"O número {n} é impar")
        return False
print(eh_par(numero))