"""
Exercício 08 – Crie um programa que solicita ao usuário um número de 1 a 7
e determina o dia da semana correspondente (utilizando elif).
Por exemplo, 1 representa domingo, 2 representa segunda-feira e assim por diante.

Entrada:
Digite um número de 1 a 7: 3

Saída:
3 é terça-feira.
"""
Dia = int(input("Digite um número de 1 a 7: "))

if Dia==1:
    print(f"1 é domingo.")

elif Dia==2:
    print(f"2 é segunda-feira.")

elif Dia==3:
    print(f"3 é terça-feira.")

elif Dia==4:
    print(f"4 é quarta-feira.")

elif Dia==5:
    print(f"5 é quinta-feira.")

elif Dia==6:
    print(f"6 é sexta-feira.")

elif Dia==7:
    print(f"7 é Sábado.")