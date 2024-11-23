# Função de Contagem de Palavras
# Descrição: Crie uma função chamada contar_palavras que recebe uma string como parâmetro e
# retorna o número de palavras na string.

def contar_palavras(frase):
    frase_formatada = frase.replace(",", "").replace(".", "")
    frase_separada = frase_formatada.split(" ")
    tamanho_frase = len(frase_separada)
    return tamanho_frase


frase = "O sucesso não é determinado por quantas vezes você ganha, mas por como você joga na semana após a derrota."
print(contar_palavras(frase))  # 20