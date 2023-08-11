import unittest
import pandas as pd


class TestCriarSeriePrivado(unittest.TestCase):
    def test_criar_serie(self):
        valores = [1.5, 2.3, 0.8]
        indices = ['Item 1', 'Item 2', 'Item 3']

        resultado = criar_serie(valores, indices)

        self.assertIsInstance(resultado, pd.Series)  # Verifica o tipo de retorno
        self.assertListEqual(list(resultado.values), valores)  # Verifica os valores da série
        self.assertListEqual(list(resultado.index), indices)  # Verifica os índices da série

