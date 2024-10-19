"""
Exercício 03 - Modifique o exercício anterior adicionando o cálculo da margem do lucro em %.
Exiba o valor com duas casas decimais.

Entrada:
Digite o preço de venda: 100
Digite o custo do produto: 80

Saída:
O lucro é de: 20.00
A margem de lucro é de: 20.00%
"""
venda = float(input("Digite o valor da venda: "))
custo = float(input("Digite o custo do produto: "))

lucro  = venda - custo
margem = (lucro/custo) * 100

print(f"O lucro foi de: R${lucro:.2f}")
print(f"A margem de lucro foi de: {margem:.2f}%")