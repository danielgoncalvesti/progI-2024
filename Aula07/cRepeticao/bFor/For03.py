"""
Crie um programa que calcula a soma dos primeiros 100 números naturais (de 1 a 100).
O programa deve exibir a soma final.
"""
soma = 0
for x in range(0,101):
    soma = x + soma
print(soma)