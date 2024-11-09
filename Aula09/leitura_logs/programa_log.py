caminho_arquivo = "server.log"
arquivo = open(caminho_arquivo, "r")

#menu
while True:
    print("-"*40)
    print("Menu de opções:")
    print("1 - Exibir todas as linhas")
    print("2 - Exibir linhas que contém um termo")
    print("3 - Exibir a contagem dos tipos de logs")
    print("0 - Sair")
    print("-"*40)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        arquivo.seek(0)
        for linha in arquivo:
            pass # implementar
    elif opcao == 2:
        termo = input("Digite o termo que deseja buscar: ")
        arquivo.seek(0) # mover o cursor para o inicio do arquivo
        for linha in arquivo:
            pass # implementar

    elif opcao == 3:
        arquivo.seek(0)

    elif opcao == 0:
        break
    else:
        print("Opção inválida")


arquivo.close()


