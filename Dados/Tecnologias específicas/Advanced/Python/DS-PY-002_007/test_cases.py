import unittest

class CaixaTest(unittest.TestCase):
    def test_nova_caixa(self):
        caixa = Caixa(qtd_max_objetos=10)
        self.assertEqual(caixa.listar_itens(), '')

    def test_caixa_ok(self):
        caixa = Caixa(qtd_max_objetos=2)
        obj1 = Objeto(nome='prego', tipo='material_construcao')
        obj2 = Objeto(nome='cartolina', tipo='material escolar')
        caixa.adicionar_objeto(obj1)
        caixa.adicionar_objeto(obj2)
        self.assertEqual(caixa.listar_itens(), 'cartolina\nprego')

    def test_caixa_objetos_excedentes(self):
        caixa = Caixa(qtd_max_objetos=2)
        obj1 = Objeto(nome='prego', tipo='material_construcao')
        obj2 = Objeto(nome='cartolina', tipo='material escolar')
        caixa.adicionar_objeto(obj1)
        caixa.adicionar_objeto(obj2)
        obj3 = Objeto(nome='banana', tipo='fruta')
        self.assertFalse(caixa.adicionar_objeto(obj3))

