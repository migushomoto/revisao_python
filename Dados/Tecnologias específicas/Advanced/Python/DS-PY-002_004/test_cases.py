import unittest
from datetime import datetime

class TestPessoa(unittest.TestCase):
    def test_pessoa(self):
        p = Pessoa.nova_pessoa(
            nome="José", sobrenome="Santos", cidade_de_residencia="São Paulo"
        )
        self.assertIsInstance(p, Pessoa)
        self.assertEqual(p.nome, "José")
        self.assertEqual(p.sobrenome, "Santos")
        self.assertEqual(p.cidade_de_residencia, "São Paulo")
        self.assertIsInstance(p._data_de_criacao, datetime)
