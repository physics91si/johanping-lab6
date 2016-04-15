#Johanna O'Day Lab 6

import numpy as np
import matplotlib.pyplot as plt

#Part 1
arr = np.zeros([9,9]) #creates a 9x9 array of zeros
arr[:,0:3] = 1  #assign last 3 columns to 1 
arr[8,] = 1 #and last row to value 1
arr[(4,7,1),(5,7,8)] = 1  # assign three individual entries the value 1: (4,5), (7,7), and (1,8).
plt.spy(arr)
plt.savefig('Part 1 Plot')