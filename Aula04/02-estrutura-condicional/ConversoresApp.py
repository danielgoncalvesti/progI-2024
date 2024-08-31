import time as Thread
import subprocess

def clear_console():
    print("\n" * 100)  # Imprime 100 linhas em branco

def spinner():
    print("Convertendo", end="")
    for i in range(3):
        Thread.sleep(0.5)
        print(".", end="")
    print()
    print("Resultado:")
    print("-" * 30)


def show_logo():
    print("""
      ____                                          _                
     / ___|___  _ ____   _____ _ __ ___  ___  _ __ / \   _ __  _ __  
    | |   / _ \| '_ \ \ / / _ \ '__/ __|/ _ \| '__/ _ \ | '_ \| '_ \ 
    | |__| (_) | | | \ V /  __/ |  \__ \ (_) | | / ___ \| |_) | |_) |
     \____\___/|_| |_|\_/ \___|_|  |___/\___/|_|/_/   \_\ .__/| .__/ 
                                                        |_|   |_|     
       """)
def menu():
    print("-" * 30)
    print("Escolha uma opção:")
    print("1. Converter temperatura (Celsius para Fahrenheit)")
    print("2. Converter distância (Quilômetros para Milhas)")
    print("3. Converter peso (Quilogramas para Libras)")
    print("4. Sair")
    print("-" * 30)


def celsius_para_fahrenheit(celsius):
    TODO # implementar a função

def converter_km_para_milhas(quilometros):
    TODO # implementar a função

def quilogramas_para_libras(quilogramas):
    TODO # implementar a função


while True:
    show_logo()
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        temperatura_fahrenheit = celsius_para_fahrenheit(celsius)
        spinner()
        print(f"{celsius}°C é igual a {temperatura_fahrenheit:.2f}°F")
        print("-" * 30)
    elif opcao == '2':
        km = float(input("Digite a distância em Quilômetros: "))
        milhas =  converter_km_para_milhas(km)
        spinner()
        print(f"{km} km é igual a {milhas:.2f} milhas")
        print("-" * 30)
    elif opcao == '3':
        quilogramas = float(input("Digite o peso em Quilogramas: "))
        libras = quilogramas_para_libras(quilogramas)
        spinner()
        print(f"{quilogramas} kg é igual a {libras:.2f} libras")
        print("-" * 30)
    elif opcao == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
    print()
    input("\nPressione Enter para continuar...")
    clear_console()
