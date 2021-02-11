from mpl_toolkits import mplot3d
import numpy as np 
import matplotlib.pyplot as plt
import math

def f(x,y):
    return ((np.power(y,2)/2)-np.cos(x))

x = np.linspace(-2*math.pi,2*math.pi,35)    
y = np.linspace(-2*math.pi,2*math.pi,35)

X,Y = np.meshgrid(x,y)
Z=f(X,Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
new=ax.plot_surface(Y,X,Z,rstride=1,cstride=1,cmap='jet',edgecolor='black')
fig.colorbar(new)
ax.set_xlabel("theta2")
ax.set_ylabel("theta1")
ax.set_zlabel("motion")
fig.savefig("img.png")
fig.show()
