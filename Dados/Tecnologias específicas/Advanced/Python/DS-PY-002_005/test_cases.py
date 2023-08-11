import unittest


class TestPessoa(unittest.TestCase):
    def test_pessoa_mensalista_total(self):
        p = PessoaMensalista(
            nome="Joao",
            idade=32,
            total_horas_trabalhadas=160,
            valor_salario=5000,
        )
        self.assertEqual(
            p.calcular_salario(), "A pessoa de nome Joao tem a receber R$ 5000"
        )

    def test_pessoa_mensalista_parcial(self):
        p = PessoaMensalista(
            nome="Paulo",
            idade=28,
            total_horas_trabalhadas=80,
            valor_salario=5000,
        )
        self.assertEqual(
            p.calcular_salario(), "A pessoa de nome Paulo tem a receber R$ 2500"
        )

    def test_pessoa_horista(self):
        p = PessoaHorista(
            nome="Maria", idade=26, total_horas_trabalhadas=100, valor_hora=50
        )
        self.assertEqual(
            p.calcular_salario(), "A pessoa de nome Maria tem a receber R$ 5000"
        )

    def test_pessoa_sem_apontamento(self):
        p = PessoaSemApontamento(nome="Jorge", idade=54, valor_salario=8000)
        self.assertEqual(
            p.calcular_salario(), "A pessoa de nome Jorge tem a receber R$ 8000"
        )


if __name__ == "__main__":
    unittest.main()
