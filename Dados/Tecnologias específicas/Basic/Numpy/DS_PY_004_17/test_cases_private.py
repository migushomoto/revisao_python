import unittest
import numpy as np

class TestMediaAvaliacao(unittest.TestCase):
    
    def test_media_avaliacao_valores_inteiros(self):
        avaliacoes = np.array([7, 8, 9, 10, 6])
        resultado_esperado = 8.0
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertEqual(resultado_esperado, resultado_obtido)
    
    def test_media_avaliacao_valores_decimais(self):
        avaliacoes = np.array([6.5, 7.8, 8.9, 9.3, 6.1])
        resultado_esperado = 7.72
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertAlmostEqual(resultado_esperado, resultado_obtido, places=2)
    
    def test_media_avaliacao_array_com_um_elemento(self):
        avaliacoes = np.array([8.7])
        resultado_esperado = 8.7
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertEqual(resultado_esperado, resultado_obtido)
    
    def test_media_avaliacao_array_negativo(self):
        avaliacoes = np.array([-6, -7, -8, -9, -10])
        resultado_esperado = -8.0
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertEqual(resultado_esperado, resultado_obtido)

    def test_media_avaliacao_retorno_float(self):
        avaliacoes = np.array([8.5, 7.9, 9.0, 8.8, 8.2])
        resultado_obtido = media_avaliacao(avaliacoes)
        self.assertIsInstance(resultado_obtido, float)
