import datetime
import unittest


class ProdutoTest(unittest.TestCase):
    def test_produto_correto(self):
        p = Produto(
            nome_produto="Geladeira",
            dt_lancamento=datetime.datetime(year=2020, month=1, day=15),
            descricao="Geladeira que gela muito"
        )

        self.assertEqual(p.nome_produto, "Geladeira")
        self.assertEqual(p.dt_lancamento, datetime.datetime(2020, 1, 15))
        self.assertEqual(p.descricao, "Geladeira que gela muito")
        self.assertTrue(p.em_venda)

    def test_produto_correto_ainda_nao_lancado(self):
        p = Produto(
            nome_produto="Geladeira",
            dt_lancamento=datetime.datetime(year=2026, month=1, day=15),
            descricao="Geladeira que gela muito"
        )

        self.assertEqual(p.nome_produto, "Geladeira")
        self.assertEqual(p.dt_lancamento, datetime.datetime(2026, 1, 15))
        self.assertEqual(p.descricao, "Geladeira que gela muito")
        self.assertFalse(p.em_venda)

    def test_produto_nome_incorreto(self):
        with self.assertRaises(ValueError):
            p = Produto(
                nome_produto="Geladeira ultra mega poderosa com o nome gigantesco",
                dt_lancamento=datetime.datetime(year=2020, month=1, day=15),
                descricao="Geladeira que gela muito"
            )

    def test_produto_descricao_incorreta(self):
        with self.assertRaises(ValueError):
            p = Produto(
                nome_produto="Geladeira",
                dt_lancamento=datetime.datetime(year=2020, month=1, day=15),
                descricao="Gela"
            )

    def test_produto_data_incorreta(self):
        with self.assertRaises(ValueError):
            p = Produto(
                nome_produto="Geladeira",
                dt_lancamento='15/1/2020',
                descricao="Geladeira muito boa"
            )

