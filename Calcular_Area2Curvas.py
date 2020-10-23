#Calculo de Area de 2 curvas
from sympy import *
import matplotlib.pyplot as plt 
import numpy as np
import sympy as sy

x = symbols("x")
def f(x): return x**3 - 3*x - 1
def g(x): return x**2/2 + 2*x -2
sol =list(N(solveset(f(x)-g(x))))  
print("Los limites son: ")
print(sol) 
resp=input("Cuantos limites tiene su ejercicio: ") 
if resp == '2':
  
    a=re(sol[0])
    b=re(sol[1])

    x = np.linspace(int(a)-1, int(b)+1, 1000)
    plt.plot(x, f(x), x, g(x))
    plt.axhline(color = 'black')
    plt.fill_between(x, f(x), g(x), where = [(x > float(a)) and (x < float(b)) for x in x], color = 'yellow', alpha = 0.3) 
    plt.show()

    x = sy.Symbol('x')
    a1=integrate(g(x)-f(x),(x,a,b))
    a= a1
    print("El area total de la region encerrada por las funciones (y1, y2) es: ")
    print (a)
else:
  a=re(sol[0])
  b=re(sol[1])  
  c=re(sol[2])

  x = np.linspace(int(a)-1, int(c)+1, 1000)
  plt.plot(x, f(x), x, g(x))
  plt.axhline( color = 'black')
  plt.fill_between(x, f(x), g(x), where = [(x > float(a)) and (x < float(b)) for x in x], color = 'yellow', alpha = 0.3)
  plt.fill_between(x, f(x), g(x), where = [(x > float(b)) and (x <float(c)) for x in x], color = 'gray', alpha = 0.3)
  plt.show()

  x = sy.Symbol('x')
  a1=integrate(f(x)-g(x),(x,a,b))
  a2=integrate(g(x)-f(x),(x,b,c))
  a= a1 + a2 
  print("El area total de la region encerrada por las funciones (y1, y2) es: ")
  print(a) 