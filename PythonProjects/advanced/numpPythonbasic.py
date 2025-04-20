# using numpy
import numpy as np

# create a simple array that stores generated data from 10 to 50
data = np.arange(10, 50)
print("Data:", data)

# max and min values
print("Max value:", np.max(data))
print("Min value:", np.min(data))

# multiply the array by 3
data = data * 3
print("Data multiplied by 3:", data)