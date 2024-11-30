"""
Crie um programa que gere senhas aleatórias seguras para proteger
contas e sistemas. O programa deve gerar 5 senhas contendo
exatamente 8 caracteres cada.

Para garantir a segurança, cada senha deve incluir:
No mínimo:
- Uma letra maiúsculas (A-Z),
- Uma letra minúsculas (a-z),
- Um Números (0-9),
- Um Caracteres especiais (como @, #, &, etc.).
Utilize um laço para gerar as senhas e exibi-las na saída formatada.
"""

alfabeto_minusculas = list(string.ascii_lowercase)

alfabeto_maiusculas = list(string.ascii_uppercase)

numeros = list(range(10)) # lista dos números de 0 a 9

caracteres_especiais = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~") # Lista de caracteres especiais


