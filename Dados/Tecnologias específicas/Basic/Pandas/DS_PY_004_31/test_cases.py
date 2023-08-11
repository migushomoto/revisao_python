import unittest
import pandas as pd

class TesteSubstituiCoresPublico(unittest.TestCase):
    def test_substitui_cores(self):
        # Dados de entrada
        df = pd.DataFrame({'A': ['maçã', 'banana', 'uva'],
                           'B': ['vermelha', 'amarela', 'roxa']})
        
        coluna = 'B'
        dicionario_cores = {'vermelha': 'rosa', 'amarela': 'dourada'}
        
        # Chamar a função
        novo_df = substitui_cores(df, coluna, dicionario_cores)
        
        # Verificar o resultado
        self.assertEqual(list(novo_df['A']), ['maçã', 'banana', 'uva'])  # Verifica se os valores da coluna 'A' estão corretos
        self.assertEqual(list(novo_df['B']), ['rosa', 'dourada', 'roxa'])  # Verifica se os valores da coluna 'B' estão corretos

    def test_tipo_retorno(self):
        # Dados de entrada
        df = pd.DataFrame({'A': ['maçã', 'banana', 'uva'],
                           'B': ['vermelha', 'amarela', 'roxa']})
        
        coluna = 'B'
        dicionario_cores = {'vermelha': 'rosa', 'amarela': 'dourada'}
        
        # Chamar a função
        novo_df = substitui_cores(df, coluna, dicionario_cores)
        

        self.assertIsInstance(novo_df, pd.DataFrame)

