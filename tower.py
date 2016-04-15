#johanna oday lab6 
#Part 2

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math

file_data = np.loadtxt('droptower_vdata.txt')
print(file_data)

time = file_data[:,0]
velocity = file_data[:,1]
velocity_plot = plt.plot(time,velocity)
plt.savefig('Velocity plot')
plt.show()

position = scipy.integrate.simps(velocity)
position_plot = plt.plot(time,position)
plt.savefig('Position Plot')