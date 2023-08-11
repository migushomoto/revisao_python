import unittest
import pandas as pd

class TesteTransformaColunaEmDummyPublico(unittest.TestCase):
    def test_transforma_coluna_em_dummy(self):
        # Dados de entrada
        df = pd.DataFrame({'A': ['maçã', 'banana', 'uva'],
                           'B': [1, 2, 3]})
        
        coluna = 'A'
        
        # Chamar a função
        novo_df = transforma_coluna_em_dummy(df, coluna)

        res = list(novo_df.columns)
        res.sort()
        esp = ['B', 'maçã', 'banana', 'uva']
        esp.sort()
        
        # Verificar o resultado
        self.assertEqual(res, esp)  # Verifica se as colunas estão corretas
        self.assertEqual(list(novo_df['B']), [1, 2, 3])  # Verifica se a coluna 'B' está correta
        self.assertEqual(list(novo_df['maçã']), [1, 0, 0])  # Verifica se a coluna 'maçã' está correta
        self.assertEqual(list(novo_df['banana']), [0, 1, 0])  # Verifica se a coluna 'banana' está correta
        self.assertEqual(list(novo_df['uva']), [0, 0, 1])  # Verifica se a coluna 'uva' está correta

    def test_tipo_retorno(self):
        # Dados de entrada
        df = pd.DataFrame({'A': ['maçã', 'banana', 'uva'],
                           'B': [1, 2, 3]})
        
        coluna = 'A'
        
        # Chamar a função
        novo_df = transforma_coluna_em_dummy(df, coluna)

        self.assertIsInstance(novo_df, pd.DataFrame)
