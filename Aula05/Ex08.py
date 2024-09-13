"""
Exercício 08 – Crie um programa que solicita ao usuário um número de 1 a 7 e
determina o dia da semana correspondente (utilizando elif).
Por exemplo, 1 representa domingo, 2 representa segunda-feira e assim por diante.
Entrada:
Digite um número de 1 a 7: 4
Saída:
Quarta-feira

Entrada:
Digite um número de 1 a 7: 8
Saída:
Número inválido. Por favor, digite um número de 1 a 7.
"""
def determinar_dia_da_semana(numero):
    # implemente a função (remover o pass)
    pass

def main():
    try:
        numero = int(input("Digite um número de 1 a 7: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    # Determina o dia da semana correspondente
    dia_da_semana = determinar_dia_da_semana(numero)

    # Exibe o resultado
    print(dia_da_semana)

if __name__ == '__main__':
    main()
