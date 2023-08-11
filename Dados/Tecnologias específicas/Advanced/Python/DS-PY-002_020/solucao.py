
class Loja:
    def __init__(self):
        self._itens_a_venda = []

    @property
    def itens_a_venda(self):
        return self._itens_a_venda

    def adicionar_item(self, item):
        if not isinstance(item, Roupa):
            raise ValueError
        self._itens_a_venda.append(item)

    def aplicar_desconto(self, valor_desconto):
        porc_desconto = valor_desconto / 100
        for pos, item in enumerate(self._itens_a_venda):
            self._itens_a_venda[pos].definir_preco(
                item.obter_preco() - (item.obter_preco() * porc_desconto)
            )

class Roupa:
    def __init__(self, tamanho):
        self._tamanho = tamanho
        self._preco = 0.0

    def definir_preco(self, valor):
        self._preco = valor

    def obter_preco(self):
        return self._preco


class Camiseta(Roupa):
    def __init__(self, tamanho, cor):
        super().__init__(tamanho=tamanho)
        self_cor = cor

class Camisa(Roupa):
    def __init__(self, tamanho, tamanho_manga, estilo):
        super().__init__(tamanho=tamanho)
        self._tamanho_manga = tamanho_manga
        self._estilo = estilo

class Calca(Roupa):
    def __init__(self, tamanho, cor, modelo):
        super().__init__(tamanho=tamanho)
        self._cor = cor
        self._modelo = modelo