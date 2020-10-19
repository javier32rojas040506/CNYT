import  numpy as np
from MatrixVectorLib import *


def proba_particle(ket, posicion):
    """"Determina la probabilidad de que la particula este en una posicion del ket dado """
    norma_ket = (complexVectorNorma(ket))**2
    for i in range(len(ket)):
        norma_posicion = (modulo(ket[i])) ** 2
        """para ver todas las probabilidades elimine el caracter #"""
        #print(i, norma_posicion/norma_ket)
    norma_posicion = (modulo(ket[posicion])) ** 2
    return posicion, norma_posicion/norma_ket

def amplitud_transicion(ket_psi,ket_phi):
    """se parte del ket psi y se llega a phi"""
    ket_phi = conjugateMatriz(ket_phi)
    norma_ket_phi = complexVectorNorma(ket_phi)
    norma_ket_psi = complexVectorNorma(ket_psi)
    norma = norma_ket_phi*norma_ket_psi
    proba = [productopunto(ket_phi, ket_psi)]
    res = escVector((1/norma, 0), proba)
    return res

def bra( ket  ):
    """Devuelve el bra de un ket dado"""
    return conjugateMatriz(ket)

def media(observable, ket):
    if esHermitania(observable):
        bra_ket = bra(ket)
        res1 = accion_Mat_Vector(observable, ket)
        res2 = productopunto(res1, bra_ket)
        return res2
    else:
        return "El observables no es hermitiano"

def varianza(observable, ket):
    if esHermitania(observable):
        bra_ket = bra(ket)
        Mu = media(observable, ket)
        identidad_Mu =  [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
        for i in range(len(observable)):
            for j in range(len(observable[i])):
                if i==j:
                    identidad_Mu[i][j] = inverse(Mu)
        identidad_Mu = sumMatrix(identidad_Mu, observable)
        observablealcudrado = producMatrizes(identidad_Mu, identidad_Mu)
        res1 = accion_Mat_Vector(observablealcudrado, ket)
        res2 = productopunto(res1, bra_ket)
        return res2
    else:
        return "El observables no es hermitiano"

def eigen_valuesvectors(observable):
    valores, vectores = np.linalg.eig(observable)
    lValores = []
    lVectores = []
    for i in range(len(valores)):
        lValores += [(valores[i].real, valores[i].imag)]
    for i in range(len(vectores)):
        vector = []
        for j in range(len(vectores[0])):
            vector += [(vectores[i][j].real, vectores[i][j].imag)]
        lVectores += [vector]
    return lValores, lVectores

def proba_vectores(ket, observable, posicion):
    vectores = eigen_valuesvectors(observable)[1]
    return amplitud_transicion(ket, vectores[posicion])

def dynamicSystem(Unitarymat,Xvetorestado, t_clicks):
    if unitaria(Unitarymat):
        for i in range(t_clicks):
            Xvetorestado = accion_Mat_Vector(Unitarymat, Xvetorestado)
        return Xvetorestado
    else:
        return "la matriz no es unitaria"


#1 Find all the possible states the system described in Exercise 4.2.2
#can transition into after a measurement has been carried out
#particle is spin up

# Ejercicio 4.3.1
def Exc431():
# Vector inicial :

    v1 = [(1, 0), (0, 0)]
    observable_x = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    vr = accion_Mat_Vector(observable_x, v1)
    valores_x, vectores_x = eigen_valuesvectors(observable_x)
    print("El resultado de la observacion es: ", vr)
    print("Los valores porpios del observable son: ", valores_x, "ademas sus vectores poropios son: ", vectores_x, " por tanto el sistema colapsa en un vector poropio")
# Excercise 4.3.2

def Exc432():
# Find all the possible states the system described in Exercise 4.2.2
#can transition into after a measurement has been carried out
    v1 = [[(1, 0)], [(0, 0)]]
    observable_x = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    valores_x, vectores_x = eigen_valuesvectors(observable_x)
    for i in range(len(vectores_x)):
        print(amplitud_transicion(v1,vectores_x[i]))

# Excercise 4.4.1
def Exc441():
# Verify that the next matrix are unitary, their preoduct is also unitary
    U1 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    U2 = [[((2**(1/2))/2, 0), ((2**(1/2))/2, 0)], [((2**(1/2))/2, 0), (-(2**(1/2))/2, 0)]]
    if unitaria(U1) and unitaria(U2):
        print(unitaria(producMatrizes(U1,U2)))

# Excercise 4.4.2
def Exc442():
#with example 3.3.2 change the unitary map and answer Determine the state of the system after three time steps.
# What is the chance of
# the quantum ball to be found at point 3?
    print(dynamicSystem([[(0, 0), (1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)],
                        [(1/(2**(1/2)), 0), (0, 0), (0, 0), (-1/(2**(1/2)), 0)],
                        [(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],
                        [(0, 0), (-1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)]],
                        [(1,0), (0,0), (0,0), (0,0)], 3))
    print(dynamicSystem([[(0, 0), (1 / (2 ** (1 / 2)), 0), (1 / (2 ** (1 / 2)), 0), (0, 0)],
                   [(0, 1 / (2 ** (1 / 2))), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],
                   [(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (0, 1 / (2 ** (1 / 2)))],
                   [(0, 0), (1 / (2 ** (1 / 2)), 0), (-1 / (2 ** (1 / 2)), 0), (0, 0)]],
                  [(1, 0), (0, 0), (0, 0), (0, 0)], 3))
