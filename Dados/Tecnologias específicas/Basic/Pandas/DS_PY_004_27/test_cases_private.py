import unittest
import pandas as pd
import numpy as np

class TestTrataDadosFaltantes(unittest.TestCase):

    def test_trata_dados_faltantes(self):

        # Caso de teste privado com dados diferentes
        df2 = pd.DataFrame({'X': [3, 4, np.nan], 'Y': [10, np.nan, 15], 'Z': [np.nan, 12.5, np.nan]})
        expected2 = pd.DataFrame({'X': [3.0, 4.0, 3.5], 'Y': [10.0, 12.5, 15.0], 'Z': [12.5, 12.5, 12.5]})
        self.assertTrue(trata_dados_faltantes(df2).equals(expected2))

    def test_trata_dados_faltantes_2(self):
        # Caso de teste com todas as colunas preenchidas (não deve haver modificação)
        df3 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 99]})
        expected3 = df3.copy()
        self.assertTrue(trata_dados_faltantes(df3).equals(expected3))

    def test_tipo_retorno(self):
        df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9]})
        result = trata_dados_faltantes(df)
        self.assertIsInstance(result, pd.DataFrame)
