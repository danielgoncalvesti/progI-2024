# Função que retorna uma lista de palavras
# Descrição: Crie uma função chamada string_para_lista_palavras que recebe uma string como parâmetro e
# retorna uma lista de palavras.

def string_para_lista_palavras(frase):
    frase_formatada = frase.replace(",", "").replace(".", "")
    frase_separada =  frase_formatada.split(" ")
    return frase_separada

frase = "O sucesso não é determinado por quantas vezes você ganha, mas por como você joga na semana após a derrota."
print(string_para_lista_palavras(frase))
# resultado esperado:
# ['O', 'sucesso', 'não', 'é', 'determinado', 'por', 'quantas', 'vezes', 'você', 'ganha', 'mas', 'por', 'como', 'você', 'joga', 'na', 'semana', 'após', 'a', 'derrota']