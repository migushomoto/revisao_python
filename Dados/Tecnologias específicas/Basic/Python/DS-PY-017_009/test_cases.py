import unittest

class TestPrecoCelular(unittest.TestCase):
    def test_mediaPrecoCelular(self):
        self.assertEqual(mediaPrecoCelular({"dispositivo": ["a", "b", "c", "d", "e"],  "valor":[638, 622, 784, 681, 790]}), [703, 622, 790])
        self.assertEqual(mediaPrecoCelular({"dispositivo": ["a", "b", "c", "d", "e"],  "valor":[631, 1534, 659, 735, 1579]}), [1027.6, 631, 1579])
        self.assertEqual(mediaPrecoCelular({"dispositivo": ["a", "b", "c", "d", "e"],  "valor":[1560, 1959, 2515, 1311, 2696]}), [2008.2, 1311, 2696])
