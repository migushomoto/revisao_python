import datetime

class Cliente:
    def __init__(self):
        self._nome_completo = ""
        self._data_de_nascimento = ""

    @property
    def idade_em_anos(self):
        nascimento_date = datetime.datetime.strptime(self._data_de_nascimento, "%d/%m/%Y")
        diferenca_datas = (datetime.datetime.now() - nascimento_date).days
        return diferenca_datas // 365

    @property
    def nome(self):
        return self._nome_completo.split(' ')[0]

    @property
    def nome_completo(self):
        return self._nome_completo

    @nome_completo.setter
    def nome_completo(self, value):
        if len(value.split(" ")) < 2:
            raise ValueError()
        self._nome_completo = value

    @property
    def data_de_nascimento(self):
        return self._data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, value):
        data_de_nascimento_em_datetime = datetime.datetime.strptime(value, "%d/%m/%Y")
        if data_de_nascimento_em_datetime > datetime.datetime.now():
            raise ValueError
        self._data_de_nascimento = value