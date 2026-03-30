import numpy as np

arr = np.array(range(1,5))

print(arr.shape)

array_2 = np.array([
    [1,2,4,5],
    [31,9,4,8],
    [14,0,4,4],
    [18,60,4,4],
    [10,0,4,54],
])

print("shape", array_2.shape)
print("ndim", array_2.ndim)
print("size", array_2.size)
print("datat type", array_2.ndim)

print("sum columns",np.sum(array_2,axis=0))
print("sum row",np.sum(array_2,axis=1))
print("max value",np.max(array_2))
arr3 = array_2.reshape(4,5)
print('reshape', arr3)