"""
Exercício 02 – Peça ao usuário dois números inteiros e exiba as comparações:
maior, menor, igual.

Crie as funções: eh_menor, eh_igual.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5

Saída:
10 é maior que 5.
10 não é menor que 5.
10 não é igual a 5.
"""
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

def eh_maior(n1, n2):
    if n1 > n2:
        return f"{n1} é maior que {n2}."
    else:
        return f"{n1} não é maior que {n2}."

def eh_menor(a, b):
    if a < b:
        return f"{a} é menor que {b}"
    else:
        return f"{numero1} não é menor que {numero2}"

def eh_igual(number1, number2):
    if number1 == number2:
        return f"{number1} é igual a {number2}"
    else:
        return f"{number1} não é igual a {number2}"

print(eh_maior(numero1,numero2))
print(eh_menor(numero1,numero2))
print(eh_igual(numero1,numero2))