
################    Program Otto-Cycle ############################

import math  #importing math module for mathematical calculations.
import matplotlib.pyplot as plt # for plotting graph.


def volumes_generator(min_angle,max_angle,total_num_angles,compression_ratio,clearence_volume,R):#The function which calculates the volume of the cylinder for different values of angle

	angles = []  # List to hold different values of angle
	volumes = []  # List to hold different values of volumes
	angle_diff = (max_angle - min_angle)/(total_num_angles-1) #calculates change in angle 
#Foor loop generates volumes corresponding to the each angle
	for i in range(0,total_num_angles):

		angle = min_angle + i*angle_diff #Logic to generate different values of angle
		angles.append(angle) #Append function appends each generated value to the angles list.

		#The formula to calculate the volume of cylinder for different values of crankangle.
		#The formula is givven by V = [1 + (0.5*compression_ratio-1)*(R + 1 + cos(crank_angle))]*clearence_volume

		trm1 = 0.5 * (compression_ratio-1)#Splitting equation into number of parts 
		trm2 = (R+1) + math.cos(angle)
		trm3 = pow(pow(R,2)-pow(math.sin(angle),2),0.5)

		volume = (1 + trm1*(trm2 - trm3))*clearence_volume # Calculating the volume for corresponding value of crank angle
		volumes.append(volume) #Append function appends each generated value to the volumes list.
		
		
		 
	return volumes # Returning volumes list to the main function	
 	
 

bore = 0.1 #Assigning the value of bore diameter
stroke = 0.1  #Assigning the value of stroke length
connecting_rod_len = 0.15 #Assigning the length of connecting rod 
compression_ratio = 10 #Assigning the value of compression ratio
a = stroke/2 #Crank radius which is given by stroke length/2.
R = connecting_rod_len/a

min_angle = math.radians(0) #Minimum angle is taken as 0 (in radians) for generating the values for crank angle
max_angle = math.radians(180) #Maxmimum angle is taken as 180 (in radians) for generating the values for crank angle
total_num_angles =45 #Total number of angles to be generated 
gamma = 1.4 #Taking value of gamma as 1.4


p_compression = [] #Declaring empty list for accomadation of pressures during compression

p_expansion = [] #Declaring empty list for accomadation of pressures during expansion


swept_volume = (math.pi/4)*pow(bore,2)*stroke #Formula to calculate the swept volume (pi*bore^2*stroke/4)
clearence_volume = swept_volume/(compression_ratio-1) #Formula to calculate the clearence volume( swept volume / (compression ratio - 1)

v1 = swept_volume + clearence_volume #Volume after the suction stroke
p1 = 101325 #Pressure at the end of suction stroke
t1 =500 #Temperature at the end of suction stroke

#State 2 i.e Compression Stroke

v2 = clearence_volume #Volume after the compression stroke
p2 = p1*pow(v1/v2 , gamma) #Volume after the compression stroke
rhs = (p1*v1)/t1
t2 = (p2*v2)/rhs 

#Calling volume generator function to generate different volumes during compression
v_compression= volumes_generator(min_angle,max_angle,total_num_angles,compression_ratio,clearence_volume,R)


#Foor loop to calculate compression pressure for the corresponding volume at that time
for v in v_compression : 
	#Formula to calculate the pressure during the compression is given by p = p1(v1/v)^gamma
	constant = p1*pow(v1,gamma)
	p_compression.append(constant/pow(v,gamma))#Append function appends each generated value to the p_compression list.

#State 3 i.e Expansion Stroke

v3 =v2 #Volume at begining of expansion stroke
t3 = 2300#Temperature of the gas at the begining of the expansion stroke 
#Formula to calculate the pressure at this ponit is given by ideal gas equation i.e P3 = p2*v2*t3/(v3*t2)
rhs = p2*v2/t2
p3 = rhs*t3/v3
#Calling volumes generator function to generate the volumes during expansion stroke
v_expansion = volumes_generator(min_angle,max_angle,total_num_angles,compression_ratio,clearence_volume,R)


#Foor loop to calculate compression pressure for the corresponding volume at that time

for v in v_expansion :
	#Formula to calculate the pressures during the expansion is given by p = p3(v3/v)^gamma
	constant = p3*pow(v3,gamma)
	p_expansion.append(constant/pow(v,gamma))#Append function appends each generated value to the p_expansion list.


#State 4
v4 = v1#volume at the begining of exhaust stroke
p4 = p3 * pow(v3, gamma)/pow(v4,gamma) #Pressue at end of the expansion stroke
t4 = p4*v4/rhs




#Finding thermal efficiency.
#Formula to find the thermaln efficiency is ,n = 1-(1/((compression ratio)^(k-1))

Thermal_efficiency = 1-(1/(pow(compression_ratio , gamma-1)))
print(f"Thermal Efficiency = {Thermal_efficiency}")


plt.plot(v_compression,p_compression)#Plots the compression volumes against compression pressures.
plt.plot(v_expansion,p_expansion)#Plots the expansion volumes volumes against expansion pressures.
plt.plot([v2,v3],[p2,p3])#Plots the volume against pressure at end of compression stroke 
plt.plot([v4,v1],[p4,p1])#Plots the volume against pressure at end of expansion stroke
plt.ylabel("Pressure(in Pa)") #Gives title to the Y-axis
plt.xlabel("Volume (in m^3)") #Gives title to the X-axis
plt.show()#Brings the plot from the backend t the frontend.



####################################    END  #########################################
