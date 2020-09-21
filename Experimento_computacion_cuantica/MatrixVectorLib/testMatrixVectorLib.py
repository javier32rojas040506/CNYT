import unittest
from MatrixVectorLib import *

# complex numbers
a = (1, 3)
b = (2, 4)
c = (6, 5)
d = (4, 9)
e = (1, 2)
f = (2, 2)
g = (1, 1)
h = (5, 0)
i = (3, 2)
j = (3, 3)
k = (4, 3)
n = (6, 4)
o = (12, -7)
p = (5, 5)
class TestLibComplex(unittest.TestCase):
    def testSumVector(self):
        self.assertEqual(sumVector([a, b], [a, b]), [(2, 6), (4, 8)])
        self.assertEqual(sumVector([a, c], [c, b]), [(7, 8), (8, 9)])
        self.assertEqual(sumVector([e, f], [e, f]), [(2, 4), (4, 4)])
        self.assertEqual(sumVector([f, e], [e, f]), [(3, 4), (3, 4)])

    def testInverseVector(self):
        self.assertEqual(inverseVector([a, c]), [(-1, -3), (-6, -5)])
        self.assertEqual(inverseVector([b, a]), [(-2, -4), (-1, -3)])
        self.assertEqual(inverseVector([e, f]), [(-1, -2), (-2, -2)])
        self.assertEqual(inverseVector([f, e]), [(-2, -2), (-1, -2)])

    def testEscVector(self):
        self.assertEqual(escVector(b, [a, b]), [(-10, 10), (-12, 16)])
        self.assertEqual(escVector(c, [b, c]), [(-8, 34), (11, 60)])
        self.assertEqual(escVector(h, [g, g, f]), [(5, 5), (5, 5), (10, 10)])
        self.assertEqual(escVector(h, [[g], [g], [f]]), [[(5, 5)], [(5, 5)], [(10, 10)]])

    def testSumMatrix(self):
        self.assertEqual(sumMatrix([[a, a], [b, b]], [[b, a], [a, b]]), [[(3, 7), (2, 6)], [(3, 7), (4, 8)]])
        self.assertEqual(sumMatrix([[c, a], [a, b]], [[b, c], [b, b]]), [[(8, 9), (7, 8)], [(3, 7), (4, 8)]])
        self.assertEqual(sumMatrix([[e, i], [f, j]], [[e, i], [f, j]]), [[(2, 4), (6, 4)], [(4, 4), (6, 6)]])
        self.assertEqual(sumMatrix([[e, i], [f, j]], [[e, i], [g, j]]), [[(2, 4), (6, 4)], [(3, 3), (6, 6)]])

    def testInverseMatrix(self):
        self.assertEqual(inverseMatrix([[a], [b], [c]]), [[(-1, -3)], [(-2, -4)], [(-6, -5)]])
        self.assertEqual(inverseMatrix([[a, a, c], [c, b, a], [d, c, b]]), [[(-1, -3), (-1, -3), (-6, -5)], [(-6, -5), (-2, -4), (-1, -3)],[(-4, -9), (-6, -5), (-2, -4)]])
        self.assertEqual(inverseMatrix([[e, i], [f, j]]), [[(-1, -2), (-3, -2)], [(-2, -2), (-3, -3)]])
        self.assertEqual(inverseMatrix([[e, i], [f, i]]), [[(-1, -2), (-3, -2)], [(-2, -2), (-3, -2)]])


    def testEscMatrix(self):
        self.assertEqual(escMatrix(d, [[c, a], [a, d]]), [[(-21, 74), (-23, 21)], [(-23, 21), (-65, 72)]])
        self.assertEqual(escMatrix(c, [[a, a], [b, b]]), [[(-9, 23), (-9, 23)], [(-8, 34), (-8, 34)]])
        self.assertEqual(escMatrix(h, [[e, i], [f, j]]), [[(5, 10), (15, 10)], [(10, 10), (15, 15)]])
        self.assertEqual(escMatrix(h, [[e, i], [f, a]]), [[(5, 10), (15, 10)], [(10, 10), (5, 15)]])

    def testTransMatriz(self):
        self.assertEqual(transMatriz([[b, a, a], [a, b, a]]), [[(2, 4), (1, 3)], [(1, 3), (2, 4)], [(1, 3), (1, 3)]])
        self.assertEqual(transMatriz([[a, b, c], [c, b, a]]), [[(1, 3), (6, 5)], [(2, 4), (2, 4)], [(6, 5), (1, 3)]])
        self.assertEqual(transMatriz([[e, i], [f, j]]), [[(1, 2), (2, 2)], [(3, 2), (3, 3)]])
        self.assertEqual(transMatriz([[e, i], [f, g]]), [[(1, 2), (2, 2)], [(3, 2), (1, 1)]])

    def testConjugateMatriz(self):
        self.assertEqual(conjugateMatriz([[b, a, c], [c, b, d]]), [[(2, -4), (1, -3), (6, -5)], [(6, -5), (2, -4), (4, -9)]])
        self.assertEqual(conjugateMatriz([[a, b, c], [c, b, a]]), [[(1, -3), (2, -4), (6, -5)], [(6, -5), (2, -4), (1, -3)]])
        self.assertEqual(conjugateMatriz([[e, i], [f, j]]), [[(1, -2), (3, -2)], [(2, -2), (3, -3)]])
        self.assertEqual(conjugateMatriz([[e, i], [f, g]]), [[(1, -2), (3, -2)], [(2, -2), (1, -1)]])

    def testAdjuntaMatVec(self):
        self.assertEqual(adjuntaMatVec([[b, a, a], [a, b, a]]), [[(2, -4), (1, -3)], [(1, -3), (2, -4)], [(1, -3), (1, -3)]])
        self.assertEqual(adjuntaMatVec([[a, b, c], [c, b, a]]), [[(1, -3), (6, -5)], [(2, -4), (2, -4)], [(6, -5), (1, -3)]])
        self.assertEqual(adjuntaMatVec([[e, i], [f, j]]), [[(1, -2), (2, -2)], [(3, -2), (3, -3)]])
        self.assertEqual(adjuntaMatVec([[e, i], [f, g]]), [[(1, -2), (2, -2)], [(3, -2), (1, -1)]])

    def testproducMatrizes(self):
        self.assertEqual(producMatrizes([[a, a], [b, b]], [[b, a], [a, b]]), [[(-18, 16), (-18, 16)], [(-22, 26), (-22, 26)]])
        self.assertEqual(producMatrizes([[a, a, b], [b, b, a]], [[b, a], [a, b], [b, b]]), [[(-30, 32), (-30, 32)], [(-32, 36), (-32, 36)]])
        self.assertEqual(producMatrizes([[e, i], [f, j]], [[e, i], [f, j]]), [[(-1, 14), (2, 23)], [(-2, 18), (2, 28)]])
        self.assertEqual(producMatrizes([[e, i, i], [f, j, i]], [[e, i], [f, j]]), "las matricces no se pueden multiplicar por sus dimensiones")

    def testaccion_Mat_Vector(self):
        self.assertEqual(accion_Mat_Vector([[e, i], [f, j]], [[e], [j]]), [[(0, 19)], [(-2, 24)]])
        self.assertEqual(accion_Mat_Vector([[e, i], [f, j]], [e, j]), [[(0, 19)], [(-2, 24)]])
        self.assertEqual(accion_Mat_Vector([[a, i], [f, j]], [e, j]), [[(-2, 20)], [(-2, 24)]])
        self.assertEqual(accion_Mat_Vector([[e, i], [e, j]], [e, j]), [[(0, 19)], [(-3, 22)]])

    def testproductopunto(self):
        self.assertEqual(productopunto([[k], [n], [o]], [[k], [n], [o]]), (122, -96))
        self.assertEqual(productopunto([k, n, o], [k, n, o]), (122, -96))
        self.assertEqual(productopunto([k, b, o], [k, n, o]), (98, -112))
        self.assertEqual(productopunto([a, n, o], [k, n, o]), (110, -105))

    def testcomplexVectorNorma(self):
        self.assertEqual(complexVectorNorma([[k], [n], [o]]), 16.431)
        self.assertEqual(complexVectorNorma([k, n, o]), 16.431)
        self.assertEqual(complexVectorNorma([k, b, o]), 15.427)
        self.assertEqual(complexVectorNorma([a, n, o]), 15.968)
    def testdistanciaVectores(self):
        self.assertEqual(distanciaVectores([[k], [p], [f]], [[g], [f], [j]]), 5.745)
        self.assertEqual(distanciaVectores([k, p, f], [g, f, j]), 5.745)
        self.assertEqual(distanciaVectores([g, p, f], [g, f, j]), 4.472)
        self.assertEqual(distanciaVectores([g, p, f], [g, p, j]), 1.414)

    def testesHermitania(self):
        a = (7, 0)
        b = (6, 5)
        c = (6, -5)
        d = (-3, 0)
        e, f = (1, 0), (0, 0)
        g = (5, 0)
        h = (3, 7)
        r = (3, -7)
        s = (2, 0)
        self.assertEqual(esHermitania([[a, b], [c, d]]), True)
        self.assertEqual(esHermitania([[e, f], [f, e]]), True)
        self.assertEqual(esHermitania([[g, h], [r, s]]), True)
        self.assertEqual(esHermitania([[i, k], [j, p]]), False)

    def testTensorProduct(self):
        def test_tensor(self):
            respuesta = tensorProduct(
                [[(3, 2), (5, -1), (0, 2)], [(0, 0), (12, 0), (6, -3)], [(2, 0), (4, 4), (9, 3)]],
                [[(1, 0), (3, 4), (5, -7)], [(10, 2), (6, 0), (2, 5)], [(0, 0), (1, 0), (2, 9)]])
            self.assertEqual(respuesta, [
                [[[(3, 2), (1, 18), (29, -11)], [(26, 26), (18, 12), (-4, 19)], [(0, 0), (3, 2), (-12, 31)]],
                 [[(5, -1), (19, 17), (18, -40)], [(52, 0), (30, -6), (15, 23)], [(0, 0), (5, -1), (19, 43)]],
                 [[(0, 2), (-8, 6), (14, 10)], [(-4, 20), (0, 12), (-10, 4)], [(0, 0), (0, 2), (-18, 4)]]],
                [[[(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]],
                 [[(12, 0), (36, 48), (60, -84)], [(120, 24), (72, 0), (24, 60)], [(0, 0), (12, 0), (24, 108)]],
                 [[(6, -3), (30, 15), (9, -57)], [(66, -18), (36, -18), (27, 24)], [(0, 0), (6, -3), (39, 48)]]],
                [[[(2, 0), (6, 8), (10, -14)], [(20, 4), (12, 0), (4, 10)], [(0, 0), (2, 0), (4, 18)]],
                 [[(4, 4), (-4, 28), (48, -8)], [(32, 48), (24, 24), (-12, 28)], [(0, 0), (4, 4), (-28, 44)]],
                 [[(9, 3), (15, 45), (66, -48)], [(84, 48), (54, 18), (3, 51)], [(0, 0), (9, 3), (-9, 87)]]]]
                             )
if __name__ == '__main__':
    unittest.main()

# Author Francisco Javier Rojas Muñoz
