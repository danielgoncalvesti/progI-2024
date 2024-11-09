caminho_arquivo = r'C:\Users\Kaua Deja\Desktop\progI-2024\Aula09\leitura_logs\server.log'
arquivo = open(caminho_arquivo, "r")

contador_error = 0
contador_warning = 0
contador_info = 0

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
            print(linha.strip())
            pass
    elif opcao == 2:
        termo = input("Digite o termo que deseja buscar: ")
        arquivo.seek(0) # mover o cursor para o inicio do arquivo
        for linha in arquivo:
            if termo in linha:
                print(linha)
        pass
    elif opcao == 3:
        arquivo.seek(0)
        for linha in arquivo:
            if "ERROR" in linha:
                contador_error +=1
            elif "WARNING" in linha:
                contador_warning +=1
            else:
                contador_info +=1
        print(contador_info)
        print(contador_error)
        print(contador_warning)
    
    elif opcao == 0:
        break
    else:
        print("Opção inválida")


arquivo.close()


