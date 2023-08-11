import datetime
import unittest


class ProdutoTest(unittest.TestCase):
    def test_produto_correto(self):
        p = Produto(
            nome_produto="Aquecedor",
            dt_lancamento=datetime.datetime(year=2023, month=8, day=1),
            descricao="Aquecedor que aquece muito"
        )

        self.assertEqual(p.nome_produto, "Aquecedor")
        self.assertEqual(p.dt_lancamento, datetime.datetime(2023, 8, 1))
        self.assertEqual(p.descricao, "Aquecedor que aquece muito")
        self.assertTrue(p.em_venda)

    def test_produto_correto_ainda_nao_lancado(self):
        p = Produto(
            nome_produto="Aquecedor",
            dt_lancamento=datetime.datetime(year=2026, month=8, day=1),
            descricao="Aquecedor que aquece muito"
        )

        self.assertEqual(p.nome_produto, "Aquecedor")
        self.assertEqual(p.dt_lancamento, datetime.datetime(2026, 8, 1))
        self.assertEqual(p.descricao, "Aquecedor que aquece muito")
        self.assertFalse(p.em_venda)

    def test_produto_nome_incorreto(self):
        with self.assertRaises(ValueError):
            p = Produto(
                nome_produto="Aquecedor ultra mega poderoso com o nome gigantesco",
                dt_lancamento=datetime.datetime(year=2023, month=8, day=1),
                descricao="Aquecedor que aquece muito"
            )

    def test_produto_descricao_incorreta(self):
        with self.assertRaises(ValueError):
            p = Produto(
                nome_produto="Aquecedor",
                dt_lancamento=datetime.datetime(year=2023, month=8, day=1),
                descricao="Aque"
            )

    def test_produto_data_incorreta(self):
        with self.assertRaises(ValueError):
            p = Produto(
                nome_produto="Aquecedor",
                dt_lancamento='1/8/2023',
                descricao="Aquecedor muito bom"
            )

