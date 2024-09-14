import unittest
from Aula05.condicional.Ex06 import calcular_desconto

class TestCalcularDesconto(unittest.TestCase):
    def test_valor_com_desconto(self):
        # Teste com valor igual ou maior que R$ 150,00
        valor_total = 200.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 180.00)
        self.assertEqual(desconto, 20.00)

    def test_valor_exatamente_limite(self):
        # Teste com valor exatamente R$ 150,00
        valor_total = 150.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 135.00)
        self.assertEqual(desconto, 15.00)

    def test_valor_zero(self):
        # Teste com valor zero
        valor_total = 0.00
        valor_com_desconto, desconto = calcular_desconto(valor_total)
        self.assertEqual(valor_com_desconto, 0.00)
        self.assertEqual(desconto, 0.00)

if __name__ == '__main__':
    unittest.main()
