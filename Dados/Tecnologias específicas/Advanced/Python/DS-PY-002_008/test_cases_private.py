import unittest

class CaixaRegistradoraTest(unittest.TestCase):
    def test_01_criacao_caixa_registradora(self):
        c = CaixaRegistradora()
        self.assertIs(type(c), CaixaRegistradora)

    def test_02_criacao_venda(self):
        c = CaixaRegistradora()
        v = c.iniciar_venda()
        self.assertIs(type(v), Venda)

    def test_03_adicionar_produto(self):
        c = CaixaRegistradora()
        v = c.iniciar_venda()
        v.adicionar_produto(nome='arroz', valor_unitario=15.0, qtd_produtos=2)
        self.assertEqual(
            v.listar_produtos(),
            (('arroz', 15.0, 2, 30.0), )
        )

    def test_04_adicionar_produtos(self):
        c = CaixaRegistradora()
        v = c.iniciar_venda()
        v.adicionar_produto(nome='arroz', valor_unitario=15.0, qtd_produtos=2)
        v.adicionar_produto(nome='carne', valor_unitario=7.50, qtd_produtos=4)
        self.assertEqual(
            v.listar_produtos(),
            (
                ('arroz', 15.0, 2, 30.0),
                ('carne', 7.50, 4, 30.0),
            )
        )

    def test_05_validar_total(self):
        c = CaixaRegistradora()
        v = c.iniciar_venda()
        v.adicionar_produto(nome='arroz', valor_unitario=15.0, qtd_produtos=2)
        v.adicionar_produto(nome='carne', valor_unitario=7.50, qtd_produtos=4)
        self.assertEqual(
            v.obter_valor_total(),
            60.0
        )

    def test_06_validar_total_caixa_registradora(self):
        c = CaixaRegistradora()
        venda_1 = c.iniciar_venda()
        venda_1.adicionar_produto(nome='banana', valor_unitario=1.50, qtd_produtos=10)
        venda_1.adicionar_produto(nome='carne', valor_unitario=7.50, qtd_produtos=4)
        self.assertEqual(
            venda_1.obter_valor_total(),
            45.0
        )
        venda_1.finalizar_venda(c)
        self.assertEqual(c.obter_saldo_atual(), 45.0)

        venda_2 = c.iniciar_venda()
        venda_2.adicionar_produto(nome='banana', valor_unitario=2.00, qtd_produtos=4)
        venda_2.adicionar_produto(nome='queijo', valor_unitario=2.00, qtd_produtos=6)
        self.assertEqual(
            venda_2.obter_valor_total(),
            20.0
        )
        venda_2.finalizar_venda(c)
        self.assertEqual(c.obter_saldo_atual(), 65.0)
