import numpy as np
import unittest

class TestSomaColunas(unittest.TestCase):
    def test_soma_colunas_publico(self):
        matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        resultado_esperado = np.array([12, 15, 18])
        resultado_obtido = soma_colunas(matriz)
        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_soma_colunas_2_publico(self):
        matriz = np.array([[1, 3], [4, 6], [7, 9]])
        resultado_esperado = np.array([12, 18])
        resultado_obtido = soma_colunas(matriz)
        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_soma_colunas_retorno(self):
        matriz = np.array([[1, 2], [3, 4]])
        resultado_obtido = soma_colunas(matriz)
        self.assertIsInstance(resultado_obtido, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")
