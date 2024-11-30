texto = """
Na programação de computadores, uma string é simplesmente uma sequência de caracteres. 
Frequentemente, as strings são usadas para representar palavras ou frases, 
mas elas também podem representar qualquer sequência de caracteres, incluindo números e símbolos. 
Manipular strings é uma habilidade essencial para qualquer programador.
"""

lista = texto.replace(',','').replace('.', '').replace('\n', '').split(" ")
contador = 0
tamanho_palavra = ""
lista_invertida = []
texto_caracter_invertido = ""
ultimo_element = len(texto) -1
indice = len(lista) -1
print(lista)

for palavra in lista:
    palavra_mais_longa = ""
    contador += 1

    if len(palavra) > len(palavra_mais_longa):
        palavra_mais_longa = palavra

while (indice >= 0):
    lista_invertida.append(lista[indice])
    indice = indice -1
for posicao in range(ultimo_element, -1, -1):
    texto_caracter_invertido = texto_caracter_invertido + texto[posicao]


# Ex 1. Calcule e imprima o número de palavras no texto.
print(f"Ex 1: Número de Palavras: {contador}")

# Ex 2. Encontre e imprima a palavra mais longa no texto.
print(f"Ex 2: Palavra Mais Longa: {palavra_mais_longa}")

# Ex 3. Inverta a ordem das palavras no texto e imprima o resultado.
# Exemplo: "Olá, mundo!" -> "mundo! Olá,"
print(f"Ex 3: Invertendo a Ordem das Palavras: {lista_invertida}")


# Ex 4. Inverta a ordem dos caracteres no texto e imprima o resultado.
# Exemplo: "Olá, mundo!" -> "!odnum ,álO"
print(f"Ex 4: Invertendo a Ordem dos Caracteres: {texto_caracter_invertido}")


# Ex 5. Use um laço 02-for para listar todas as palavras no texto que começam com uma letra maiúscula.
# Utilize a função `isupper()`.
print("Ex 5: Palavras que Começam com Letra Maiúscula: ")


# Ex 6. Use um laço 02-for para encontrar e imprimir a primeira palavra no texto com mais de 10 letras.
print("Ex 6: Primeira Palavra com Mais de 10 Letras: ")


# Ex 7. Utilize um laço para contar quantas vezes a vírgula aparece no texto.
print("Ex 7: Contagem de Vírgulas: ")


# Ex 8. Utilize um laço 02-for para contar quantas vezes cada vogal (a, e, i, o, u) aparece no texto.
print("Ex 8: Contagem de Vogais: ")


# Ex 9. Encontrar e Contar Palavras que Terminam com 's'
print("Ex 9: Palavras que Terminam com 's': ")


# Ex 10. Encontrar e Contar Palavras que Contêm 'a'
print("Ex 10: Palavras que Contêm 'a': ")


# Ex 11. Contar o Número de Sentenças no Texto
print("Ex 11: Contagem de Sentenças: ")


# Ex 12. Reverter a Ordem das Sentenças no Texto
# Utilize um laço para inverter a ordem das sentenças no texto.
# Considere uma sentença como qualquer sequência de caracteres terminada por um ponto.
print("Ex 12: Invertendo a Ordem das Sentenças: ")


# Ex 13. Identificar e Contar Palavras Que Começam e Terminam Com a Mesma Letra
# Use um laço 02-for para identificar e contar quantas palavras no texto começam e terminam com a mesma letra.
print("Ex 13: Palavras que Começam e Terminam com a Mesma Letra: ")

# Ex 14. Exibir todas as palavras maiores com mais de 2 caracteres. Imprimir a palavra somente uma vez.
print("Ex 14: Palavras com Mais de 2 Caracteres: ")