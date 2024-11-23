# Função de Comparação de Strings Ignorando Maiúsculas/Minúsculas
# Descrição: Crie uma função chamada comparar_strings que recebe duas strings como parâmetros e retorna True
# se as strings forem iguais, ignorando maiúsculas e minúsculas.

def comparar_strings(s1, s2):
    s1_f = s1.upper()
    s2_f = s2.upper()
    if s1_f == s2_f:
        return True
    else:
        return False

print(comparar_strings("Python", "python"))  # True
print(comparar_strings("Python", "Java"))  # False
