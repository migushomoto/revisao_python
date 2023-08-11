import pandas as pd
import unittest

class TestBuscaPorFaixaEtaria(unittest.TestCase):
    def setUp(self):
        dados = {
            'Nome': ['Ana', 'João', 'Pedro', 'Maria', 'Lucas'],
            'Idade': [23, 27, 31, 19, 22],
            'Sexo': ['F', 'M', 'M', 'F', 'M'],
            'Altura': [1.65, 1.78, 1.85, 1.60, 1.75],
            'Peso': [65, 80, 90, 55, 70]
        }
        self.df = pd.DataFrame(dados)

    def test_busca_por_faixa_etaria(self):
        resultado = busca_por_faixa_etaria(self.df, 20, 30)
        esperado = pd.DataFrame({
            'Nome': ['Ana', 'João', 'Lucas'],
            'Idade': [23, 27, 22],
            'Sexo': ['F', 'M', 'M'],
            'Altura': [1.65, 1.78, 1.75],
            'Peso': [65, 80, 70]
        })
        pd.testing.assert_frame_equal(resultado.reset_index(drop=True), esperado.reset_index(drop=True))

    def test_busca_por_faixa_etaria_todos(self):
        resultado = busca_por_faixa_etaria(self.df, 0, 100)
        pd.testing.assert_frame_equal(resultado.reset_index(drop=True), self.df.reset_index(drop=True))

    def test_tipo_retorno(self):
        resultado = busca_por_faixa_etaria(self.df, 20, 30)
        self.assertIsInstance(resultado, pd.DataFrame)