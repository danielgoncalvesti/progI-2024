import unittest
from Ex03 import encontrar_maior, encontrar_menor

# Testes unitários
class TestComparacaoTresNumeros(unittest.TestCase):
    def test_encontrar_maior(self):
        self.assertEqual(encontrar_maior(10, 5, 8), 10, "Erro: O maior número deveria ser 10.")
        self.assertEqual(encontrar_maior(1, 3, 2), 3, "Erro: O maior número deveria ser 3.")
        self.assertEqual(encontrar_maior(7, 7, 7), 7, "Erro: O maior número deveria ser 7.")
        self.assertEqual(encontrar_maior(-5, -1, -3), -1, "Erro: O maior número deveria ser -1.")

    def test_encontrar_menor(self):
        self.assertEqual(encontrar_menor(10, 5, 8), 5, "Erro: O menor número deveria ser 5.")
        self.assertEqual(encontrar_menor(1, 3, 2), 1, "Erro: O menor número deveria ser 1.")
        self.assertEqual(encontrar_menor(7, 7, 7), 7, "Erro: O menor número deveria ser 7.")
        self.assertEqual(encontrar_menor(-5, -1, -3), -5, "Erro: O menor número deveria ser -5.")

unittest.TextTestRunner().run(unittest.makeSuite(TestComparacaoTresNumeros))
