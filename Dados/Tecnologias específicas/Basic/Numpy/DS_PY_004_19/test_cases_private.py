import unittest
import numpy as np


class PrivateTransacoesTestCase(unittest.TestCase):
    def setUp(self):
        self.transacoes = np.array([400.0, 150.0, 75.0, 600.0, 350.0, 200.0, 180.0, 900.0])

    def test_medidas_estatisticas(self):
        result = analisa_transacoes(self.transacoes)
        expected_result = np.array([356.875   , 258.395742,  75.      , 900.      , 275.      ,172.5     , 450.      ])
        np.testing.assert_allclose(result, expected_result, rtol=1e-6, atol=1e-6, err_msg="Medidas não conferem")

    def test_return_type(self):
        result = analisa_transacoes(self.transacoes)
        self.assertIsInstance(result, np.ndarray, msg="O objeto retornado não é do tipo 'ndarray'")
