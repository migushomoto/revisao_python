import unittest
import pandas as pd

class TestCriaDataFramePrivado(unittest.TestCase):
    def test_cria_dataframe(self):
        lista = [["Carlos", 28, "M", 1.70, 75.0],
                 ["Mariana", 33, "F", 1.62, 60.0],
                 ["Ricardo", 45, "M", 1.80, 85.0]]
        resultado_esperado = pd.DataFrame(lista, columns=["Nome", "Idade", "Sexo", "Altura", "Peso"])
        resultado_obtido = cria_dataframe(lista)
        self.assertTrue(resultado_obtido.equals(resultado_esperado))

    def test_cria_dataframe_2(self):
        lista = [["Lucas", 27, "M", 1.85, 78.0],
                 ["Fernanda", 31, "F", 1.68, 62.0],
                 ["Gabriel", 22, "M", 1.78, 70.0],
                 ["Carolina", 29, "F", 1.73, 68.0],
                 ["Rafael", 26, "M", 1.81, 75.0],
                 ["Amanda", 24, "F", 1.63, 58.0],
                 ["Felipe", 30, "M", 1.79, 72.0],
                 ["Isabela", 32, "F", 1.70, 64.0],
                 ["Thiago", 28, "M", 1.77, 80.0],
                 ["Juliana", 27, "F", 1.67, 61.0]]
        resultado_esperado = pd.DataFrame(lista, columns=["Nome", "Idade", "Sexo", "Altura", "Peso"])
        resultado_obtido = cria_dataframe(lista)
        self.assertTrue(resultado_obtido.equals(resultado_esperado))
