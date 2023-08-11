import unittest
import pandas as pd


class TestCriarSeriePublico(unittest.TestCase):
    def test_criar_serie(self):
        valores = [100, 200, 150, 300]
        indices = ['Produto A', 'Produto B', 'Produto C', 'Produto D']

        resultado = criar_serie(valores, indices)

        self.assertIsInstance(resultado, pd.Series)  # Verifica o tipo de retorno
        self.assertListEqual(list(resultado.values), valores)  # Verifica os valores da série
        self.assertListEqual(list(resultado.index), indices)  # Verifica os índices da série
