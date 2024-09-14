"""
Exercício 07 - Escreva um programa que recebe o valor total
e aplica descontos em compras:
-5% para compras até ou igual a R$100,
-10% para compras acima de R$100 até R$500, e
-15% para compras acima de R$500.
Exiba o valor original, o valor do desconto e o valor final.

Entrada:
Digite o valor total das suas compras (em R$): 200

Saída:
Valor total: R$ 200.00
Valor com desconto: R$ 180.00
Desconto: R$ 20.00
"""
def calcular_desconto(valor_total):
    # implemente a função (remover o pass),
    # a função deve retornar o valor com desconto (float) e o valor do desconto (float)
    pass

def main():
    # Entrada do valor total das compras
    valor_total = float(input("Digite o valor total das suas compras (em R$): "))

    valor_com_desconto, desconto = calcular_desconto(valor_total)

    # Exibe o resultado
    print(f"Valor total: R$ {valor_total:.2f}")
    print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")

if __name__ == '__main__':
    main()
