"""
Adivinhe o Número
Implemente um jogo simples onde o programa escolhe aleatoriamente um número entre 1 e 100,
e o usuário tenta adivinhar esse número.
Após cada tentativa, o programa informa se o palpite está correto,
é muito alto, ou muito baixo, continuando até o usuário acertar.
"""
import random
numero_secreto = random.randint(1, 100)

while True:
    tentativa = int(input("Digite um número: "))
    if numero_secreto != tentativa:
        print(numero_secreto)
        if numero_secreto > tentativa:
            print("É muito baixo, tente novamente!!")
        else:
            print("É muito alto, tente novamente!!")
    else:
        print("Parabéns, você acertou!!")
        break