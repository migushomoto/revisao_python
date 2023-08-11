import numpy as np
import unittest

class TestSomaColunas(unittest.TestCase):
    def test_soma_colunas_privado(self):
        matriz = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
        resultado_esperado = np.array([150, 180, 210, 240])
        resultado_obtido = soma_colunas(matriz)
        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_soma_colunas_retorno(self):
        matriz = np.array([[10, 22], [13, 22]])
        resultado_obtido = soma_colunas(matriz)
        self.assertIsInstance(resultado_obtido, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")
