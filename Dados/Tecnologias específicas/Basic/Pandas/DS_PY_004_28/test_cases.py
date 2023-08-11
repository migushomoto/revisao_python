import unittest
import pandas as pd
import numpy as np

class PublicTestCase(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Temperatura': [30, 32, 35, 28, 27, 31, 400, 29, 33, 34, 36],
            'Pressao': [100, 101, 102, 99, 98, 97, 1003, 100, 101, 99, 102],
            'Umidade': [600, 58, 62, 61, 63, 65, 59, 60, 64, 63, 61]
        })

    def test_identifica_outliers_temperatura(self):
        expected = pd.DataFrame({
            'Temperatura': [400],
            'Pressao': [1003],
            'Umidade': [59]
        })
        result = identifica_outliers(self.df, 'Temperatura').reset_index(drop=True)
        self.assertTrue(result.equals(expected))

    def test_identifica_outliers_pressao(self):
        expected = pd.DataFrame({
            'Temperatura': [400],
            'Pressao': [1003],
            'Umidade': [59]
        })
        result = identifica_outliers(self.df, 'Pressao').reset_index(drop=True)
        self.assertTrue(result.equals(expected))

    def test_identifica_outliers_umidade(self):
        expected = pd.DataFrame({
            'Temperatura': [30],
            'Pressao': [100],
            'Umidade': [600]
        })
        result = identifica_outliers(self.df, 'Umidade').reset_index(drop=True)
        self.assertTrue(result.equals(expected))

    def test_identifica_outliers_tipo_retorno(self):
        result = identifica_outliers(self.df, 'Temperatura')
        self.assertIsInstance(result, pd.DataFrame)
