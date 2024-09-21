"""
Exercício 06 - Crie um programa onde o usuário deve adivinhar
um número gerado aleatoriamente entre 1 a 100. A cada tentativa,
exiba se ele deve tentar um número maior ou menor.
Quando o número for acertado, exiba o número de tentativas.

Exemplo:
Digite um número: 50
Tente um número maior.
Digite um número: 80
Tente um número menor.
Digite um número: 61
Parabéns! Você acertou o número em 3 tentativas.
"""

import random
numero_secreto = random.randint(1, 100)