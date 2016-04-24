from scipy.stats import poisson
import numpy as np
from matplotlib import pyplot as plt
lambdas = [ 1.0, 2.5, 5.0]
colours = ['red', 'blue', 'green']

x_s = np.arange(20)
y_s = [poisson.pmf(x_s, lambda_) for lambda_ in lambdas]

for ii in range(len(y_s)):
    plt.bar(x_s, y_s[ii], color = colours[ii], alpha = 0.5)
plt.show()