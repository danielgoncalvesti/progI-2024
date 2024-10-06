"""
Exercício 08 – Crie um programa que solicita duas notas (n1 e n2)
e calcule a média aritmética dessas notas.
Exiba o resultado usando duas casas decimais.

Entrada:
Digite a primeira nota: 8
Digite a segunda nota: 7

Saída:
A média aritmética é: 7.50
"""
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

print(f"A média das notas é: {media:.2f}")