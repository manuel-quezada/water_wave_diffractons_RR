import numpy as np

data = np.genfromtxt('change_in_shape_diff1_Nx64.txt',delimiter=',')
print np.max(data[:,0]), np.max(data[:,1]), np.max(data[:,2])
data = np.genfromtxt('change_in_shape_diff1_Nx128.txt',delimiter=',')
print np.max(data[:,0]), np.max(data[:,1]), np.max(data[:,2])

