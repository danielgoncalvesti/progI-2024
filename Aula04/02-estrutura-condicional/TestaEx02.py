import unittest

from Ex02 import eh_maior, eh_menor, eh_igual

class TestComparacoes(unittest.TestCase):
    def test_eh_maior(self):
        self.assertTrue(eh_maior(10, 5), "Erro: 10 deveria ser considerado maior que 5.")
        self.assertFalse(eh_maior(5, 10), "Erro: 5 não deveria ser considerado maior que 10.")
        self.assertFalse(eh_maior(5, 5), "Erro: 5 não deveria ser considerado maior que 5.")

    def test_eh_menor(self):
        self.assertTrue(eh_menor(5, 10), "Erro: 5 deveria ser considerado menor que 10.")
        self.assertFalse(eh_menor(10, 5), "Erro: 10 não deveria ser considerado menor que 5.")
        self.assertFalse(eh_menor(5, 5), "Erro: 5 não deveria ser considerado menor que 5.")

    def test_eh_igual(self):
        self.assertTrue(eh_igual(5, 5), "Erro: 5 deveria ser considerado igual a 5.")
        self.assertFalse(eh_igual(5, 10), "Erro: 5 não deveria ser considerado igual a 10.")
        self.assertFalse(eh_igual(10, 5), "Erro: 10 não deveria ser considerado igual a 5.")

# Executar os testes
unittest.TextTestRunner().run(unittest.makeSuite(TestComparacoes))
