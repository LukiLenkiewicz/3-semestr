from numpy import random, sqrt, log, sin, cos, pi
import numpy as np
from scipy.stats import kurtosis, skew
from scipy import stats
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

def gaussian(u1,u2):
  z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
  z2 = sqrt(-2*log(u1))*sin(2*pi*u2)
  return z1,z2


u1 = random.rand(1000)
u2 = random.rand(1000)
print(u1)
print(u2)

z1,z2 = gaussian(u1,u2)

print(stats.shapiro(z1))
print(stats.shapiro(z2))


distribution(z1)
distribution(z2)