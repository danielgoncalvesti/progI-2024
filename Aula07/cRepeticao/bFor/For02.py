"""
Crie um programa que solicita ao usuário um número entre 1 a 10.
Após isso, exiba a tabuada do número digitado.
Implemente a função imprime_tabuada que recebe um número inteiro
e imprime a tabuada desse número.
"""
def imprime_tabuada(numero: int):
    for i in range(1, 11):
        print(f"{numero}*{i} = {numero*i}")

def main():
    n = int(input("Digite um número para ver sua tabuada: "))
    imprime_tabuada(n)

if __name__ == "__main__":
    main()