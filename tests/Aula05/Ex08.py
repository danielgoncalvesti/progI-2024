import unittest

from Aula05.Ex08 import determinar_dia_da_semana

class TestDeterminarDiaDaSemana(unittest.TestCase):

    def test_dia_domingo(self):
        self.assertEqual(determinar_dia_da_semana(1), "Domingo")
    def test_dia_segunda(self):
        self.assertEqual(determinar_dia_da_semana(2), "Segunda-feira")
    def test_dia_terca(self):
        self.assertEqual(determinar_dia_da_semana(3), "Terça-feira")
    def test_dia_quarta(self):
        self.assertEqual(determinar_dia_da_semana(4), "Quarta-feira")
    def test_dia_quinta(self):
        self.assertEqual(determinar_dia_da_semana(5), "Quinta-feira")
    def test_dia_sexta(self):
        self.assertEqual(determinar_dia_da_semana(6), "Sexta-feira")
    def test_dia_sabado(self):
        self.assertEqual(determinar_dia_da_semana(7), "Sábado")
    def test_numero_invalido_menor_que_1(self):
        self.assertEqual(determinar_dia_da_semana(0), "Número inválido. Por favor, digite um número de 1 a 7.")
    def test_numero_invalido_maior_que_7(self):
        self.assertEqual(determinar_dia_da_semana(8), "Número inválido. Por favor, digite um número de 1 a 7.")
    def test_numero_invalido_negativo(self):
        self.assertEqual(determinar_dia_da_semana(-3), "Número inválido. Por favor, digite um número de 1 a 7.")

if __name__ == '__main__':
    unittest.main()
