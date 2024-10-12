"""
Crie um programa que pede ao usuário para digitar números positivos e soma esses números.
O loop termina quando o usuário digita o número 0, e o programa exibe a soma final.

Entrada:
Digite um número: 5
Digite um número: 3
Digite um número: 2
Digite um número: 0

Saída:
A soma dos números é 10
"""
soma = 0
while True:
    num = int(input("Digite um numero: "))
    if num == 0:
        break
    else:
        soma = num + soma
print(f"A soma do numeros é {soma}")