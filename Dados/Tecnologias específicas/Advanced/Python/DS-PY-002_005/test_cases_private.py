import unittest


class TestPessoa(unittest.TestCase):
    def test_pessoa_mensalista_total(self):
        p = PessoaMensalista(
            nome="José",
            idade=20,
            total_horas_trabalhadas=200,
            valor_salario=10000,
        )
        self.assertEqual(
            p.calcular_salario(), "A pessoa de nome José tem a receber R$ 10000"
        )

    def test_pessoa_mensalista_parcial(self):
        p = PessoaMensalista(
            nome="Márcia",
            idade=28,
            total_horas_trabalhadas=80,
            valor_salario=4000,
        )
        self.assertEqual(
            p.calcular_salario(), "A pessoa de nome Márcia tem a receber R$ 2000"
        )

    def test_pessoa_horista(self):
        p = PessoaHorista(
            nome="Maria", idade=41, total_horas_trabalhadas=140, valor_hora=80
        )
        self.assertEqual(
            p.calcular_salario(), "A pessoa de nome Maria tem a receber R$ 11200"
        )

    def test_pessoa_sem_apontamento(self):
        p = PessoaSemApontamento(nome="Manuel", idade=54, valor_salario=9000)
        self.assertEqual(
            p.calcular_salario(), "A pessoa de nome Manuel tem a receber R$ 9000"
        )


if __name__ == "__main__":
    unittest.main()
