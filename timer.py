import numpy as np
import timeit
import time
from random import shuffle

t0 = time.time()
ar1 = list(range(1,100))
t1 = time.time()

print(t1-t0)

t2 = time.time()
ar2 = np.arange(100)
t3 = time.time()

print(t3-t2)

# def check():
#     return list(range(1,1000000))
# print(timeit.timeit(check, number = 1000))

def check_2():
    return np.arange(1000000)

def check_3():
    l = np.arange(1000000)
    shuffle(l)
    return l

print(timeit.timeit(check_2, number = 1000))
print(timeit.timeit(check_3, number = 1000))