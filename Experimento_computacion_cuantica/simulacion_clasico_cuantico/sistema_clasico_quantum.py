import matplotlib.pyplot as plot
import numpy as np
from MatrixVectorLib import *

def accion_Bool_Mat_Vector(Matriz, vector):
    row, column = len(Matriz), len(Matriz[0])
    longitud = len(vector)

    if column == longitud:
        respuesta = [False for c in range(row)]

        for i in range(row):
            variable_bool = True

            for j in range(column):
                variable_bool = Matriz[i][j] and vector[j]
                respuesta[i] = respuesta[i] or variable_bool

        return respuesta
    print("Las dimensiones de las matrices no permiten la multiplicacion")


def Boolean_clicks(booleanMatriz, Xvectbool, t_clicks):
    for c in range(t_clicks):
        Xvectbool = accion_Bool_Mat_Vector(booleanMatriz, Xvectbool)

    return Xvectbool


def proba_clicks(Matriz, Xvetorestado, t_clicks):
    for i in range(t_clicks):
        Xvetorestado = accion_Mat_Vector(Matriz, Xvetorestado)
    return Xvetorestado


def Quantum_clicks(Matriz, Xvetorestado, t_clicks):
    ansProba=[]
    for i in range(t_clicks):
        Xvetorestado = accion_Mat_Vector(Matriz, Xvetorestado)
    for fila in Xvetorestado:
        fila = (complexVectorNorma(fila))**2
        ansProba = ansProba + [fila]
    return ansProba


def grafico_probabilidades(vector):
    ejes = len(vector)
    x = np.array([x for x in range(ejes)])
    y = np.array([round(vector[x]*100, 3) for x in range(ejes)])
    plot.bar(x, y, color="blue", align="center")
    plot.title("Vector Probabilities")
    plot.savefig("Vector_Probabilities.png")
    plot.show()
