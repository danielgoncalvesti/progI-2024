import unittest
from Aula05.condicional.Ex09 import verificar_elegibilidade_voto

class TestVerificarElegibilidadeVoto(unittest.TestCase):
    def test_elegivel_para_votar(self):
        # Testa quando a idade é maior ou igual a 18 e é cidadão brasileiro
        self.assertEqual(verificar_elegibilidade_voto(22, "S"), "Elegível para votar.")
        self.assertEqual(verificar_elegibilidade_voto(18, "S"), "Elegível para votar.")

    def test_nao_elegivel_por_idade(self):
        # Testa quando a idade é menor que 18
        self.assertEqual(verificar_elegibilidade_voto(15, "S"), "Não elegível para votar.")
        self.assertEqual(verificar_elegibilidade_voto(17, "S"), "Não elegível para votar.")

    def test_nao_elegivel_por_nao_ser_brasileiro(self):
        # Testa quando não é cidadão brasileiro
        self.assertEqual(verificar_elegibilidade_voto(22, "N"), "Não elegível para votar.")
        self.assertEqual(verificar_elegibilidade_voto(30, "n"), "Não elegível para votar.")

    def test_nao_elegivel_por_idade_e_nao_ser_brasileiro(self):
        # Testa quando a idade é menor que 18 e não é cidadão brasileiro
        self.assertEqual(verificar_elegibilidade_voto(15, "N"), "Não elegível para votar.")
        self.assertEqual(verificar_elegibilidade_voto(17, "n"), "Não elegível para votar.")

if __name__ == "__main__":
    unittest.main()
