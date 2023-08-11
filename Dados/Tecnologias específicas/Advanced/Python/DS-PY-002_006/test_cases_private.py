import unittest

class EstudanteTest(unittest.TestCase):
    def test_novo_estudante(self):
        e = Estudante(nome="Anakin")
        e.adicionar_notas(2, 2, 4, 4)
        self.assertEqual(e.obter_media(), 3)

    def test_novo_estudante_lista_notas(self):
        e = Estudante(nome="Anakin")
        e.adicionar_notas((2, 2, 4, 4))
        self.assertEqual(e.obter_media(), 3)

    def test_novo_estudante_qtd_notas_errada(self):
        e = Estudante(nome="Han")
        with self.assertRaises(QuantidadeErradaNotasError):
            e.adicionar_notas(1, 2, 3)

    def test_notas_primeira_prova(self):
        t = Turma(nome="Turma 3")
        aluno_01 = Estudante(nome='Luke')
        aluno_01.adicionar_notas(1, 2, 3, 4)
        t.adicionar_estudante(123, aluno_01)

        aluno_02 = Estudante(nome='Padmé')
        aluno_02.adicionar_notas(1, 9,9,9)
        t.adicionar_estudante(124, aluno_02)

        aluno_03 = Estudante(nome='Luke')
        aluno_03.adicionar_notas(1, 7, 9, 9)
        t.adicionar_estudante(125, aluno_03)

        self.assertEqual(t.obter_media_prova(1), 1)

    def test_adicionar_estudante_ja_registrado(self):
        t = Turma(nome="Turma 4")
        aluno_01 = Estudante(nome="Leia")
        aluno_01.adicionar_notas(9,9,9,9)
        t.adicionar_estudante(2, aluno_01)

        with self.assertRaises(EstudanteJaRegistradoError):
            aluno_02 = Estudante(nome="Ben")
            aluno_02.adicionar_notas(9, 7, 9, 9)
            t.adicionar_estudante(2, aluno_02)

if __name__ == "__main__":
    unittest.main()
