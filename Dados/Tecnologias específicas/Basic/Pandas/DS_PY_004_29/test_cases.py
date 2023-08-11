import unittest
import pandas as pd

class TesteDeletaRegistrosPublico(unittest.TestCase):
    def test_deleta_registros(self):
        # Dados de entrada
        df = pd.DataFrame({'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
                           'Idade': [25, 30, 40, 20],
                           'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']})

        indices = [1, 3]

        # Chamar a função
        novo_df = deleta_registros(df, indices)

        # Verificar o resultado
        self.assertEqual(novo_df.shape[0], 2)  # Verifica se o número de linhas é igual a 2
        self.assertEqual(list(novo_df['Nome']), ['João', 'Pedro'])  # Verifica se os nomes estão corretos
        self.assertEqual(list(novo_df['Idade']), [25, 40])  # Verifica se as idades estão corretas
        self.assertEqual(list(novo_df['Cidade']), ['São Paulo', 'Belo Horizonte'])  # Verifica se as cidades estão corretas

    def test_tipo_retorno(self):
        df = pd.DataFrame({'Nome': ['Alice', 'Daniel'],
                    'Idade': [45, 27],
                    'Cidade': ['Belo Horizonte', 'Porto Alegre']})

        indices = [0]

        novo_df = deleta_registros(df, indices)

        self.assertIsInstance(novo_df, pd.DataFrame)

