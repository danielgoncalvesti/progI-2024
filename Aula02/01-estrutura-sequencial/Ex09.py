"""
Exercício 09 – Crie um programa que solicite ao usuário a entrada de um número inteiro.
O programa deve calcular e exibir os seguintes resultados:

O dobro do número.
O triplo do número.
O quadrado do número.
O cubo do número.
A metade do número.

Entrada:
Digite um número inteiro: 4

Saída:
O dobro de 4 é 8.
O triplo de 4 é 12.
O quadrado de 4 é 16.
O cubo de 4 é 64.
A metade de 4 é 2.0.

"""
numero = int(input("Digite um numero: "))
print(f"O dobro do número {numero} é {numero*2}\n"
      f"O triplo do número {numero} é {numero*3}\n"
      f"O quadrado do número {numero} é {numero**2}\n"
      f"O cubo de {numero} é {numero**3}\n"
      f"A metade de {numero} é {numero/2}")