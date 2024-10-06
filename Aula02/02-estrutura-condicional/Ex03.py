"""
Exercício 03 – Peça ao usuário três números inteiros
e exiba qual é o maior e qual é o menor entre eles.
Defina as funções: encontrar_maior e encontrar_menor.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8

Saída:
O maior número é 10.
O menor número é 5.

"""
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Encontrando o maior e o menor número
def encontrar_maior(n1, n2, n3):
    if n1 > n2 and n1> n3:
        return f"{n1} é o maior!"
    elif n2 > n1 and n2 > n3:
        return f"{n2} é o maior!"
    elif n3>n1 and n3>n2:
        return f"{n3} é o maior!"

def encontrar_menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return f"{n1} é o menor!"
    elif n2 < n1 and n2 < n3:
        return f"{n2} é o menor!"
    elif n3 < n1 and n3<n2:
        return f"{n3} é o menor!"

# Exibindo o resultado
print(encontrar_maior(numero1,numero2,numero3))
print(encontrar_menor(numero1,numero2,numero3))

