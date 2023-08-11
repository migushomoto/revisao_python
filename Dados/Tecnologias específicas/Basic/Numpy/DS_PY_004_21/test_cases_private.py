import numpy as np
import unittest

class TestCriaMatrizIdentidade(unittest.TestCase):
    def test_cria_matriz_identidade_privado(self):
        n = 2
        m = 3
        resultado_esperado = np.array([[3., 0.],
                                       [0., 3.]])
        resultado_obtido = cria_matriz_identidade(n, m)
        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_cria_matriz_identidade_retorno(self):
        n = 4
        m = 1
        resultado_obtido = cria_matriz_identidade(n, m)
        self.assertIsInstance(resultado_obtido, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")

    def test_cria_matriz_identidade_opt(self):
        n = 10000
        m = 6
        resultado_obtido = cria_matriz_identidade(n, m)
        self.assertIsInstance(resultado_obtido, np.ndarray)
