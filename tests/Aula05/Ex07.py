import unittest
from Aula05.Ex07 import calcular_desconto  # Substitua 'seu_modulo' pelo nome do módulo onde a função está definida

class TestCalcularDiferenteDescontos(unittest.TestCase):

    def test_desconto_ate_100(self):
        valor_total = 100.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 95.00)  # 5% de desconto
        self.assertEqual(desconto, 5.00)

    def test_desconto_acima_100_ate_500(self):
        valor_total = 200.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 180.00)  # 10% de desconto
        self.assertEqual(desconto, 20.00)

    def test_desconto_acima_500(self):
        valor_total = 600.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 510.00)  # 15% de desconto
        self.assertEqual(desconto, 90.00)

    def test_valor_zero(self):
        valor_total = 0.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 0.00)
        self.assertEqual(desconto, 0.00)

if __name__ == '__main__':
    unittest.main()
