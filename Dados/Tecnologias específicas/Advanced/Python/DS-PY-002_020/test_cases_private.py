import unittest


class TestLoja(unittest.TestCase):
    def test_criar_loja(self):
        l = Loja()
        self.assertIsInstance(l, Loja)

    def test_adicionar_roupa(self):
        l = Loja()
        camiseta = Camiseta(tamanho='p', cor='preta')
        camiseta.definir_preco(150)
        self.assertEqual(camiseta.obter_preco(), 150)
        l.adicionar_item(camiseta)
        self.assertEqual(len(l.itens_a_venda), 1)

    def test_aplicar_desconto(self):
        l = Loja()
        camiseta = Camiseta(tamanho='p', cor='preta')
        camiseta.definir_preco(80)
        l.adicionar_item(camiseta)
        camisa = Camisa(tamanho='m', tamanho_manga='l', estilo='social')
        camisa.definir_preco(142)
        l.adicionar_item(camisa)
        calca = Calca(tamanho='gg', cor='vermelha', modelo='social')
        calca.definir_preco(180)
        l.adicionar_item(calca)
        l.aplicar_desconto(10)
        self.assertEqual(l.itens_a_venda[0].obter_preco(), 72)
        self.assertEqual(l.itens_a_venda[1].obter_preco(), 127.8)
        self.assertEqual(l.itens_a_venda[2].obter_preco(), 162)
