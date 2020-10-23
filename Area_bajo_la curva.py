#Calculo de Area bajo la curva

#%matplotlib inline
import matplotlib.pyplot as plt 
import numpy as np
import sympy as sy

y1 = input("Ingrese la ecuacion: ")

def f(x): return 4*x + 3*x**2

i = input('Ingrese el limite inferior: ')
s = input('Ingrese el limite superior: ')

x = np.linspace(int(i)-1, int(s)+1, 1000)

plt.plot(x, f(x))
plt.axhline(color = 'black')
plt.fill_between(x, f(x), where = [(x > int(i)) and (x < int(s)) for x in x], color = 'red', alpha = 0.3)
plt.show()

x = sy.Symbol('x')
print("El area de la funcion en u^2 es: ")
print(sy.integrate(f(x), (x,i,s)))