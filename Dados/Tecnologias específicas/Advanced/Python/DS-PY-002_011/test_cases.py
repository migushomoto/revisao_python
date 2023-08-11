import unittest

class ClienteTest(unittest.TestCase):
    def test_criar_cliente(self):
        cliente = Cliente()
        cliente.nome_completo = "Jose Dantas"
        cliente.data_de_nascimento = "11/10/2000"
        self.assertEqual(cliente.idade_em_anos, 22)
        self.assertEqual(cliente.nome, "Jose")

    def teste_criar_cliente_nome_errado(self):
        cliente = Cliente()
        with self.assertRaises(ValueError):
            cliente.nome_completo = "Mario"

    def teste_criar_cliente_data_nascimento_errada(self):
        cliente = Cliente()
        with self.assertRaises(ValueError):
            cliente.data_de_nascimento = "01/01/2040"

