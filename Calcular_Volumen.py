#Calculo de volumen
import matplotlib.pyplot as plt 
import numpy as np
from sympy import Integral, integrate
from sympy import *
from sympy.plotting import plot
from sympy import Symbol
from sympy.plotting import plot

x = Symbol('x')

i = input('Ingrese el limite inferior: ')
j = input('Ingrese el limite superior: ')

f = input('Ingrese la primera expresión: ')
f = sympify(f)
pprint(f)

g = input('Ingrese la segunda expresión: ')
g = sympify(g)
pprint(g)

p = plot(f, g, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()

print("\n")
print("------------------------------------------------------")
print("HABIENDO VISTO LA GRAFICA, POR FAVOR IDENTIFIQUE:")
print("------------------------------------------------------ \n")
fx=input('Expresión mayor: ')
fx= sympify(fx)
pprint(fx ) 


gx=input('Expresión menor: ')
gx= sympify(gx)
pprint(gx)

d1 = np.pi * Integral(fx**2,(x,i,j)).doit()
d2 = np.pi * Integral(gx**2,(x,i,j)).doit()
print("El valor del volumen entre {} y {} es : {}".format(i,j,d1-d2))