"""
Exercício 05 - Faça um programa que recebe uma nota (0 a 10) e mostra se o aluno está reprovado (nota abaixo de 6),
de recuperação (nota entre 6 e 7) ou aprovado (nota acima de 7).

Defina a função verificar_status_aluno que recebe a nota e retorna a
mensagem de status: reprovado, recuperação ou aprovado.

Entrada:
Digite a nota do aluno: 8

Saída:
aprovado

"""

# Solicitando a nota ao usuário
nota = float(input("Digite a nota do aluno: "))

# Verificando o status do aluno
resultado = verificar_status_aluno(nota)

# Exibindo o resultado
print(resultado)
