class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self._mensagem = "A pessoa de nome {nome} tem a receber R$ {salario}"


class PessoaHorista(Pessoa):
    def __init__(
        self,
        nome: str,
        idade: int,
        total_horas_trabalhadas: int,
        valor_hora: int,
    ) -> None:
        super().__init__(nome, idade)
        self.total_horas_trabalhadas = total_horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self) -> str:
        return self._mensagem.format(
            nome=self.nome,
            salario=int(self.total_horas_trabalhadas * self.valor_hora),
        )


class PessoaMensalista(Pessoa):
    def __init__(
        self,
        nome: str,
        idade: int,
        total_horas_trabalhadas: int,
        valor_salario: int,
    ) -> None:
        super().__init__(nome, idade)
        self.total_horas_trabalhadas = total_horas_trabalhadas
        self.valor_salario = valor_salario

    def calcular_salario(self) -> str:
        salario_a_receber = self.valor_salario
        if self.total_horas_trabalhadas < 160:
            valor_hora = self.valor_salario / 160
            salario_a_receber = self.total_horas_trabalhadas * valor_hora

        return self._mensagem.format(
            nome=self.nome,
            salario=int(salario_a_receber),
        )


class PessoaSemApontamento(Pessoa):
    def __init__(self, nome: str, idade: int, valor_salario: int) -> None:
        super().__init__(nome, idade)
        self.valor_salario = valor_salario

    def calcular_salario(self) -> str:
        return self._mensagem.format(nome=self.nome, salario=self.valor_salario)
