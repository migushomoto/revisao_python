import unittest
import pandas as pd

class TesteSubstituiValoresPrivado(unittest.TestCase):
    def test_substitui_valores(self):
        # Dados de entrada
        df = pd.DataFrame({'X': [10, 20, 30, 40, 50],
                           'Y': [60, 70, 80, 90, 100]})

        coluna = 'Y'
        limite = 70
        valor_padrao = 15

        # Chamar a função
        novo_df = substitui_valores(df, coluna, limite, valor_padrao)

        # Verificar o resultado
        self.assertEqual(list(novo_df['X']), [10, 20, 30, 40, 50])  # Verifica se os valores da coluna 'X' estão corretos
        self.assertEqual(list(novo_df['Y']), [60, 15, 15, 15, 15])  # Verifica se os valores da coluna 'Y' estão corretos

    def test_tipo_retorno(self):
        df = pd.DataFrame({'X': [10, 20, 30, 40, 50],
                           'Y': [60, 70, 80, 90, 100]})

        coluna = 'Y'
        limite = 70
        valor_padrao = 15

        # Chamar a função
        novo_df = substitui_valores(df, coluna, limite, valor_padrao)

        self.assertIsInstance(novo_df, pd.DataFrame)

