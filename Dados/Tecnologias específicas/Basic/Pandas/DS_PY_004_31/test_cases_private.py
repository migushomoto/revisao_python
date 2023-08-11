import unittest
import pandas as pd

class TesteSubstituiCoresPrivado(unittest.TestCase):
    def test_substitui_cores(self):
        # Dados de entrada
        df = pd.DataFrame({'X': ['banana', 'uva', 'maçã'],
                           'Y': ['amarela', 'roxa', 'vermelha']})
        
        coluna = 'Y'
        dicionario_cores = {'amarela': 'dourada', 'vermelha': 'rosa'}
        
        # Chamar a função
        novo_df = substitui_cores(df, coluna, dicionario_cores)
        
        # Verificar o resultado
        self.assertEqual(list(novo_df['X']), ['banana', 'uva', 'maçã'])  # Verifica se os valores da coluna 'X' estão corretos
        self.assertEqual(list(novo_df['Y']), ['dourada', 'roxa', 'rosa'])  # Verifica se os valores da coluna 'Y' estão corretos

    def test_tipo_retorno(self):
        # Dados de entrada
        df = pd.DataFrame({'X': ['banana', 'uva', 'maçã'],
                           'Y': ['amarela', 'roxa', 'vermelha']})
        
        coluna = 'Y'
        dicionario_cores = {'amarela': 'dourada', 'vermelha': 'rosa'}
        
        # Chamar a função
        novo_df = substitui_cores(df, coluna, dicionario_cores)

        self.assertIsInstance(novo_df, pd.DataFrame)


