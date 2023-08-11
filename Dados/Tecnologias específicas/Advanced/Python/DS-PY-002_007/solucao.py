
class Objeto:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo

class Caixa:
    def __init__(self, qtd_max_objetos: int):
        self.qtd_max_objetos = qtd_max_objetos
        self.objetos: list[Objeto] = []

    def adicionar_objeto(self, objeto: Objeto):
        if len(self.objetos) >= self.qtd_max_objetos:
            return False
        self.objetos.append(objeto)
        return True

    def listar_itens(self):
        nomes_objetos = [o.nome
                         for o in self.objetos]
        nomes_objetos_sorted = sorted(nomes_objetos)
        return '\n'.join(nomes_objetos_sorted)