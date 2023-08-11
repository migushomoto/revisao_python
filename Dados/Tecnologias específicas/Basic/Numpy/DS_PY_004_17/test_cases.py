import unittest
import numpy as np

class TestMediaAvaliacao(unittest.TestCase):
    
    def test_media_avaliacao_valores_inteiros(self):
        avaliacoes = np.array([6, 4, 1, 8, 6])
        resultado_esperado = 5.0
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertEqual(resultado_esperado, resultado_obtido)
    
    def test_media_avaliacao_valores_decimais(self):
        avaliacoes = np.array([3.14, 2.71, 1.62, 0.99])
        resultado_esperado = 2.114999999
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertAlmostEqual(resultado_esperado, resultado_obtido, places=2)
    
    def test_media_avaliacao_array_com_um_elemento(self):
        avaliacoes = np.array([10.6])
        resultado_esperado = 10.6
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertEqual(resultado_esperado, resultado_obtido)
    
    def test_media_avaliacao_array_negativo(self):
        avaliacoes = np.array([-600, -75, -8.5, -9.8, -11])
        resultado_esperado = -140.85999999999999
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertEqual(resultado_esperado, resultado_obtido)

    def test_media_avaliacao_retorno_float(self):
        avaliacoes = np.array([0.5, 1.5, 2.5])
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertIsInstance(resultado_obtido, float)
