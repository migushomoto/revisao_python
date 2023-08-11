import unittest


class VeiculosTest(unittest.TestCase):
    def test_criar_carro(self):
        carro = registrar_veiculo(
            qtd_passageiros=4,
            tipo_negociacao='venda',
            condicao='usado',
            placa='q1w2e3r4'
        )
        self.assertIsInstance(carro, Carro)
        self.assertIsInstance(carro, Veiculo)

    def test_criar_onibus(self):
        onibus = registrar_veiculo(
            qtd_passageiros=40,
            tipo_negociacao='venda',
            condicao='usado',
            placa='q1w2e3r4'
        )
        self.assertIsInstance(onibus, Onibus)
        self.assertIsInstance(onibus, Veiculo)

    def test_criar_carro_erro_tipo_negociacao(self):
        with self.assertRaises(ValueError):
            carro = registrar_veiculo(
                qtd_passageiros=2,
                tipo_negociacao='emprestimo',
                condicao='novo',
                placa='qwer1234'
            )

    def test_criar_carro_erro_condicao(self):
        with self.assertRaises(ValueError):
            carro = registrar_veiculo(
                qtd_passageiros=2,
                tipo_negociacao='venda',
                condicao='quebrado',
                placa='qwer1234'
            )

    def test_criar_carro_erro_placa(self):
        with self.assertRaises(ValueError):
            carro = registrar_veiculo(
                qtd_passageiros=2,
                tipo_negociacao='venda',
                condicao='novo',
                placa='qwer'
            )