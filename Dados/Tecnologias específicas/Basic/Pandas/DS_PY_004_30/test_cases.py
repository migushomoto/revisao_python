import unittest
import pandas as pd

class TesteSubstituiValoresPublico(unittest.TestCase):
    def test_substitui_valores(self):
        # Dados de entrada
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                           'B': [6, 7, 8, 9, 10]})

        coluna = 'B'
        limite = 8
        valor_padrao = 20

        # Chamar a função
        novo_df = substitui_valores(df, coluna, limite, valor_padrao)

        # Verificar o resultado
        self.assertEqual(list(novo_df['A']), [1, 2, 3, 4, 5])  # Verifica se os valores da coluna 'A' estão corretos
        self.assertEqual(list(novo_df['B']), [6, 7, 20, 20, 20])  # Verifica se os valores da coluna 'B' estão corretos

    def test_tipo_retorno(self):
        # Dados de entrada
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                           'B': [6, 7, 8, 9, 10]})

        coluna = 'B'
        limite = 8
        valor_padrao = 20

        # Chamar a função
        novo_df = substitui_valores(df, coluna, limite, valor_padrao)

        self.assertIsInstance(novo_df, pd.DataFrame)