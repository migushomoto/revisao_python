import unittest
import pandas as pd
import numpy as np

class TestTrataDadosFaltantes(unittest.TestCase):

    def test_trata_dados_faltantes(self):
        # Caso de teste público
        df1 = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9]})
        expected1 = pd.DataFrame({'A': [1.0, 2.0, 1.5], 'B': [4.0, 4.0, 4.0], 'C': [7, 8, 9]})
        self.assertTrue(trata_dados_faltantes(df1).equals(expected1))

    def test_trata_dados_faltantes_2(self):
        # Caso de teste com todas as colunas preenchidas (não deve haver modificação)
        df3 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        expected3 = df3.copy()
        self.assertTrue(trata_dados_faltantes(df3).equals(expected3))

    def test_tipo_retorno(self):
        df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9]})
        result = trata_dados_faltantes(df)
        self.assertIsInstance(result, pd.DataFrame)
