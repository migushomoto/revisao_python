
def registrar_veiculo(qtd_passageiros, tipo_negociacao, condicao, placa):
    if qtd_passageiros > 5:
        v = Onibus(qtd_passageiros, condicao, tipo_negociacao, placa)
    else:
        v = Carro(qtd_passageiros, condicao, tipo_negociacao, placa)

    return v


class Veiculo:
    def __init__(self, qtd_passageiros, condicao, tipo_negociacao, placa):
        self._qtd_passageiros = None
        self._tipo_negociacao = None
        self._condicao = None
        self._placa = None

        self.qtd_passageiros = qtd_passageiros
        self.condicao = condicao
        self.tipo_negociacao = tipo_negociacao
        self.placa = placa

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, valor):
        if len(str(valor)) != 8:
            raise ValueError()

    @property
    def tipo_negociacao(self):
        return self._tipo_negociacao

    @tipo_negociacao.setter
    def tipo_negociacao(self, valor):
        if valor not in ('aluguel', 'venda'):
            raise ValueError()
        self._tipo_negociacao = valor

    @property
    def qtd_passageiros(self):
        return self._qtd_passageiros

    @qtd_passageiros.setter
    def qtd_passageiros(self, valor):
        self._qtd_passageiros = valor

    @property
    def condicao(self):
        return self._condicao

    @condicao.setter
    def condicao(self, valor):
        if valor not in ('novo', 'usado'):
            raise ValueError()
        self._condicao = valor


class Carro(Veiculo):
    def __init__(self, qtd_passageiros, condicao, tipo_negociacao, placa):
        super().__init__(qtd_passageiros, condicao, tipo_negociacao, placa)


class Onibus(Veiculo):
    def __init__(self, qtd_passageiros, condicao, tipo_negociacao, placa):
        super().__init__(qtd_passageiros, condicao, tipo_negociacao, placa)

