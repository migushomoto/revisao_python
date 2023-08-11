import unittest
import pandas as pd

class TestCriaDataFramePublico(unittest.TestCase):
    def test_cria_dataframe(self):
        lista = [["Maria", 30, "F", 1.65, 65.0],
                 ["João", 25, "M", 1.75, 80.0],
                 ["Ana", 40, "F", 1.70, 70.0],
                 ["Pedro", 20, "M", 1.80, 75.0],
                 ["Lúcia", 35, "F", 1.60, 55.0]]
        resultado_esperado = pd.DataFrame(lista, columns=["Nome", "Idade", "Sexo", "Altura", "Peso"])
        resultado_obtido = cria_dataframe(lista)
        self.assertTrue(resultado_obtido.equals(resultado_esperado))


    def test_cria_dataframe_2(self):
        lista = [["Maria", 30, "F", 1.65, 65.0],
                 ["João", 25, "M", 1.75, 80.0],
                 ["Ana", 40, "F", 1.70, 70.0],
                 ["Pedro", 20, "M", 1.80, 75.0],
                 ["Lúcia", 35, "F", 1.60, 55.0],
                 ["Carlos", 28, "M", 1.70, 75.0],
                 ["Mariana", 33, "F", 1.62, 60.0],
                 ["Ricardo", 45, "M", 1.80, 85.0],
                 ["Lucas", 27, "M", 1.85, 78.0],
                 ["Fernanda", 31, "F", 1.68, 62.0]]
        resultado_esperado = pd.DataFrame(lista, columns=["Nome", "Idade", "Sexo", "Altura", "Peso"])
        resultado_obtido = cria_dataframe(lista)
        self.assertTrue(resultado_obtido.equals(resultado_esperado))
