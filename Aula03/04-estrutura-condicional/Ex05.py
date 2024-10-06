"""
Exercício 05 - Faça um programa que recebe uma nota (0 a 10) e mostra se o aluno está reprovado (nota abaixo de 6),
de recuperação (nota entre 6 e 7) ou aprovado (nota acima de 7).

Entrada:
Digite a nota do aluno: 8

Saída:
O aluno está aprovado.
"""
n = int(input("Digite a nota do aluno: "))
if n > 7:
    print(f"O aluno foi aprovado")
elif n == 6 or n == 7:
    print(f"O aluno ficou de recuperação")
else:
    print(f"O aluno foi reprovado")