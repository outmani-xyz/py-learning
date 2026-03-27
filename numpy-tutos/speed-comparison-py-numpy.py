import time
import numpy as np

size = 10000000

list_a = list(range(size))

list_b = list(range(size))

start = time.time()

# to add list to another in python need for loog
res = []
for index in range(len(list_a)):
    res.append(list_a[index]+list_b[index])

end = time.time()

print(end-start)

arr_a = np.array(list_a)
arr_b = np.array(list_b)

start = time.time()
res = arr_a+arr_b
end = time.time()

print(end-start)