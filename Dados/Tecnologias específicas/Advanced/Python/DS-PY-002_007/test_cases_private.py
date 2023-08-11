import unittest

class CaixaTest(unittest.TestCase):
    def test_nova_caixa(self):
        caixa = Caixa(qtd_max_objetos=10)
        self.assertEqual(caixa.listar_itens(), '')

    def test_caixa_ok(self):
        caixa = Caixa(qtd_max_objetos=4)
        obj1 = Objeto(nome='martelo', tipo='material_construcao')
        obj2 = Objeto(nome='sulfite', tipo='material escolar')
        obj3 = Objeto(nome='prego', tipo='material_construcao')
        obj4 = Objeto(nome='caderno', tipo='material escolar')
        caixa.adicionar_objeto(obj1)
        caixa.adicionar_objeto(obj2)
        caixa.adicionar_objeto(obj3)
        caixa.adicionar_objeto(obj4)
        self.assertEqual(caixa.listar_itens(), 'caderno\nmartelo\nprego\nsulfite')

    def test_caixa_objetos_excedentes(self):
        caixa = Caixa(qtd_max_objetos=2)
        obj1 = Objeto(nome='martelo', tipo='material_construcao')
        obj2 = Objeto(nome='sulfite', tipo='material escolar')
        caixa.adicionar_objeto(obj1)
        caixa.adicionar_objeto(obj2)
        obj3 = Objeto(nome='laranja', tipo='fruta')
        self.assertFalse(caixa.adicionar_objeto(obj3))

