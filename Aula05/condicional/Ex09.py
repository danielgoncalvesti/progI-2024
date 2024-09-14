"""
Exercício 09 - Crie um programa que solicite idade e confirmação
se é cidadão brasileiro. Se for maior que 18 e brasileiro
exibe "Elegível para votar." caso contrário
"Não elegível para votar."

Entrada:
Digite sua idade: 22
É cidadão brasileiro? (S/N): S

Saída:
Elegível para votar.

Entrada:
Digite sua idade: 15
Saída:
Não elegível para votar.
"""
def verificar_elegibilidade_voto(idade, cidadao_brasileiro):
    pass

def main():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        cidadao_brasileiro = input("É cidadão brasileiro? (S/N): ").upper().strip()

        resultado = verificar_elegibilidade_voto(idade, cidadao_brasileiro)
        print(resultado)
    else:
        print("Não elegível para votar.")

if __name__ == "__main__":
    main()

