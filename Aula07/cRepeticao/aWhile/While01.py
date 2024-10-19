"""
Escreva um programa que faz uma contagem regressiva de 10 até 1 e
depois imprime "Feliz Ano Novo!".
"""
import time

x = 10
while x >= 1:
    print(x)
    x -= 1
    time.sleep(1)
print("Feliz Ano Novo!!")
