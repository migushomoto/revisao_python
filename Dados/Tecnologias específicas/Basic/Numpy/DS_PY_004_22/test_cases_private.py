import numpy as np
import unittest

class TestCalculaImagemIntegralPrivado(unittest.TestCase):
    def test_calcula_imagem_integral_2(self):
        imagem = np.array([[1, 2], [3, 4]])
        resultado_esperado = np.array([[1, 3],
                                       [4, 10]])
        resultado_obtido = calcula_imagem_integral(imagem)
        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_calcula_imagem_integral_3(self):
        imagem = np.array([[1, 1, 1], [1, 1, 1]])
        resultado_esperado = np.array([[1, 2, 3],
                                       [2, 4, 6]])
        resultado_obtido = calcula_imagem_integral(imagem)
        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_calcula_imagem_integral_retorno(self):
        imagem = np.array([[1, 2], [3, 4]])
        resultado_obtido = calcula_imagem_integral(imagem)
        self.assertIsInstance(resultado_obtido, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")
