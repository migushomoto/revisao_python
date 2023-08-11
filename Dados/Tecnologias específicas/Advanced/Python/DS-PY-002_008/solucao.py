class Venda:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome: str, valor_unitario: float, qtd_produtos: float):
        self.produtos.append((nome, valor_unitario, qtd_produtos, valor_unitario * qtd_produtos))

    def listar_produtos(self):
        return tuple(self.produtos)

    def obter_valor_total(self):
        total = 0
        for item in self.produtos:
            total += item[-1]
        return total

    def finalizar_venda(self, caixa_registradora):
        caixa_registradora.adicionar_pagamento(self.obter_valor_total())


class CaixaRegistradora:
    def __init__(self):
        self.saldo_total = 0.0

    def iniciar_venda(self):
        return Venda()

    def obter_saldo_atual(self):
        return self.saldo_total

    def adicionar_pagamento(self, total: float):
        self.saldo_total += total