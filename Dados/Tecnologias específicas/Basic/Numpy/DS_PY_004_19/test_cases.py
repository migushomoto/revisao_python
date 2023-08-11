import unittest
import numpy as np


class PublicTransacoesTestCase(unittest.TestCase):
    def setUp(self):
        self.transacoes = np.array([100.0, 200.0, 50.0, 300.0, 250.0, 120.0, 80.0, 500.0])

    def test_medidas_estatisticas(self):
        result = analisa_transacoes(self.transacoes)
        expected_result = np.array([200.0, 139.55285736952862, 50.0, 500.0, 160.0, 95.0, 262.5])
        np.testing.assert_allclose(result, expected_result, rtol=1e-6, atol=1e-6, err_msg="Medidas não conferem")

    def test_return_type(self):
        result = analisa_transacoes(self.transacoes)
        self.assertIsInstance(result, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")