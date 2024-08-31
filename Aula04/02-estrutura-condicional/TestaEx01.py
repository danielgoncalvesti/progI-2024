import unittest
from Ex01 import eh_par

class TestEhPar(unittest.TestCase):
    def test_numero_par(self):
        self.assertTrue(eh_par(4), "Erro: 4 deveria ser considerado um número par.")
        self.assertTrue(eh_par(0), "Erro: 0 deveria ser considerado um número par.")
        self.assertTrue(eh_par(100), "Erro: 100 deveria ser considerado um número par.")

    def test_numero_impar(self):
        self.assertFalse(eh_par(5), "Erro: 5 deveria ser considerado um número ímpar.")
        self.assertFalse(eh_par(7), "Erro: 7 deveria ser considerado um número ímpar.")
        self.assertFalse(eh_par(99), "Erro: 99 deveria ser considerado um número ímpar.")

# Executar os testes
unittest.TextTestRunner().run(unittest.makeSuite(TestEhPar))
