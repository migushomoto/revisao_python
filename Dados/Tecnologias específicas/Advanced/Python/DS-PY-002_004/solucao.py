from datetime import datetime


class Pessoa:
    """Define o objeto pessoa"""

    def __init__(self, nome: str, sobrenome: str, cidade_de_residencia: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cidade_de_residencia = cidade_de_residencia
        self._data_de_criacao = datetime.now()

    @staticmethod
    def nova_pessoa(nome: str, sobrenome: str, cidade_de_residencia: str):
        """cria uma nova pessoa"""
        p = Pessoa(nome, sobrenome, cidade_de_residencia)
        return p


if __name__ == "__main__":
    print("Modulo nao habilitado para chamada direta")
