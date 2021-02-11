#Minimize f = x(xy-sqrt(z)) with the following constraint:
# x+2y-6z <0
# x-y < 8
# xyz >= 100
# -10 <=x <=12
from numpy import *
import numpy as np 
from scipy import *
from scipy.optimize import minimize

def functionToMinimize(p):
    x,y,z = p
    return x*(x*y - np.lib.scimath.sqrt(z))


def constraint2(p):
    x,y,z = p
    return -(x+2*y -6*z)

def constraint1(p):
    x,y,z = p
    return -(x-y)+8

def constraint3(p):
    x,y,z = p
    return (x*y*z)-100    



cons = [{'type':'ineq','fun':constraint1},{'type':'ineq','fun':constraint2},{'type':'ineq','fun':constraint3}]

bondaryConditions = ((-10,12),(-inf,+inf),(-inf,+inf))

results = minimize(functionToMinimize,(1,1,1),bounds = bondaryConditions,constraints = cons)

print(results)