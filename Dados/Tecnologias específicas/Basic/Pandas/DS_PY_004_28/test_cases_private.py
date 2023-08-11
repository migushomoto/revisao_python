import unittest
import pandas as pd
import numpy as np

class PrivateTestCase(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Temperatura': [25, 220, 27, 30, 29, 33, 40, 42, 28, 35, 26],
            'Pressao': [99, 98, 101, 250, 100, 97, 102, 100, 98, 97, 99],
            'Umidade': [61, 59, 63, 60, 62, 666, 61, 63, 59, 64, 65]
        })

    def test_identifica_outliers_temperatura(self):
        expected = pd.DataFrame({
            'Temperatura': [220],
            'Pressao': [98],
            'Umidade': [59]
        })
        result = identifica_outliers(self.df, 'Temperatura').reset_index(drop=True)
        self.assertTrue(result.equals(expected))

    def test_identifica_outliers_pressao(self):
        expected = pd.DataFrame({
            'Temperatura': [30],
            'Pressao': [250],
            'Umidade': [60]
        })
        result = identifica_outliers(self.df, 'Pressao').reset_index(drop=True)
        self.assertTrue(result.equals(expected))

    def test_identifica_outliers_umidade(self):
        expected = pd.DataFrame({
            'Temperatura': [33],
            'Pressao': [97],
            'Umidade': [666]
        })
        result = identifica_outliers(self.df, 'Umidade').reset_index(drop=True)
        self.assertTrue(result.equals(expected))

    def test_identifica_outliers_tipo_retorno(self):
        result = identifica_outliers(self.df, 'Temperatura')
        self.assertIsInstance(result, pd.DataFrame)



