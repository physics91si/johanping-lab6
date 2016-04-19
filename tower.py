#johanna oday lab6 
#Part 2

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math

file_data = np.loadtxt('droptower_vdata.txt')
print(file_data)
plt.figure(0)
time = file_data[:,0]

#Velocity
velocity = file_data[:,1]
velocity_plot = plt.plot(time,velocity)
plt.title("Velocity plot")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.savefig('Velocity plot.png')
#plt.show()

#Position
plt.figure(1)
position = integrate.cumtrapz(velocity, x= time, dx = 1.0, initial =0)
position_plot = plt.plot(time,position)
plt.title('Position plot')
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.savefig('Position Plot.png')
#plt.show()

#Acceleration
plt.figure(2)
acceleration = np.diff(velocity)
print(acceleration)
time2 = np.delete(time,0)
print(time2) 
#append the time array because ndiff has one less elt since it's
#taking the difference between two points and thus will have n-1 elements of array length n
acceleration_plot = plt.plot(time2,acceleration)
plt.title('Acceleration plot')
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s*s)")
plt.savefig('Acceleration Plot.png')
#plt.show()

#Extra Question
positive_a = acceleration[acceleration>0]
average_a = sum(positive_a)/len(positive_a)
print("The average positive acceleration is " + str(average_a))
