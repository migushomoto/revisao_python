import unittest

class TestPrecoCelular(unittest.TestCase):
    def test_mediaPrecoCelular(self):
        self.assertEqual(mediaPrecoCelular({"dispositivo": ["a", "b", "c", "d", "e"],  "valor":[2537, 603, 1970, 1693, 2681]}), [1896.8, 603, 2681])
        self.assertEqual(mediaPrecoCelular({"dispositivo": ["a", "b", "c", "d", "e"],  "valor":[2318, 2552, 1231, 1625, 2378]}), [2020.8,1231, 2552])
        self.assertEqual(mediaPrecoCelular({"dispositivo": ["a", "b", "c", "d", "e"],  "valor":[2329, 999, 2456, 2327, 1471]}), [1916.4, 999, 2456])
