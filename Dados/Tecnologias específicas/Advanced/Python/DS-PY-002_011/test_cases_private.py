import unittest

class ClienteTest(unittest.TestCase):
    def test_criar_cliente(self):
        cliente = Cliente()
        cliente.nome_completo = "Maria Lopes"
        cliente.data_de_nascimento = "11/06/1997"
        self.assertEqual(cliente.idade_em_anos, 26)
        self.assertEqual(cliente.nome, "Maria")

    def teste_criar_cliente_nome_errado(self):
        cliente = Cliente()
        with self.assertRaises(ValueError):
            cliente.nome_completo = "José"

    def teste_criar_cliente_data_nascimento_errada(self):
        cliente = Cliente()
        with self.assertRaises(ValueError):
            cliente.data_de_nascimento = "11/11/2050"

