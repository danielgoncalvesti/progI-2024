# Função de Extração de Domínio de Email
# Descrição: Crie uma função chamada extrair_dominio que recebe um endereço de email como parâmetro
# e retorna o domínio do email.

def extrair_dominio(email):
    dominio = email.split("@")
    return dominio[1]

lista_emails = ["usuario@fatec.sp.gov.br", "usuario@dominio.com", "nome.sobrenome@empresa.org"]

for emails in lista_emails:
    print(extrair_dominio(emails))

# resultado esperado:
# fatec.sp.gov.br
# dominio.com
# empresa.org