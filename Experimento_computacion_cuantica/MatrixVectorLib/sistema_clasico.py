from MatrixVectorLib import *
c1 = (-1 / (6 * 0.5), 1 / (6 ** 0.5))
c2 = (-1 / (6 ** 0.5), -1 / (6 ** 0.5))
c3 = (1 / (6 ** 0.5), -1 / (6 ** 0.5))

def clicks(M, X, t):
    for i in range(t):
        X = accion_Mat_Vector(M, X)
    return X

#print(clicks([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]], [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]], 3))
print(clicks([[(1/(2**0.5),0), (1/(2**0.5),0), (0,0) ],[(0,-1/(2**0.5)),(0,1/(2**0.5)), (0,0)],[(0,0), (0,0), (0,-1)]], [(1/(3)**0.5,0),(0,2/(15)**0.5),((2/5)**0.5,0)], 4))