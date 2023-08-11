import unittest
from datetime import datetime

class TestPessoa(unittest.TestCase):
    def test_pessoa(self):
        p = Pessoa.nova_pessoa(
            nome="Maria", sobrenome="Silva", cidade_de_residencia="Santos"
        )
        self.assertIsInstance(p, Pessoa)
        self.assertEqual(p.nome, "Maria")
        self.assertEqual(p.sobrenome, "Silva")
        self.assertEqual(p.cidade_de_residencia, "Santos")
        self.assertIsInstance(p._data_de_criacao, datetime)
