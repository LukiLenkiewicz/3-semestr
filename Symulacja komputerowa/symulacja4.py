import numpy as np
from scipy.stats import kurtosis, skew
import statistics


def distribution(arr):
    average = np.average(arr)
    variance = statistics.variance(arr)
    standard_deviation = statistics.stdev(arr)
    skewness = skew(arr)
    kurtosis_ = kurtosis(arr)
    median = statistics.median(arr)

    print(f"Średnia: {average}\nWarancja: {variance}\nOdchylenie standardowe: "
          f"{standard_deviation}\nSkośność: {skewness}\nKurtoza: {kurtosis_}"
          f"\nMediana: {median}\n\n")


def lcg(n):
    a = 4
    c = 1
    m = 2**32 - 1
    seed = 0
    arr = [seed]
    for _ in range(n):
        seed = (a*seed + c)%m
        arr.append(seed)
    return arr

def fib_gen(n):
    x0 = 0
    x1 = 1
    arr = [0, 1]
    m = 9
    for _ in range(n):
        xn = (x1 + x0) % m
        arr.append(xn)
        x0 = x1
        x1 = xn
    return arr


print(lcg(10))
print(fib_gen(10))
distribution(lcg(10))
distribution(fib_gen(10))