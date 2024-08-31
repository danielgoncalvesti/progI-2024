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
def eh_maior(a, b):
    return a > b

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Exibindo o resultado
if eh_maior(numero1, numero2):
    print(f"{numero1} é maior que {numero2}.")
else:
    print(f"{numero1} não é maior que {numero2}.")

# continue com as outras comparações