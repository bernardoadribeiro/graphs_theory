""" Unit tests for hypercube module
"""

import unittest

from hypercube import Hypercube


class TestHypercubeGenerator(unittest.TestCase):
    def test_3hypercube_generation(self):
        V1, E1 = Hypercube().generate(3)

        V2 = ['000', '001', '010', '011', '100', '101', '110', '111']
        E2 = set({('000', '010'), ('100', '101'), ('000', '100'), ('001', '101'), ('000', '001'),
                  ('010', '011'), ('011', '111'), ('101', '111'), ('001', '011'), ('110', '111'),
                  ('010', '110'), ('100', '110')})

        self.assertEqual(V1, V2, "Os conjuntos V1 e V2 não são iguais.")
        self.assertEqual(E1, E2, "Os conjuntos E1 e E2 não são iguais.")

    def test_2hypercube_generation(self):
        V1, E1 = Hypercube().generate(2)
        V2 = ['00', '01', '10', '11']
        E2 = set({('00', '10'), ('00', '01'), ('01', '11'), ('10', '11')})

        self.assertEqual(V1, V2, "Os conjuntos V1 e V2 não são iguais.")
        self.assertEqual(E1, E2, "Os conjuntos E1 e E2 não são iguais.")


if __name__ == '__main__':
    unittest.main()
