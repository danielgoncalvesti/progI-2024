"""
Gere uma senha aleatória de 6 caracteres alfanuméricos.

Dica: use a função random.choice() para escolher um caractere aleatório de uma string.
Use:
import random
caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
letra_aleatoria = random.choice(caracteres)
"""
import random
caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"

senha = ""
for s in range(0,6):
    s = random.choice(caracteres)
    senha += s
print(senha)


