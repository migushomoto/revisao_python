import unittest
import numpy as np

class TestConcatenacaoArrays(unittest.TestCase):

    def test_concatena_array(self):
        vendas_sul = np.array([100, 150, 200])
        vendas_norte = np.array([50, 75, 100])
        resultado_esperado = np.array([100, 150, 200, 50, 75, 100])

        resultado_obtido = concatena_array(vendas_sul, vendas_norte)

        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_concatena_array_float(self):
        vendas_sul = np.array([100.5, 150.2, 200.7])
        vendas_norte = np.array([50.3, 75.9, 100.1])
        resultado_esperado = np.array([100.5, 150.2, 200.7, 50.3, 75.9, 100.1])

        resultado_obtido = concatena_array(vendas_sul, vendas_norte)

        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_concatena_array_boolean(self):
        vendas_sul = np.array([True, False])
        vendas_norte = np.array([False, True])
        resultado_esperado = np.array([True, False, False, True])

        resultado_obtido = concatena_array(vendas_sul, vendas_norte)

        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_data_type(self):
        vendas_sul = np.array([100, 150, 200])
        vendas_norte = np.array([50, 75, 100])

        result = concatena_array(vendas_sul, vendas_norte)

        self.assertIsInstance(result, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")
