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
        v.adicionar_produto(nome='banana', valor_unitario=1.50, qtd_produtos=10.0)
        self.assertEqual(
            v.listar_produtos(),
            (('banana', 1.50, 10.0, 15.0), )
        )

    def test_04_adicionar_produtos(self):
        c = CaixaRegistradora()
        v = c.iniciar_venda()
        v.adicionar_produto(nome='banana', valor_unitario=1.50, qtd_produtos=10.0)
        v.adicionar_produto(nome='detergente', valor_unitario=7.50, qtd_produtos=2)
        self.assertEqual(
            v.listar_produtos(),
            (
                ('banana', 1.50, 10.0, 15.0),
                ('detergente', 7.50, 2.0, 15.0),
            )
        )

    def test_05_validar_total(self):
        c = CaixaRegistradora()
        v = c.iniciar_venda()
        v.adicionar_produto(nome='banana', valor_unitario=1.50, qtd_produtos=10.0)
        v.adicionar_produto(nome='detergente', valor_unitario=7.50, qtd_produtos=2)
        self.assertEqual(
            v.obter_valor_total(),
            30.0
        )

    def test_06_validar_total_caixa_registradora(self):
        c = CaixaRegistradora()
        venda_1 = c.iniciar_venda()
        venda_1.adicionar_produto(nome='banana', valor_unitario=1.50, qtd_produtos=10)
        venda_1.adicionar_produto(nome='detergente', valor_unitario=7.50, qtd_produtos=2)
        self.assertEqual(
            venda_1.obter_valor_total(),
            30.0
        )
        venda_1.finalizar_venda(c)
        self.assertEqual(c.obter_saldo_atual(), 30.0)

        venda_2 = c.iniciar_venda()
        venda_2.adicionar_produto(nome='maçã', valor_unitario=2.00, qtd_produtos=4)
        venda_2.adicionar_produto(nome='pão', valor_unitario=2.00, qtd_produtos=6)
        self.assertEqual(
            venda_2.obter_valor_total(),
            20.0
        )
        venda_2.finalizar_venda(c)
        self.assertEqual(c.obter_saldo_atual(), 50.0)
