"""
Crie um programa que solicita ao usuário um número entre 1 a 10.
Após isso, exiba a tabuada do número digitado.
Implemente a função imprime_tabuada que recebe um número inteiro
e imprime a tabuada desse número.
"""
def imprime_tabuada(numero: int):
    multiplicador = 1
    while multiplicador < 11:
        print(f"{numero} X {multiplicador} = {numero*multiplicador}")
        multiplicador += 1

def main():
    n = int(input("Digite um número para ver sua tabuada: "))
    imprime_tabuada(n)

main()