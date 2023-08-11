class Transcritor:
    def __init__(self, numero_inteiro: int):
        self.__numero = numero_inteiro
        self.__transcricoes = {
            "0": "zero",
            "1": "um",
            "2": "dois",
            "3": "três",
            "4": "quatro",
            "5": "cinco",
            "6": "seis",
            "7": "sete",
            "8": "oito",
            "9": "nove",
            "-": "menos",
        }

    def transcrever(self):
        e = []
        s = str(self.__numero)
        for n in s:
            e.append(self.__transcricoes[n])
        return " ".join(e)

    def __add__(self, other):
        return Transcritor(self.__numero + other.__numero)

    def __sub__(self, other):
        return Transcritor(self.__numero - other.__numero)

    def __str__(self) -> str:
        return self.transcrever()

    def __mul__(self, other):
        return Transcritor(self.__numero * other.__numero)

    def __floordiv__(self, other):
        return Transcritor(self.__numero // other.__numero)
