# Ex. 04: Listar Números Pares e Ímpares
# Use um laço `for` para separar os números pares e ímpares em duas listas diferentes a partir da lista `numeros`.

# Inicializa a lista `numeros` com os números de 1 a 10.
numeros = list(range(1, 11))
lista_par = []
lista_impar = []

for i in numeros:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f"Os números impares: {lista_impar}")
print(f"Os números pares: {lista_par}")
