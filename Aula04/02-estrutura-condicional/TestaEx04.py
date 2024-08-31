import unittest
from Ex04 import eh_positivo, eh_negativo, eh_zero  # Importando as funções específicas do arquivo Ex04

# Testes unitários
class TestVerificarNumero(unittest.TestCase):
    def test_eh_positivo(self):
        self.assertTrue(eh_positivo(5), "Erro: 5 deveria ser considerado positivo.")
        self.assertTrue(eh_positivo(100), "Erro: 100 deveria ser considerado positivo.")
        self.assertFalse(eh_positivo(-1), "Erro: -1 não deveria ser considerado positivo.")
        self.assertFalse(eh_positivo(0), "Erro: 0 não deveria ser considerado positivo.")

    def test_eh_negativo(self):
        self.assertTrue(eh_negativo(-3), "Erro: -3 deveria ser considerado negativo.")
        self.assertTrue(eh_negativo(-50), "Erro: -50 deveria ser considerado negativo.")
        self.assertFalse(eh_negativo(5), "Erro: 5 não deveria ser considerado negativo.")
        self.assertFalse(eh_negativo(0), "Erro: 0 não deveria ser considerado negativo.")

    def test_eh_zero(self):
        self.assertTrue(eh_zero(0), "Erro: 0 deveria ser considerado zero.")
        self.assertFalse(eh_zero(5), "Erro: 5 não deveria ser considerado zero.")
        self.assertFalse(eh_zero(-1), "Erro: -1 não deveria ser considerado zero.")

unittest.TextTestRunner().run(unittest.makeSuite(TestVerificarNumero))
