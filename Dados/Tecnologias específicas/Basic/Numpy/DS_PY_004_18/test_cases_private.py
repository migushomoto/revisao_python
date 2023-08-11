import unittest
import numpy as np

class TestConcatenacaoArrays(unittest.TestCase):

    def test_concatena_array(self):
        vendas_sul = np.array([300, 400, 500])
        vendas_norte = np.array([200, 250, 300])
        resultado_esperado = np.array([300, 400, 500, 200, 250, 300])

        resultado_obtido = concatena_array(vendas_sul, vendas_norte)

        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_concatena_array_float(self):
        vendas_sul = np.array([100.5, 150.2, 200.7])
        vendas_norte = np.array([50.3, 75.9, 100.1])
        resultado_esperado = np.array([100.5, 150.2, 200.7, 50.3, 75.9, 100.1])

        resultado_obtido = concatena_array(vendas_sul, vendas_norte)

        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_concatena_array_boolean(self):
        vendas_sul = np.array([True, False, True])
        vendas_norte = np.array([False, True])
        resultado_esperado = np.array([True, False, True, False, True])

        resultado_obtido = concatena_array(vendas_sul, vendas_norte)

        self.assertTrue(np.array_equal(resultado_obtido, resultado_esperado))

    def test_data_type(self):
        vendas_sul = np.array([50, 150, 200])
        vendas_norte = np.array([150, 75, 100])

        result = concatena_array(vendas_sul, vendas_norte)

        self.assertIsInstance(result, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")
