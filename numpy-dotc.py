# https://docs.scipy.org/doc/numpy/reference/generated/numpy.c_.html#numpy.c_
import numpy as np

print("array1:", np.array([1,2,3])) 
print("array2:", np.array([4,5,6])) 
print("np.c_:")
print(np.c_[np.array([1,2,3]), np.array([4,5,6])])

#array([[1, 4],
#       [2, 5],
#       [3, 6]])

#np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
#array([[1, 2, 3, 0, 0, 4, 5, 6]])

