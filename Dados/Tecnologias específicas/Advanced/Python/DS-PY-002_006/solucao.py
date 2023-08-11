

class QuantidadeErradaNotasError(Exception):
    pass


class EstudanteJaRegistradoError(Exception):
    pass


class Estudante:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.notas = []

    def adicionar_notas(self, *args):
        self._validar_notas(args)

        notas = args[:]
        if type(args[0]) in (list, tuple):
            notas = args[0][:]
        self.notas.extend(notas)

        return self

    def _validar_notas(self, lista_notas: list):
        if len(lista_notas) == 4 or (len(lista_notas) == 1 and len(lista_notas[0]) == 4):
            try:
                l = map(float, lista_notas)
                return  # tudo certo
            except Exception:
                raise QuantidadeErradaNotasError()

        raise QuantidadeErradaNotasError()

    def obter_media(self):
        return sum(self.notas) / len(self.notas)

class Turma:
    def __init__(self, nome: str):
        self.estudantes: list[dict] = []
        self.nome = nome

    def adicionar_estudante(self, nro_matricula: int, estudante: Estudante):
        if nro_matricula in [e['nro_matricula'] for e in self.estudantes]:
            raise EstudanteJaRegistradoError()
        self.estudantes.append({'nro_matricula': nro_matricula, 'estudante': estudante})
        return estudante

    def obter_media_prova(self, nro_prova: int):
        todas_notas = [e['estudante'].notas for e in self.estudantes]
        notas_provas = []
        for n in todas_notas:
            notas_provas.append(n[nro_prova-1])
        return sum(notas_provas) / len(notas_provas)