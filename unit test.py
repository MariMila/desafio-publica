import unittest
import FuncoesDesafio as fdd


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
        self.assertEqual(fdd.quebras_positivas([12, 24, 10, 24, 100, 50]),
                         ([0, 1, 1, 1, 2, 2], [12, 24, 24, 24, 100, 100]))
        self.assertEqual(fdd.quebras_negativas([12, 24, 10, 24, 100, 50]),
                         ([0, 0, 1, 1, 1, 1], [12, 12, 10, 10, 10, 10]))
        self.assertEqual(fdd.numero_impressao(24), ' 24 ')
        self.assertEqual(fdd.para_salvar([1, 2, 3]), "pontuacoes = [1, 2, 3]")


if __name__ == '__main__':
    unittest.main()


