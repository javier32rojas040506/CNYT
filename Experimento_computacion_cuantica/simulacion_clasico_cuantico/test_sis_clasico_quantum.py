import unittest
from sistema_clasico_quantum import *

class sistema_clasico_quantum(unittest.TestCase):

    def testBoolena_clicks(self):
        booleanMatriz = \
        [[False, False, False, False, False, False], [False, False, False, True, False, False],
        [False, True, False, False, False, True], [False, False, True, False, False, False],
        [False, False, False, False, True, False], [True, False, False, False, False, False]]

        Xvectbool= [False, False, False, False, False, True]

        self.assertEqual(Boolean_clicks(booleanMatriz, Xvectbool, 1),
                         [False, False, True, False, False, False])

        self.assertEqual(Boolean_clicks(booleanMatriz, Xvectbool, 2),
                         [False, False, False, True, False, False])

        self.assertEqual(Boolean_clicks(booleanMatriz, Xvectbool, 3),
                         [False, True, False, False, False, False])

        self.assertEqual(Boolean_clicks(booleanMatriz, Xvectbool, 2019),
                         [False, True, False, False, False, False])

    def testproba_clicks(self):
        Matriz = [[(0, 0), (1/6, 0), (5/6, 0)], [(1/3, 0), (1/2, 0), (1/6, 0)], [(2/3, 0), (1/3, 0), (0, 0)]]
        Xvectorestado = [(1/5, 0), (7/10, 0), (1/10, 0)]

        self.assertEqual(proba_clicks(Matriz, Xvectorestado, 1),
        [[(0.2, 0.0)], [(0.4333333333333333, 0.0)], [(0.36666666666666664, 0.0)]])

        self.assertEqual(proba_clicks(Matriz, Xvectorestado, 2),
        [[(0.37777777777777777, 0.0)], [(0.34444444444444444, 0.0)], [(0.2777777777777778, 0.0)]])

        self.assertEqual(proba_clicks(Matriz, Xvectorestado, 3),
        [[(0.2888888888888889, 0.0)], [(0.34444444444444444, 0.0)], [(0.36666666666666664, 0.0)]])

        self.assertEqual(proba_clicks(Matriz, Xvectorestado, 4),
        [[(0.36296296296296293, 0.0)], [(0.3296296296296296, 0.0)], [(0.3074074074074074, 0.0)]])

    def testQuantum_clisks(self):
        Matriz = [[(1/(2**0.5),0), (0, 1/(2**0.5))],[(1/(2**0.5), 0), (0, -1/(2**0.5))]]
        Xvectorestado = [(1, 0), (0, 0)]

        self.assertEqual(Quantum_clicks(Matriz, Xvectorestado, 1), [0.49984899999999993, 0.49984899999999993])

        self.assertEqual(Quantum_clicks(Matriz, Xvectorestado, 3), [1.0, 0.0])
        c1 = (-1 / (6 * 0.5), 1 / (6 ** 0.5))
        c2 = (-1 / (6 ** 0.5), -1 / (6 ** 0.5))
        c3 = (1 / (6 ** 0.5), -1 / (6 ** 0.5))

        Matriz = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                 [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                 [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                 [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                 [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
                 [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
                 [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
                 [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]]
        Xvectorestado = [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]

        self.assertEqual(Quantum_clicks(Matriz, Xvectorestado, 1), [0.0, 0.25, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0])

        self.assertEqual(Quantum_clicks(Matriz, Xvectorestado, 10), [0.0, 0.0, 0.0, 0.07022500000000001, 0.0841, 0.001024, 0.0841, 0.0841])

if __name__ == '__main__':
    unittest.main()

# Author Francisco Javier Rojas Muñoz
