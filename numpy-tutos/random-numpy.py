import numpy as np

arr = np.random.rand(2,3)

print(arr)

arr2 = np.random.randn(3,2)

print(arr2)

nbr = np.random.randint(3,40)

print(nbr)

arr_1d_int = np.random.randint(1,33,5)

print(arr_1d_int)

arr_2d_int = np.random.randint(1,33,size=(3,4))

print(arr_2d_int)


np.random.seed(5)

print(np.random.rand(5,3))

arr_shufl = [2,4,5,7]

np.random.shuffle(arr_shufl)

print(arr_shufl)