"""
Exercício 06 – Desenvolva um programa que solicite
ao usuário o valor total de suas compras como um número decimal (float).
Se o valor informado for R$ 150,00 ou mais, aplique
automaticamente um desconto de 10%.
Exiba o valor total com desconto aplicado,
bem como o total economizado com o desconto.

Entrada:
Digite o valor total de suas compras: 200.00

Saída:
O valor total com desconto é R$ 180.00.
Você economizou R$ 20.00.
"""
compras = float(input("Digite o valor das compras: "))

if compras >= 150:
    desconto = compras/10
    print(f"O valor total com desconto é R${compras-desconto}\n"
          f"Você economizou R${desconto}")