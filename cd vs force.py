####### Program for plot of drag force vs drag coefficients ########



import math  #importing math module for mathematical calculations
import matplotlib.pyplot as plt # for plotting graph

import math  #importing math module for mathematical calculations
import matplotlib.pyplot as plt # for plotting graph


#Different values of drag coefficients based on different shapes
drag_coefficients =[1.1,1.3,0.88,0.83,1.0,1.15,1.095,0.968,0.741,0.699,0.05,0.10]

# Frontal Area (in sq.meters)
area = 4.9

#Density of the fluid(in kg/qubic m)
density = 1.226

#The flow velocity relative tonthe object(in km/h)

velocity = 20

#Drag Forces for different values of coefficient of drag(in N)
forces = []

#For loop to compute each force corresponding to given drag coefficient

for drag_coefficient in drag_coefficients :#In each iteration each value of velocity ie iterated
	force = (0.5*drag_coefficient*area*density*pow(velocity,2))/1000   #Formula for computation of drag force
	forces.append(force)    #Appends each value of force to the 'forces' list

	
plt.plot(drag_coefficients,forces)#Plots the graph of force vs velocities
plt.xlabel('drag_coefficient')#Gives label for x-axis
plt.ylabel('force(in N)')#Gives label for y-axis 
plt.show()#Brings the plot from backend to frontend



###################################### END ####################################