import datetime


class Produto:
    def __init__(self, nome_produto, dt_lancamento, descricao):
        self._nome_produto = None
        self._dt_lancamento = None
        self._descricao = None

        self.nome_produto = nome_produto
        self.dt_lancamento = dt_lancamento
        self.descricao = descricao

    @property
    def nome_produto(self):
        return self._produto

    @nome_produto.setter
    def nome_produto(self, valor):
        if len(str(valor)) < 5 or len(str(valor)) > 30:
            raise ValueError("Nome de Produto invalido")
        self._produto = valor

    @property
    def dt_lancamento(self):
        return self._dt_lancamento

    @dt_lancamento.setter
    def dt_lancamento(self, valor):
        if type(valor) is not datetime.datetime:
            raise ValueError("Data de Lancamento invalida")
        self._dt_lancamento = valor

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        if len(str(valor)) < 5 or len(str(valor)) > 200:
            raise ValueError('Descricao invalida')
        self._descricao = valor

    @property
    def em_venda(self):
        return not(self._dt_lancamento > datetime.datetime.now())