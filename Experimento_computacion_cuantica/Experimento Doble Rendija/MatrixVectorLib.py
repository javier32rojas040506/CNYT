from Libreria_Num_Complejos import *


#verificar la longitud de un vestor

def lenght(vector, vetor1):
    if len(vector) == len(vetor1):
        return True
    else:
        return False

#suma de vectores

def sumVector(vector, vector1):
    """funcion que suma vectores (list, list)-> list"""
    if lenght(vector, vector1) == True:
        vectoR = []
        for dimension in range(len(vector)):
            vectoR = vectoR + [complexsum(vector[dimension], vector1[dimension])]
    return vectoR

#inversa de un vector

def inverseVector(vector):
    """funcion que saca el inverso de un vector (list, list)-> list"""
    vectoR = []
    for dimension in range(len(vector)):
        vectoR = vectoR + [inverse(vector[dimension])]
    return vectoR

#escalar por un vector

def escVector(a, vector):
    """ determina el el producto esclar de un vector"""
    esTupla = isinstance(vector[0], tuple)
    if esTupla == True:
        for dimension in range(len(vector)):
            vector[dimension] = complexproduc(vector[dimension], a)
    else:
        for dimension in range(len(vector)):
            for j in range(len(vector[0])):
                vector[dimension][j] = complexproduc(vector[dimension][j], a)
    return vector

#suma de dos matrices

def sumMatrix(mat, mat1):
    """"funcion que suma matrices (list2d, list2d)->list2d"""
    if lenght(mat, mat1) and lenght(mat[0], mat1[0]) == True:
        for row in range(len(mat)):
            mat1[row] = sumVector(mat[row], mat1[row])
        return mat1
    return "dimensiones diferentes"

#inversa de una matriz

def inverseMatrix(mat):
    """funcion que saca la inversa de una matriz (list2d)->list2d"""
    for row in range(len(mat)):
        for column in range(len(mat[0])):
            mat[row][column] = inverse(mat[row][column])
    return mat

#multiplicacion escalar matriz

def escMatrix(a, mat):
    """funcion que determina el producto escalar por una matriz (list, int)->list2d"""
    for row in range(len(mat)):
        mat[row] = escVector(a, mat[row])
    return mat

#matriz transpuesta

def transMatriz(mat):
    """funncion  que calcula la transpuesta (list2d)->list2d"""
    m = len(mat)
    n = len(mat[0])
    trans = [[0 for j in range(m)] for i in range(n)]
    for row in range(m):
        for column in range(n):
            trans[column][row] = mat[row][column]
    return trans

#conjugada de una matriz

def conjugateMatriz(mat):
    """funcion que calcula la conjugada de una matriz (list2d)->list2d"""
    if isinstance(mat[0], tuple) ==  True:
        mat = cambio_vector_horizontal(mat)
    conju = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    for row in range(len(mat)):
        for column in range(len(mat[0])):
            conju[row][column] = conjugado(mat[row][column])
    return conju

#adjunta de una matriz

def adjuntaMatVec(mat):
    """matriz que determina la adjunta de una matriz o vector (list2d)->list2d"""
    mat1 = conjugateMatriz(mat)
    mat1 = transMatriz(mat1)
    return mat1

# producto matrizes

def producMatrizes(mat, mat1):
    """funcion que hace la multiplicacion entre matrices (list2d,list2d)->list2d"""
    if len(mat[0]) == len(mat1):
        matR = [[(0,0) for j in range(len(mat1[0]))]for i in range(len(mat))]
        for row in range(len(mat)):
            for column in range(len(mat1[0])):
                for i in range(len(mat[0])):
                    matR[row][column] = complexsum(matR[row][column], complexproduc(mat[row][i], mat1[i][column]))
        return matR
    else:
        return "las matricces no se pueden multiplicar por sus dimensiones"

# cambia la horientacion del vector

def cambio_vector_horizontal(vector):
    """funcion que cambia el sentido del vetor (list)->list"""
    vector1 = [[(0,0) for j in range(1)] for i in range(len(vector))]
    for i in range(len(vector)):
        vector1[i][0] =tuple(vector[i])
    return  vector1

# ACCION DE UNA MATRIZ SOBRE VECTOR

def accion_Mat_Vector(mat, vector):
    """funcion que hace la accion de una matriz sobre un vector (list2d,list)->list2d"""
    if isinstance(vector[0], tuple) ==  True:
        vector = cambio_vector_horizontal(vector)
    matR = producMatrizes(mat, vector)
    return matR

#PRODUCTO INTERNO DOS VECTORES

def productopunto(vector, vector1):
    """funcion que determina el producto punto entre vectores (list,list)->int"""
    total = (0, 0)
    if isinstance(vector[0], tuple) and isinstance(vector1[0], tuple) ==  True:
        vector = cambio_vector_horizontal(vector)
        vector1 = cambio_vector_horizontal(vector1)
    elif isinstance(vector[0], tuple)==True:
        vector = cambio_vector_horizontal(vector)
    elif isinstance(vector1[0], tuple) == True:
        vector1 = cambio_vector_horizontal(vector1)
    for i in range(len(vector)):
        for j in range(len(vector1[0])):
            total = complexsum(total, complexproduc(vector1[i][j], vector[i][j]))
    return total


#NORMA DE UN VECTOR

def complexVectorNorma(vector):
    """determina la norma de un vector (list)-> int"""
    suma = 0
    if isinstance(vector[0], tuple) == True:
        vector = cambio_vector_horizontal(vector)
    for i in range(len(vector)):
        for j in range(len(vector[0])):
            suma = suma + round(modulo(vector[i][j])**2, 3)
    suma = (round(math.sqrt(suma), 3))
    return suma

#Distancia entre dos vectores

def distanciaVectores(vector, vector1):
    """determina la distancia entre dos vectore (list)->int"""
    if isinstance(vector[0], tuple) and isinstance(vector1[0], tuple) ==  True:
        vector = cambio_vector_horizontal(vector)
        vector1 = cambio_vector_horizontal(vector1)
    for fila in range(len(vector)):
        for columna in range(len(vector[0])):
            vector[fila][columna] = complexresta(vector[fila][columna], vector1[fila][columna])
    distancia = complexVectorNorma(vector)
    return distancia

# Revisar matriz Unitaria

def  unitaria(mat):
    """revisa si un matris es unitaria (list2d)-> boolean"""
    mat1 = adjuntaMatVec(mat)
    Munitaria = [[(0, 0) for j in range(len(mat[0]))] for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j:
                Munitaria[i][j] = (1, 0)
    mat2 = producMatrizes(mat, mat1)
    mat2= escMatrix((1/mat2[0][0][0]), mat2)
    
    if mat2 == Munitaria:
        return True
    else:
        return False
    
# Revisar matriz Hermitania

def esHermitania(mat):
    """determina si una matriz es hermitania (list2d)-> boolean"""
    mat1 = adjuntaMatVec(mat)
    if mat1 == mat:
        return True
    else:
        return False

# producto tensor

def tensorProduct(mat, mat1):
    """determina el prodcuto tensor entre dos marices (list2d,list2d)-> boolean"""
    mat2 = [[(0, 0) for j in range(len(mat[0]))] for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat1)):
            a = mat[i][j]
            mat2[i][j] = escMatrix(a, mat1)
    return mat2