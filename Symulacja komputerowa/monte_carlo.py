from numpy.core.numeric import array_equiv
from scipy import random
import numpy as np

def f(x):
    return np.sin(x)

a = 0
b = np.pi
N = 1000000

arr = np.zeros(N)

for i in range(len(arr)):
    arr[i] = random.uniform(a, b)

integral = 0.0

for i in arr:
    integral += f(i)

ans = (b-a)/float(N)*integral

print(ans)