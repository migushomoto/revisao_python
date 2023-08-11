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


# Classe para os testes privados
class PrivateTestCase(unittest.TestCase):
    
    def test_calcula_imc(self):
        dados = {
            "Nome": ["Paula", "Rafael", "Larissa", "Pedro", "Fernanda"],
            "Idade": [22, 35, 42, 28, 31],
            "Sexo": ["F", "M", "F", "M", "F"],
            "Altura": [1.60, 1.85, 1.75, 1.68, 1.72],
            "Peso": [50, 75, 68, 62, 70]
        }
        df = pd.DataFrame(dados)
        df_resultado = calcula_imc(df)
        
        # Verifica se a coluna IMC foi adicionada corretamente
        self.assertTrue("IMC" in df_resultado.columns)
        
        # Verifica se o IMC foi calculado corretamente
        self.assertEqual(df_resultado.loc[0, "IMC"], 19.531249999999996)
        self.assertEqual(df_resultado.loc[1, "IMC"], 21.913805697589478)
        self.assertEqual(df_resultado.loc[2, "IMC"], 22.20408163265306)
        self.assertEqual(df_resultado.loc[3, "IMC"], 21.9671201814059)
        self.assertEqual(df_resultado.loc[4, "IMC"], 23.661438615467823)


# Execução dos testes
if __name__ == '__main__':
    unittest.main()
