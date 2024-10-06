"""
Exercício 10 - Peça ao usuário três números e verifique se todos são iguais,
se todos são diferentes e se algum deles é maior que 50.

Entrada:
Digite o primeiro número: 25
Digite o segundo número: 50
Digite o terceiro número: 75

Saída:
Todos os números são iguais? False
Todos os números são diferentes? True
Algum número é maior que 50? True
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

todos_iguais = (num1 == num2) and (num2 == num3) and (num1 == num3)
todos_diferentes = (num1 != num2) and (num2 != num3) and (num1 != num3)
algum_maior_que_50 = (num1 > 50) or (num2 > 50) or (num3 > 50)

print(f"Todos os números são iguais? {todos_iguais}")
print(f"Todos os números são diferentes? {todos_diferentes}")
print(f"Algum número é maior que 50? {algum_maior_que_50}")
