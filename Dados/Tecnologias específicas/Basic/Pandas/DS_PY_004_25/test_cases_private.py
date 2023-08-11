import pandas as pd
import unittest

class TestBuscaPorFaixaEtariaMaisDados(unittest.TestCase):
    def setUp(self):
        dados = {
            'Nome': ['Carlos', 'Mariana', 'Pedro', 'Camila', 'Lucas', 'Ana', 'João', 'Paula', 'Rafael'],
            'Idade': [34, 28, 31, 19, 22, 45, 27, 38, 33],
            'Sexo': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'],
            'Altura': [1.70, 1.65, 1.80, 1.60, 1.75, 1.68, 1.73, 1.69, 1.77],
            'Peso': [75, 60, 90, 55, 70, 68, 80, 62, 85]
        }
        self.df = pd.DataFrame(dados)

    def test_busca_por_faixa_etaria(self):
        # Faixa etária de 25 a 35 anos
        resultado = busca_por_faixa_etaria(self.df, 25, 35)
        esperado = pd.DataFrame({
            'Nome': ['Carlos', 'Mariana', 'Pedro', 'João', 'Rafael'],
            'Idade': [34, 28, 31, 27, 33],
            'Sexo': ['M', 'F', 'M', 'M', 'M'],
            'Altura': [1.70, 1.65, 1.80, 1.73, 1.77],
            'Peso': [75, 60, 90, 80, 85]
        })
        pd.testing.assert_frame_equal(resultado.reset_index(drop=True), esperado.reset_index(drop=True))


    def test_busca_por_faixa_etaria_todos(self):
        resultado = busca_por_faixa_etaria(self.df, 0, 100)
        pd.testing.assert_frame_equal(resultado.reset_index(drop=True), self.df.reset_index(drop=True))

    def test_tipo_retorno(self):
        resultado = busca_por_faixa_etaria(self.df, 20, 30)
        self.assertIsInstance(resultado, pd.DataFrame)