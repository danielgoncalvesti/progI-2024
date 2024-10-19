"""
Crie um programa que pede ao usuário para digitar números positivos e soma esses números.
O loop termina quando o usuário digita o número 0, e o programa exibe a soma final.
"""
num = 0
soma = 0

while True:
    num = int(input("Digite um número: "))
    if num>0:
        soma = num + soma
    elif num == 0:
        print(f"O valor das somas foram: {soma}")
        break