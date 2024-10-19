lista =[]
while True:
    nome = input("Digite uma palavra ou digite (S) para sair: ")
    if nome == "S":
        print("Saindo...")
        break
    else:
        nova_lista = lista.append(nome.lower())
print(f"Você digitou a lista: {lista} com tamanho {len(lista)}")