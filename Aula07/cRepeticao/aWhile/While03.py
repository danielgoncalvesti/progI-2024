"""
Crie um programa que calcula a soma dos primeiros 100 números naturais (de 1 a 100).
O programa deve exibir a soma final.
"""
x = 1
soma = 0
while x <= 100:
    soma = x + soma
    x+=1
print(soma)