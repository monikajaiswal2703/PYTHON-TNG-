import numpy as np

# Create a 2-D array, set every second element in
# some rows and find max per row:

x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:,::2] = -99
print(x)
print(x.max(axis=1))
# array([ 4,  8, 13])