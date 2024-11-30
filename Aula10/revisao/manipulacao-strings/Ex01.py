"""
Exercício Detecção de Palavras Proibidas
Receba uma string e uma lista de palavras proibidas.
Substitua as palavras proibidas por ***.

Exemplo:
palavras_proibidas: ["confidencial"]
Entrada: "Este é um texto confidencial"

Saída: Este é um texto ***
"""
entrada = (
    "Este documento é confidencial e contém informações privadas que são restritas "
    "a usuários autorizados. O acesso ao sistema exige credenciais válidas, incluindo "
    "senha e token de autenticação. A transmissão segura desses dados é essencial para evitar "
    "vazamentos ou violações de segurança. Mantenha o backup atualizado e classificado."
)
palavras_proibidas = ["confidencial", "sigiloso", "privado", "restrito", "secreto", "proibido",
                      "reservado", "classificado", "sensível", "exclusivo", "não autorizado", "vazamento",
                      "violação", "senha", "acesso", "crédito", "cartão", "dados pessoais", "informação",
                      "crítica", "alta prioridade", "segurança", "identidade", "rastreável", "interno",
                      "confirmação", "código", "protocolo", "credencial", "token", "autenticação", "padrão",
                      "admin", "informações privadas", "alerta", "backup", "cópia segura", "transmissão segura"]

