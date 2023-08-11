import unittest


class TranscritorTest(unittest.TestCase):
    def test_transcript(self):
        t = Transcritor(100)
        self.assertEquals(t.transcrever(), "um zero zero")
        t = Transcritor(3831)
        self.assertEquals(t.transcrever(), "três oito três um")
        t = Transcritor(7)
        self.assertEquals(t.transcrever(), "sete")

    def test_transcript_soma(self):
        t1 = Transcritor(100)
        t2 = Transcritor(120)
        t3 = t1 + t2
        self.assertEqual(t3.transcrever(), "dois dois zero")

    def test_transcript_soma_str(self):
        t1 = Transcritor(100)
        t2 = Transcritor(120)
        t3 = t1 + t2
        self.assertEqual(str(t3), "dois dois zero")

    def test_transcript_negativo(self):
        t1 = Transcritor(15)
        t2 = Transcritor(20)
        t3 = t1 - t2
        self.assertEqual(t3.transcrever(), "menos cinco")

    def test_transcript_multiplicacao(self):
        t1 = Transcritor(15)
        t2 = Transcritor(20)
        t3 = t1 * t2
        self.assertEqual(t3.transcrever(), "três zero zero")

    def test_transcript_divisao(self):
        t1 = Transcritor(400)
        t2 = Transcritor(20)
        t3 = t1 // t2
        self.assertEqual(t3.transcrever(), "dois zero")

    def test_transcript_divisao_inteira(self):
        t1 = Transcritor(410)
        t2 = Transcritor(20)
        t3 = t1 // t2
        self.assertEqual(t3.transcrever(), "dois zero")