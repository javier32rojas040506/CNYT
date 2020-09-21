# Libreria_Num_Complejos

_This program can do the next operations with complex numbers_
 -add 
- Multiplications
- subtraction
- Division
- Module
- Conjugate
- conversion into polar and cartesian representation
- the phase of a complex number

##  Starting 🚀

_We need to know that the complex  number have one part real and other one imaginary, so we have_
```
5 + 7i
```
_to use the library we are going to use tuple with this structure_ 
```
(real, imagimary) ----> (5, 7) ----> 5 + 7i
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
```

###  How to Running Unittest ⌨️

_when you have the repository only follow the next address_

```
cd 1tercio/testLib_complejos
```


## Built With 🛠️

_built with python 3.8_

## Author ✒️

* **Francisco Javier Rojas Muñoz** - *test and library* 
 
## referenced

*the model that i took for did the README is from:
[Villanuevand](https://github.com/Villanuevand)

---
