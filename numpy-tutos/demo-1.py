import numpy as np

py_list = [4,5,6,7]
py_list_2 = [10,11,12,34]
# here is like concatination
res = py_list + py_list_2
print(res)

# to add list to another in python need for loog
res = []
for index in range(len(py_list)):
    res.append(py_list[index]+py_list_2[index])

print(res)


#here doing math operation
np_list  = np.array([2,3,4,5])
np_list_2  = np.array([2,3,4,5])

print(np_list + np_list_2)

