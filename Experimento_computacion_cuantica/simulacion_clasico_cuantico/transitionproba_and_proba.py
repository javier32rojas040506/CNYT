from MatrixVectorLib import *


def proba_particle(ket, posicion):
    norma_ket = (complexVectorNorma(ket))**2
    for i in range(len(ket)):
        norma_posicion = (modulo(ket[i])) ** 2
        print(i ,norma_posicion/norma_ket)
    norma_posicion = (modulo(ket[posicion])) ** 2
    return posicion, norma_posicion/norma_ket

def amplitud_transicion(ket_psi,ket_phi):
    """se parte del ket psi y se llega a phi"""
    ket_phi = conjugateMatriz(ket_phi)
    norma_ket_phi = complexVectorNorma(ket_phi)
    norma_ket_psi = complexVectorNorma(ket_psi)
    norma = norma_ket_phi*norma_ket_psi
    proba = [productopunto(ket_phi, ket_psi)]
    res = escVector((1/norma,0), proba)
    return res

#print(amplitud_transicion([(2,1), (-1,2), (0,1), (1,0), (3,-1), (2,0), (0,-2), (-2,1), (1,-3), (0,-1)], [(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]))
#print(proba_particle([(2,1), (-1,2), (0,1), (1,0), (3,-1), (2,0), (0,-2), (-2,1), (1,-3), (0,-1)], 7))
#print(amplitud_transicion([(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]))