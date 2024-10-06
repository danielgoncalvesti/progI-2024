"""
Exercício 09 – Crie um programa que recebe o preço de venda do produto e custo do produto.
Calcule o valor do lucro e exiba com duas casas decimais.

Entrada:
Digite o preço de venda: 100
Digite o custo do produto: 50

Saída:
O lucro é de: 50.00
"""
venda = float(input("Digite o valor da venda: "))
custo = float(input("Digite o custo do produto: "))

lucro  = venda - custo

print(f"O lucro foi de: R${lucro:.2f}")