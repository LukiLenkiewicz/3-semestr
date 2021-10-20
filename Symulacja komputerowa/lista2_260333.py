import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats

p = 0.05


def uniform(uniform_distribution):
    _, pvalue = stats.chisquare(uniform_distribution)
    print(f"Wynik testu chi-kwadrat: {pvalue}")
    if pvalue > p:
        print("Mamy podstawy do przyjęcia hipotezy o jednostajności rozkładu.")
    else:
        print("Mamy podstawy do odrzucenia hipotezy o jednostajności rozkładu.")


def normal(normal_distribution):
    _, pvalue = stats.shapiro(normal_distribution)
    print(f"Wynik testu Shapiro-Wilka: {pvalue}")
    if pvalue > p:
        print("Mamy podstawy do przyjęcia hipotezy o rozkładzie normalnym.")
    else:
        print("Mamy podstawy do odrzucenia hipotezy o rozkładzie normalnym.")
    mu = np.average(normal_distribution)
    sigma = np.std(normal_distribution)
    count, bins, ignored = plt.hist(normal_distribution, 30, density=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)))
    plt.show()


def compare_samples(samples):
    for i in range(len(samples)):
        for j in range(i+1, len(samples)):
            _, pvalue = scipy.stats.ttest_ind(samples[i], samples[j])
            print(f"Porównanie próby {i} i {j}: {pvalue}")
            if pvalue > p:
                print("Mamy podstawy do przyjęcia hipotezy o takiej samej populacji.")
            else:
                print("Mamy podstawy do odrzucenia hipotezy o takiej samej populacji.")


print("Rozkład jednostajny:")
uniform1 = np.random.uniform(0., 1., 100)
uniform(uniform1)
uniform2 = np.random.uniform(5., 10., 100)
uniform(uniform2)


print("Rozkład normalny: ")
normal1 = np.random.normal(0., 1., 100)
normal(normal1)
normal2 = np.random.normal(5., 10., 100)
normal(normal2)

samples = [uniform1, uniform2, normal1, normal2]
compare_samples(samples)