#######  PROGRAM FOR PLOT OF DRAG FORCE vs VELOCITY  ########


import math  #importing math module for mathematical calculations
import matplotlib.pyplot as plt # for plotting graph


#DRAG COEFFICIENT 
drag_coefficient = 1.1

#Fontal Area(in sq.meters)
area = 4.9

#Density of the fluid(in kg/qubic m)
density = 1.226

#The flow velocity relative to the object(in km/h)

velocities = [20,22,24,25,26,27,29,30,35]
 
#Drag Forces for different values of velocity(in N)
forces = []

#For loop to compute each force corresponding to given velocity

for velocity in velocities :#In each iteration each value of velocity ie iterated
	force = (0.5*drag_coefficient*area*density*pow(velocity,2))/1000   #Formula for computation of drag force
	forces.append(force)    #Appends each value of force to the 'forces' list

	
plt.plot(velocities,forces)#Plots the graph of force vs velocities
plt.xlabel('velocity(in km/h)')#Gives label for x-axis
plt.ylabel('force(in N)')#Gives label for y-axis 
plt.show()#Brings the plot from backend to frontend


############################ END #########################################