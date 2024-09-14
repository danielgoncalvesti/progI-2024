"""
Exercício 06 - Crie um programa que receba o valor total das compras (float).
Se for R$ 150,00 ou mais, aplique um desconto de 10%.
Exiba o valor final com desconto e o total economizado.

Entrada:
Digite o valor total das suas compras (em R$): 200

Saída:
Valor total: R$ 200.00
Valor com desconto: R$ 180.00
Desconto: R$ 20.00
"""
def calcular_desconto(valor_total):
    # implemente a função (remover o pass)
    pass

def main():
    valor_total = float(input("Digite o valor total das suas compras (em R$): "))

    # Verifica se o valor é elegível para o desconto
    if valor_total >= 150.00:
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        # Termine de implementar o código


    print(f"Valor total: R$ {valor_total:.2f}")
    print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")

if __name__ == '__main__':
    main()

