import numpy as np
import unittest

class TestCalculaImagemIntegralPublico(unittest.TestCase):
    def test_calcula_imagem_integral_1(self):
        imagem = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        resultado_esperado = np.array([[1, 3, 6],
                                       [5, 12, 21],
                                       [12, 27, 45]])
        resultado_obtido = calcula_imagem_integral(imagem)
        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_calcula_imagem_integral_2(self):
        imagem = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
        resultado_esperado = np.array([[2, 4, 6],
                                       [4, 8, 12],
                                       [6, 12, 18]])
        resultado_obtido = calcula_imagem_integral(imagem)
        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_calcula_imagem_integral_retorno(self):
        imagem = np.array([[0, 0], [0, 0]])
        resultado_obtido = calcula_imagem_integral(imagem)
        self.assertIsInstance(resultado_obtido, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")

