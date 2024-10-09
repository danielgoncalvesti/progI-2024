"""
Exercício 14 – Peça ao usuário dois números e verifique se o primeiro é divisível pelo segundo.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 3

Saída:
O primeiro número é divisível pelo segundo? False
"""
number1 = int(input("Digite um numero: "))
number2 = int(input("Digite um numero: "))

def eh_divisivel(n1, n2):
    if n1%n2 == 0:
        return True
    else:
        return False

print(f"O primeiro número é divisível pelo segundo? {eh_divisivel(number1,number2)}")
