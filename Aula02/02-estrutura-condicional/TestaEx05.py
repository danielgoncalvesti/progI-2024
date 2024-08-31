import unittest

from Ex05 import verificar_status_aluno
class TestVerificarStatusAluno(unittest.TestCase):
    def test_reprovado(self):
        self.assertIn("reprovado", verificar_status_aluno(5), "Erro: O aluno deveria estar reprovado.")
        self.assertIn("reprovado", verificar_status_aluno(0), "Erro: O aluno deveria estar reprovado.")
        self.assertIn("reprovado", verificar_status_aluno(5.9), "Erro: O aluno deveria estar reprovado.")

    def test_recuperacao(self):
        self.assertIn("recuperação", verificar_status_aluno(6), "Erro: O aluno deveria estar de recuperação.")
        self.assertIn("recuperação", verificar_status_aluno(6.5), "Erro: O aluno deveria estar de recuperação.")
        self.assertIn("recuperação", verificar_status_aluno(7), "Erro: O aluno deveria estar de recuperação.")

    def test_aprovado(self):
        self.assertIn("aprovado", verificar_status_aluno(7.1), "Erro: O aluno deveria estar aprovado.")
        self.assertIn("aprovado", verificar_status_aluno(8), "Erro: O aluno deveria estar aprovado.")
        self.assertIn("aprovado", verificar_status_aluno(10), "Erro: O aluno deveria estar aprovado.")

unittest.TextTestRunner().run(unittest.makeSuite(TestVerificarStatusAluno))