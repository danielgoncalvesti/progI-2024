import unittest

from Ex06 import calcular_desconto
class TestCalcularDesconto(unittest.TestCase):

    def test_valor_com_desconto(self):
        # Teste com valor igual ou maior que R$ 150,00
        valor_total = 200.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 180.00)  # 10% de desconto
        self.assertEqual(desconto, 20.00)

    def test_valor_exatamente_limite(self):
        # Teste com valor exatamente R$ 150,00
        valor_total = 150.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 135.00)  # 10% de desconto
        self.assertEqual(desconto, 15.00)

    def test_valor_sem_desconto(self):
        # Teste com valor menor que R$ 150,00 (sem desconto, mas verificando retorno correto)
        valor_total = 100.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 90.00)  # 10% de desconto
        self.assertEqual(desconto, 10.00)

    def test_valor_zero(self):
        # Teste com valor zero
        valor_total = 0.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 0.00)
        self.assertEqual(desconto, 0.00)

unittest.TextTestRunner().run(unittest.makeSuite(TestCalcularDesconto))
