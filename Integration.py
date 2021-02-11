import numpy as np 
import sympy as sp

sp.init_printing(use_latex = 'mathjax')

r1 = 0.2
r = sp.symbols("r")
v = (3*(1-25*r**2))

da = 2*3.14*r
print(da)
vda = v*da

Q = sp.integrate(vda,(r,0,r1))
print(Q)

V=Q/(3,14*r**2)
print(V,"m3/s")