modo = input("Digite decrypt ou encrypt: ")
palavra = input("Digite uma palavra:")
deslocamento = int(input("Digite um número de deslocamento: "))

alfabeto_min = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mai = alfabeto_min.upper()
def letra_cifrada(ch, num_deslocamento):
    palavra_cifrada = ""
    for i in range(len(ch)):
        letra = ch[i]
        if modo == "encrypt":
            if letra in alfabeto_min:
                    encontrar_indice = alfabeto_min.index(letra)
                    cifra = (encontrar_indice + num_deslocamento) % 26
                    novo_caracter = alfabeto_min[cifra]
                    palavra_cifrada += novo_caracter
            elif letra in alfabeto_mai:
                encontrar_indice = alfabeto_mai.index(letra)
                cifra = (encontrar_indice + num_deslocamento) % 26
                novo_caracter = alfabeto_mai[cifra]
                palavra_cifrada += novo_caracter
            else:
                print("Erro inesperado")
        elif modo == "decrypt":
                if letra in alfabeto_min:
                    encontrar_indice = alfabeto_min.index(letra)
                    cifra = (encontrar_indice - num_deslocamento) % 26
                    novo_caracter = alfabeto_min[cifra]
                    palavra_cifrada += novo_caracter
                elif letra in alfabeto_mai:
                    encontrar_indice = alfabeto_mai.index(letra)
                    cifra = (encontrar_indice - num_deslocamento) % 26
                    novo_caracter = alfabeto_mai[cifra]
                    palavra_cifrada += novo_caracter
                else:
                    print("Erro inesperado")
        else:
            print("O modo selecionado não existe!")
    return palavra_cifrada

resultado = letra_cifrada(palavra, deslocamento)
print(resultado)