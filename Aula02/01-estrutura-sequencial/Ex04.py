"""
Exercício 04 - Escreva um programa que leia uma temperatura em graus Celsius e a converta para Fahrenheit.
A fórmula de conversão é F = C * 9/5 + 32.

Exemplo de Entrada:
Digite uma temperatura em Celsius para conversão: 25

Exemplo de Saída:
25°C é equivalente a 77.0°F
"""
temperatura = int(input("Digite uma temperatura em Celsius para conversão para Fahrenheit: "))
Fahrenheit = float(temperatura * (9/5) + 32)
print(f"{temperatura}°C é equivalente a {Fahrenheit}°F")