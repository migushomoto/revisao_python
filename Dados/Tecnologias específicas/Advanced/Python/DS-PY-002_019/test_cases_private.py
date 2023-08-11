import unittest


class VeiculosTest(unittest.TestCase):
    def test_criar_carro(self):
        carro = registrar_veiculo(
            qtd_passageiros=4,
            tipo_negociacao='aluguel',
            condicao='usado',
            placa='1234abcd'
        )
        self.assertIsInstance(carro, Carro)
        self.assertIsInstance(carro, Veiculo)

    def test_criar_onibus(self):
        onibus = registrar_veiculo(
            qtd_passageiros=40,
            tipo_negociacao='aluguel',
            condicao='usado',
            placa='1234abcd'
        )
        self.assertIsInstance(onibus, Onibus)
        self.assertIsInstance(onibus, Veiculo)

    def test_criar_carro_erro_tipo_negociacao(self):
        with self.assertRaises(ValueError):
            carro = registrar_veiculo(
                qtd_passageiros=2,
                tipo_negociacao='doação',
                condicao='novo',
                placa='abcd1234'
            )

    def test_criar_carro_erro_condicao(self):
        with self.assertRaises(ValueError):
            carro = registrar_veiculo(
                qtd_passageiros=2,
                tipo_negociacao='aluguel',
                condicao='quebrado',
                placa='abcd1234'
            )

    def test_criar_carro_erro_placa(self):
        with self.assertRaises(ValueError):
            carro = registrar_veiculo(
                qtd_passageiros=2,
                tipo_negociacao='aluguel',
                condicao='novo',
                placa='abcd'
            )