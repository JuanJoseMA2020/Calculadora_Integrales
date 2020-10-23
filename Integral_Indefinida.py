#Integral_Indefinida
from sympy import Symbol
from sympy import integrate
from sympy import *

x = Symbol('x')

y1 = input("Ingrese la ecuacion: ")
y1 = sympify(y1)
pprint(y1)

plot(y1)

print("El resultado de la integral es: ")
print(integrate(y1),x)