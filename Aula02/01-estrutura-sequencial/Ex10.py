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
Num1 =int(input("Digite um numero: "))
Num2 = int(input("Digite um numero: "))
Num3 = int(input("Digite um numero: "))

print(f"Todos os números são iguais? {Num1 == Num2 and Num2 == Num3:}")
print(f"Todos os numeros são diferentes? {Num1 != Num2 and Num2 != Num3 and Num1 != Num3}")
print(f"Algum numero é maior que 50!: {Num1 > 50 or Num2>50 or Num3>50}")