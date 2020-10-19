# Libreria_Num_Complejos

_This program can do the next operations with complex numbers_
- add 
- Multiplications
- subtraction
- Division
- Module
- Conjugate
- conversion into polar and cartesian representation
- the phase of a complex number

# MatrixVectorLib
- this program can do the next operations with matrix and  complex vectors
- Adición de vectores complejos.
- Inverso (aditivo) de un vector complejo.
- Multiplicación de un escalar por un vector complejo.
- Adición de matrices complejas.
- Inversa (aditiva) de una matriz compleja.
- Multiplicación de un escalar por una matriz compleja.
- Transpuesta de una matriz/vector
- Conjugada de una matriz/vector
- Adjunta (daga) de una matriz/vector
- Producto de dos matrices (de tamaños compatibles)
- Función para calcular la "acción" de una matriz sobre un vector.
- Producto interno de dos vectores
- Norma de un vector
- Distancia entre dos vectores
- Revisar si una matriz es unitaria
- Revisar si una matriz es Hermitiana
- Producto tensor de dos matrices/vectores

# Simulacion Sistemas Clasicos y Cuanticos
-Experimentos de sistemas clasicos con canicas rpresentados mediante coeficientes booleanos
-Experimentos de múltiples rendijas sistema clásico-probabilístico, con más de dos rendijas.
-Experimento de las múltiples rendijas sistema cuántico.
-Función que crea grafica con un diagrama de barras que muestra las probabilidades de un vector y sus estados. La imagen se muestra al final y seguarga en formato png.

# Teoria cuantica basica
- probabilidad de en encontrar una particula en un ket
- amplitud de transicion de una particula de un keta otro
- media o valor esperado despues de una medicion
- varianza determina la varianza de una particula con un ket y un observable dado
- calcula la dinamica de un sistema
# EXERCISES


Ejercicio 4.3.1

1 Find all the possible states the system described in Exercise 4.2.2
can transition into after a measurement has been carried out
particle is spin up.

with the next function we solve the exercise Exc431():
using our functions for eigen vectors and values, we take the observable and ket
```
 v1 = [(1, 0), (0, 0)]
    observable_x = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
```
then we have
```

El resultado de la observacion es:  [[(0, 0)], [(1, 0)]]
Los valores porpios del observable son:  [(array([0., 0.]), array([0., 0.])), (array([1., 0.]), array([0., 0.]))] ademas sus vectores poropios son:  [[(array([0.00000000e+000, 2.00416836e-292]), array([0., 0.])), (array([ 1., -1.]), array([0., 0.]))], [(array([1., 0.]), array([0., 0.])), (array([0., 1.]), array([0., 0.]))]]  por tanto el sistema colapsa en un vector poropio
El resultado de la observacion es:  [[(0, 0)], [(1, 0)]]
Los valores porpios del observable son:  [(array([0., 0.]), array([0., 0.])), (array([1., 0.]), array([0., 0.]))] ademas sus vectores poropios son:  [[(array([0.00000000e+000, 2.00416836e-292]), array([0., 0.])), (array([ 1., -1.]), array([0., 0.]))], [(array([1., 0.]), array([0., 0.])), (array([0., 1.]), array([0., 0.]))]]  por tanto el sistema colapsa en un vector poropio

```
Excercise 4.4.1
with the next function we solve the exercise Exc441():
1.Verify that the next matrix are unitary, their product is also unitary
we take  the matriz and next to prove that the matrix are unitary with the function unitaria
then we prove the same with the product of the matrix
```
    U1 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    U2 = [[((2**(1/2))/2, 0), ((2**(1/2))/2, 0)], [((2**(1/2))/2, 0), (-(2**(1/2))/2, 0)]]
    if unitaria(U1) and unitaria(U2):
        return unitaria(producMatrizes(U1,U2))
```
then we have
```
True
```
Excercise 4.4.2
1.with example 3.3.2 change the unitary map and answer Determine the state of the system after three time steps.
 What is the chance of
 the quantum ball to be found at point 3?
 
 with the next function we solve the exercise Exc4412():
 let the unitary matrix , the vector state and the numbers of clicks, we have
 ```
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
```
then we have
```
[[(0.0, 0.0)], [(0.7071067811865474, 0.0)], [(0.7071067811865474, 0.0)], [(0.0, 0.0)]]
[[(0.0, 0.0)], [(-0.7071067811865474, 0.7071067811865474)], [(0.0, 0.0)], [(0.0, 0.0)]]
```
Ejercicio 4.5.2
the generalize sytem is
|B> = |X0>⊗|Y0>+...+|Xn>⊗|Yn>

Ejercicio 4.5.3
the sistem can't separete becouse there are interlaced an the sistenm of the next equations dont have solution
c0b0=1, c1b0=0, c0b1=0, c1b1=1

##  Starting 🚀

_We need to know that the complex  number have one part real and other one imaginary, so we have_
```
5 + 7i
```
_to use the library we are going to use tuple with this structure_ 
```
(real, imagimary) ----> (5, 7) ----> 5 + 7i
```
_For matrix an vectors structure are_ 
```
[[complex],[complex],[complex],[complex]]
```
_you can use vertical horizontal vectors_ 
```
[complex, complex, complex] or [[complex][complex][complex]]
```
_For simulations and experiments_ 


_simulation of classic system with one marble and boolean matrix_ 
```
booleanMatriz = [[bool], [bool], [bool], ....] // it represents the system

Xvectbool = [bool, ...] // it represents the state of system

```

_simulation of classic system with multiplies slits_ 
```
booleanMatriz = [[complex, complex, ...], ....] // it represents the system

Xvectbool = [complex, complex, ...] // it represents the state of system

```

_simulation of quantum system with multiplies slits_ 
```
booleanMatriz = [[complex, complex, ...], ....] // it represents the system

Xvectbool = [complex, complex, ...] // it represents the state of system

in this case we have a vector of probabilities 

Probabilities = [float, ...]

```
_graph of probabilities_ 
```
we have a vector of probabilities 

Probabilities = [float, ...]

```

### Pre-requirements 📋

*Python 3 or followed versions


### Installation 🔧

_You can download python last version in this link https://www.python.org/downloads/_

## Running Tests ⚙️

_1. Download the repository use:_
```
git clone https://github.com/javier32rojas040506/CNYT.git
```
_then you can use the library imported them_
```
from Libreria_Num_Complejos import *
```
### AutoTests end-to-end 🔩

_the proves are very important to know how efficient and correct are ours functions, therefore we use unittest library from python with parameter assertEqual to compare the answers_

```
class TestLibComplejos(unittest.TestCase):
    n1, n2 = (5, -1), (1, -4)
    def test_complexsum(self):
        self.assertEqual(complexsum(self.n1, self.n2), (6, -5))

class TestLibComplex(unittest.TestCase):
    def testInverseMatrix(self):
        self.assertEqual(inverseMatrix([[a], [b], [c]]), [[(-1, -3)], [(-2, -4)], [(-6, -5)]])
        self.assertEqual(inverseMatrix([[a, a, c], [c, b, a], [d, c, b]]), [[(-1, -3), (-1, -3), (-6, -5)], [(-6, -5), (-2, -4), (-1, -3)],[(-4, -9), (-6, -5), (-2, -4)]])
        self.assertEqual(inverseMatrix([[e, i], [f, j]]), [[(-1, -2), (-3, -2)], [(-2, -2), (-3, -3)]])
        self.assertEqual(inverseMatrix([[e, i], [f, i]]), [[(-1, -2), (-3, -2)], [(-2, -2), (-3, -2)]])
```
###  How to Running Unittest ⌨️

_when you have the repository only follow the next address_

```
cd 1tercio/testLib_complejos
cd 1tercio/testMatrixVectorLib
```


## Built With 🛠️

_built with python 3.8_

## Author ✒️

* **Francisco Javier Rojas Muñoz** - *test and library* 
 
## referenced

*the model that i took for did the README is from:
[Villanuevand](https://github.com/Villanuevand)

---
