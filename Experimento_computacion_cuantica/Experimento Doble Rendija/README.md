# Experimento Doble Rendija
El experimento de doble rendija, fue realizado en 1801 por Thomas Young, en un intento de discernir
la naturaleza de la luz, esto fundaría lo que hoy conocemos como los fundamentos de la mecánica
cuántica, con los factores fundamentales como superposición, interferencia, entrelazamiento que
explicaremos a lo largo del experimento

## Objetivo
El objetivo de este experimento estudiar y entender el comportamiento del universo cuántico entendiendo sus fundamentos 
mas básicos

## Explicación 

En el experimento se uso un láser que arroja un haz de luz sobre una placa de papel aluminio. Si esta tiene una sola
abertura o rendija entonces tendremos la proyección de un solo punto la luz pasa por una sola rendija, esto representa 
un sistema clásico deterministico, es decir que podemos observar y predecir un patrón sobre una pared cuando usamos el
láser, tal como se presenta en la siguiente imagen teórica resultado

![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/resultado1.PNG)
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/punto.jpg)

Si cambiamos un poco del sistema utilizando dos rendijas en teoría si nos ceñimos a los resultados 
anteriores pudimos predecir que se presentará el mismo patrón solo que en dos regiones por que la mitad de 
la dispersión total se trasladará a la otra rendija, sin embargo el resultado es totalmente diferente 
pues se da un patrón en cual las probabilidades no encajan para explicarlo tendremos que cambiar de un sistemas clásico
a un sistemas cuántico. En la mecánica cuántica se puede predecir este patrón con la función de onda
de Erwin Schrödinger que describe un campo en todos los puntos del espacio con números complejos, que posteriormente
Niels Bohr descubrió que la norma al cuadrado de esos puntos obtenía otro campo capaz de predecir probabilisticamente 
el mundo cuántico.

Ahora que sabemos predecir el patrón, podemos explicar mejor que pasa con variaciones del experimento para entender 
mejor los resultados anteriores un ejemplo es lo que pasa si de amplia o reduce la distancias entre rendijas, pues a 
pesar que se repite el patrón este sufre un cambio de distancias en las proyecciones, esto se debe a que la función de
onda de Schrödinger que causa que el estado del sistema sufra superposición de estados
(donde se acentúan las proyecciones) e interferencia con el cancelamiento de algunas proyecciones, no obstante la relación
de la separación entre distancias de separación y proyección se debe a un entrelazamiento de estados que interpreta dicha
distancia proectandose en los resultados. A continuación una imagen del sistema cuántico

![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/resultado3.PNG)


## Simulación 
Para las simulaciones utilizamos un modelo matemático basado en los grafos del sistema y las matrices adyacencia propias
de los mismos, posteriormente realizamos una simulación en la librería simulación_clasico_cuantico en python de este
repositorio.

También tendremos en cuenta la forma en el que el experimento se representara, entonces el sistema tendra una matriz 
asociada y a su vez un vector de estado inicial

*Grafo*
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/grafo.PNG)

![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/numcomplejos.PNG)


*Matriz*
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/matriz.PNG)


## Elaboración 
**Materiales:**
* Cinta aislante negra 
* Un laser
* 1/8 de cartulina blanca
* Una aguja
* Alambre

**Pasos:**

* Pegamos un alambre en la mitad del laser logrando el efecto de la doble rendija junto con la cinta aislante
* preparar una base acorde a las necesidads del experimento
* tambien se pude usar papel aluminio cortando con la aguja para tener el efecto de doble rendija 
* Con la cartulina hicimos una base para reflejar el efecto

**Imagenes**

**proceso y materiales**

![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/materiales1.jpeg)
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/materales2.jpeg)
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/materiales3.jpeg)
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/materiales4.jpeg)


**Representación libreria**
```
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
```
### Pre-requisitos

- Tener instalado una version mayor o igual a python 3
- Es opcional tener instalado git 

ademas se van hacer uso de estas librerias una es nativa de python "numpy" y la otra es matplotlib.pyplot as plot
para descargar esta ultima compiladores como pychar ofrecen la opncon de descargarla directamente, en cualquier
otro caso seguir el siguiente link https://matplotlib.org/downloads.html

### Uso
Defina la matriz de su sistema cauntico o deterministico a su vez defina su vector de estado inicial ejemplo:
```
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
```
Usar alguna de las funciones de la libreria para saber el estado del sistema despues de t clicks, en el caso del ejemplo
anterior tenemos un sistema cuantico entonces vamos a usar, dado que queremos visualizar el diagrama de barras que
representa la probabilidad vamos a usar la grafico de probabilidades

```
print(grafico_probabilidades(Quantum_clicks(Matriz, Xvectorestado, 2)))
```
resultado
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/resultado2.PNG)
## Resultado 
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/resultado2.PNG)
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/resultado4.jpeg)
![](https://github.com/javier32rojas040506/CNYT/blob/master/Experimento_computacion_cuantica/Experimento%20Doble%20Rendija/imagenes/resultado5.jpeg)
ver video resultado https://www.youtube.com/watch?v=2LDqRkjJ7XY
 
 evidencaimos lo explicado en el patron obtenido pues como se explico anteriormente el patron interactua con la distancia 
  del lazer esto es claro en las fotos y el video el resultado ademas se puede analizar que si nuestro universo no fuera cauntico tendriamos
 unicamente un punto si no que es el resultado de la interaccion de la onda (luz lazer) que se superpone en algunos casos y en otros 
 se cancelan, tambien cabe recalcar que la el patron no se refleja la mayoria del tiempo y su calidad no es tan alta por
 variables que afectan el experimento como el medio, poder del lazer, etc. no obstante se logra apreciar el resultado,
 dandonos a entender que el universo es quantico y que los fenomenos de superposicion, inteferencia y entrelazamiento estan 
 presentes en la naturaleza y por esto tenemos como resultado el patron obtenido 



# Simulacion Sistemas Clasicos y Cuanticos
-Experimentos de sistemas clasicos con canicas rpresentados mediante coeficientes booleanos
-Experimentos de múltiples rendijas sistema clásico-probabilístico, con más de dos rendijas.
-Experimento de las múltiples rendijas sistema cuántico.
-Función que crea grafica con un diagrama de barras que muestra las probabilidades de un vector y sus estados. La imagen
 se muestra al final y seguarga en formato png.


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

_the proves are very important to know how efficient and correct are ours functions, therefore we use unittest library 
from python with parameter assertEqual to compare the answers_

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

```
###  How to Running Unittest ⌨️

_when you have the repository only follow the next address_

```
cd 1tercio/testLib_complejos
cd 1tercio/testMatrixVectorLib
```


## Built With 🛠️

_built with python 3.8_

## Author ️

* **Francisco Javier Rojas Muñoz** - *test, library and experiment* 
 
## referenced

*the model that i took for did the README is from:
[Villanuevand](https://github.com/Villanuevand)

---
