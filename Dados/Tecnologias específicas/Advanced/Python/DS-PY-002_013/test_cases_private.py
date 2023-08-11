import unittest


class TranscritorTest(unittest.TestCase):
    def test_transcript(self):
        t = Transcritor(111)
        self.assertEquals(t.transcrever(), "um um um")
        t = Transcritor(42)
        self.assertEquals(t.transcrever(), "quatro dois")
        t = Transcritor(7123)
        self.assertEquals(t.transcrever(), "sete um dois três")

    def test_transcript_soma(self):
        t1 = Transcritor(400)
        t2 = Transcritor(23)
        t3 = t1 + t2
        self.assertEqual(t3.transcrever(), "quatro dois três")

    def test_transcript_soma_str(self):
        t1 = Transcritor(400)
        t2 = Transcritor(23)
        t3 = t1 + t2
        self.assertEqual(str(t3), "quatro dois três")

    def test_transcript_negativo(self):
        t1 = Transcritor(20)
        t2 = Transcritor(25)
        t3 = t1 - t2
        self.assertEqual(t3.transcrever(), "menos cinco")

    def test_transcript_multiplicacao(self):
        t1 = Transcritor(20)
        t2 = Transcritor(150)
        t3 = t1 * t2
        self.assertEqual(t3.transcrever(), "três zero zero zero")

    def test_transcript_divisao(self):
        t1 = Transcritor(900)
        t2 = Transcritor(30)
        t3 = t1 // t2
        self.assertEqual(t3.transcrever(), "três zero")

    def test_transcript_divisao_inteira(self):
        t1 = Transcritor(910)
        t2 = Transcritor(30)
        t3 = t1 // t2
        self.assertEqual(t3.transcrever(), "três zero")