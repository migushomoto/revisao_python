import unittest
import pandas as pd


def calcula_imc(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula o IMC para cada paciente no DataFrame e adiciona uma nova coluna com o resultado.

    Args:
        df (pd.DataFrame): DataFrame contendo as informações dos pacientes.

    Returns:
        pd.DataFrame: DataFrame modificado com a nova coluna do IMC.
    """
    df['IMC'] = df['Peso'] / (df['Altura'] ** 2)
    return df

# Classe para os testes públicos
class PublicTestCase(unittest.TestCase):
    
    def test_calcula_imc(self):
        dados = {
            "Nome": ["João", "Maria", "José", "Ana", "Carlos"],
            "Idade": [30, 25, 40, 35, 28],
            "Sexo": ["M", "F", "M", "F", "M"],
            "Altura": [1.75, 1.68, 1.80, 1.65, 1.72],
            "Peso": [70, 55, 85, 75, 80]
        }
        df = pd.DataFrame(dados)
        df_resultado = calcula_imc(df)
        
        # Verifica se a coluna IMC foi adicionada corretamente
        self.assertTrue("IMC" in df_resultado.columns)
        
        # Verifica se o IMC foi calculado corretamente
        self.assertEqual(df_resultado.loc[0, "IMC"], 22.857142857142858)
        self.assertEqual(df_resultado.loc[1, "IMC"], 19.48696145124717)
        self.assertEqual(df_resultado.loc[2, "IMC"], 26.234567901234566)
        self.assertEqual(df_resultado.loc[3, "IMC"], 27.548209366391188)
        self.assertEqual(df_resultado.loc[4, "IMC"], 27.041644131963228)


# Execução dos testes
if __name__ == '__main__':
    unittest.main()
