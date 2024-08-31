def calcular_desconto(valor_total):
    return valor_com_desconto, desconto

# Solicita o valor total das compras ao usuário
valor_total = float(input("Digite o valor total das suas compras (em R$): "))

# Verifica se o valor é elegível para o desconto
if valor_total >= 150.00:
    valor_com_desconto, desconto = calcular_desconto(valor_total)
    # Termine de implementar o código
