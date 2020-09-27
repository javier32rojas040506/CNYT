import math


def complexsum(c1, c2):
    """function that add complex numbers like tuples
    (tuple,tuple)->tuple"""
    n1 = c1[0] + c2[0]
    n2 = c1[1] + c2[1]
    res = (n1, n2)
    return res


def complexproduc(c1, c2):
    """function that multiply complex numbers like tuples
    (tuple,tuple)->tuple"""
    n1 = c1[0] * c2[0] - c1[1] * c2[1]
    n2 = c1[0] * c2[1] + c1[1] * c2[0]
    res = (n1, n2)
    return res


def complexresta(c1, c2):
    """function that subtraction complex numbers like tuples
    (tuple,tuple)->tuple"""
    n1 = c1[0] - c2[0]
    n2 = c1[1] - c2[1]
    res = (n1, n2)
    return res


def division(c1, c2):
    """function that divide complex numbers like tuples
    (tuple,tuple)->tuple"""
    deno = c2[0]**2 + c2[1]**2
    n1 = c1[0]*c2[0] + c1[1]*c2[1]
    n2 = c2[0]*c1[1] - c1[0]*c2[1]
    res = (n1/deno, n2/deno)
    return res


def modulo(c):
    """function that gets the module from complex numbers like tuples
    (tuple,tuple)->tuple"""
    modul = round(math.sqrt(c[0]**2+c[1]**2), 3)
    return modul


def conjugado(c):
    """function that gets conjugate number from a complex numbers like tuples
    (tuple,tuple)->tuple"""
    n2 = (c[0], c[1]*-1)
    return n2
def inverse(c):
    """function that gets negative number from a complex numbers like tuples
    (tuple,tuple)->tuple"""
    n2 = (c[0]*-1, c[1]*-1)
    return n2

def polar(c):
    """function that gets the polar representation  from a complex numbers like tuples
    (tuple,tuple)->tuple"""
    norma = round(math.sqrt(c[0]**2+c[1]**2), 3)
    angulo = round(math.atan2(c[1], c[0]), 3)
    return norma, angulo


def cartesianas(c):
    """function that gets the cartesian representation from a complex numbers like tuples
    (tuple,tuple)->tuple"""
    a = round(c[0] * math.cos(c[1]), 3)
    b = round(c[0] * math.sin(c[1]), 3)
    return a, b


def fase(c):
    """function that gets the phase from complex numbers like tuples
    (tuple,tuple)->tuple"""
    angulo = round(math.atan2(c[1], c[0]), 3)
    return angulo

# Author Francisco Javier Rojas Muñoz
