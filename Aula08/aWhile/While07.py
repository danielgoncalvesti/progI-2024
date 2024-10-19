# Ex 07 - Dada a lista `letras`, converta-a em uma string.

letras = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'é', ' ', 'm', 'u', 'i', 't', 'o', ' ', 'l', 'e', 'g', 'a', 'l']


# Solução com While
# i = 0
# string = ''
# while i < len(letras):
#     string += letras[i]
#     i += 1
#
# print(string)
#
# # Solução com For
# string = ''
# for letra in letras:
#     string += letra
# print(string)


# Solução com Join
string = ''.join(letras)
print(string)
