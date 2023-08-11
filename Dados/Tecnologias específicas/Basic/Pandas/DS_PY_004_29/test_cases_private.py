import unittest
import pandas as pd

class TesteDeletaRegistrosPrivado(unittest.TestCase):
    def test_deleta_registros(self):
        # Dados de entrada
        df = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carlos', 'Daniel'],
                           'Idade': [30, 35, 45, 27],
                           'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']})

        indices = [0, 2]

        # Chamar a função
        novo_df = deleta_registros(df, indices)

        # Verificar o resultado
        self.assertEqual(novo_df.shape[0], 2)  # Verifica se o número de linhas é igual a 2
        self.assertEqual(list(novo_df['Nome']), ['Bob', 'Daniel'])  # Verifica se os nomes estão corretos
        self.assertEqual(list(novo_df['Idade']), [35, 27])  # Verifica se as idades estão corretas
        self.assertEqual(list(novo_df['Cidade']), ['Rio de Janeiro', 'Porto Alegre'])  # Verifica se as cidades estão corretas


    def test_tipo_retorno(self):
        df = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carlos', 'Daniel'],
                    'Idade': [30, 35, 45, 27],
                    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']})

        indices = [0, 2]

        novo_df = deleta_registros(df, indices)

        self.assertIsInstance(novo_df, pd.DataFrame)


