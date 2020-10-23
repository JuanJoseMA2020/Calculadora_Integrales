#Integral_Definida
from sympy import Symbol
from sympy import integrate
from scipy.integrate import quad
from sympy import *
import matplotlib.pyplot as plt 
import numpy as np
import sympy as sy

x = Symbol('x')

i = input('Ingrese el limite inferior: ')
s = input('Ingrese el limite superior: ')

y1 = input("Ingrese la ecuacion: ")
y1 = sympify(y1)
pprint(y1)

plot(y1)

print("El resultado de la integral es: ")
print(integrate (y1 ,(x, i, s)))