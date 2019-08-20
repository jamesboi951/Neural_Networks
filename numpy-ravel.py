import numpy as np

arr = np.array([[[  0,   1,   2],
                 [ 10,  12,  13]],
                [[100, 101, 102],
                 [110, 112, 113]]])

print("arr:")
print(arr)

print("arr.ravel():")
print(arr.ravel())
#array([  0,   1,   2,  10,  12,  13, 100, 101, 102, 110, 112, 113])

