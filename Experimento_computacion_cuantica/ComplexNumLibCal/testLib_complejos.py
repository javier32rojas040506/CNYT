import unittest
from Libreria_Num_Complejos import *
from math import *


class TestLibComplejos(unittest.TestCase):
    n1, n2 = (5, -1), (1, -4)
    n3, n4 = (3, 7), (2, -3)
    n5, n6 = (1, 9), (-2, 1)
    n7, n8 = (5, 5), (5, 5)

    def test_complexsum(self):
        self.assertEqual(complexsum(self.n1, self.n2), (6, -5))
        self.assertEqual(complexsum(self.n3, self.n4), (5, 4))
        self.assertEqual(complexsum(self.n5, self.n6), (-1, 10))
        self.assertEqual(complexsum(self.n7, self.n8), (10, 10))

    def test_complexproduc(self):
        self.assertEqual(complexproduc(self.n1, self.n2), (1, -21))
        self.assertEqual(complexproduc(self.n3, self.n4), (27, 5))
        self.assertEqual(complexproduc(self.n5, self.n6), (-11, -17))
        self.assertEqual(complexproduc(self.n7, self.n8), (0, 50))

    def test_complexresta(self):
        self.assertEqual(complexresta(self.n1, self.n2), (4, 3))
        self.assertEqual(complexresta(self.n3, self.n4), (1, 10))
        self.assertEqual(complexresta(self.n5, self.n6), (3, 8))
        self.assertEqual(complexresta(self.n7, self.n8), (0, 0))

    def test_division(self):
        self.assertEqual(division(self.n1, self.n2), (9 / 17, 19 / 17))
        self.assertEqual(division(self.n3, self.n4), (-15 / 13, 23 / 13))
        self.assertEqual(division(self.n5, self.n6), (7 / 5, -19 / 5))
        self.assertEqual(division(self.n7, self.n8), (1, 0))

    def test_modulo(self):
        self.assertEqual(modulo(self.n1), 5.099)
        self.assertEqual(modulo(self.n3), 7.616)
        self.assertEqual(modulo(self.n5), 9.055)
        self.assertEqual(modulo(self.n7), 7.071)

    def test_conjugado(self):
        self.assertEqual(conjugado(self.n1), (5, 1))
        self.assertEqual(conjugado(self.n3), (3, -7))
        self.assertEqual(conjugado(self.n5), (1, -9))
        self.assertEqual(conjugado(self.n7), (5, -5))

    def test_polar(self):
        self.assertEqual(polar(self.n1), (5.099, round(math.radians(-11.310), 3)))
        self.assertEqual(polar(self.n3), (7.616, round(math.radians(66.801), 3)))
        self.assertEqual(polar(self.n5), (9.055, round(math.radians(83.660), 3)))
        self.assertEqual(polar(self.n7), (7.071, round(math.radians(45), 3)))

    def test_cartesianas(self):
        n9 = (4, pi/4)
        n10 = (3, pi/2)
        n11 = (-5, pi/6)
        self.assertEqual(cartesianas(n9), (2.828, 2.828))
        self.assertEqual(cartesianas(n10), (0, 3))
        self.assertEqual(cartesianas(n11), (-4.330, -2.5))

    def test_fase(self):
        self.assertEqual(fase(self.n1), round(math.radians(-11.310), 3))
        self.assertEqual(fase(self.n3), round(math.radians(66.801), 3))
        self.assertEqual(fase(self.n6), round(math.radians(-26.565) + pi, 3))
        self.assertEqual(fase(self.n7), round(math.radians(45), 3))


if __name__ == '__main__':
    unittest.main()

# Author Francisco Javier Rojas Muñoz
