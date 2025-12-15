import numpy as np
from random import*
import matplotlib.pyplot as plt
from scipy.stats import*
np.random.seed(123)

lambd = 1
tam = 1000
u = np.random.uniform(0,1,tam)
x = -(1/lambd)*np.log(1-u)
plt.hist(x, bins=20, density=True)

x = np.linspace(0,8,tam)
pdf_values = expon.pdf(x, scale=1/lambd)
plt.plot(x, pdf_values, color='red')

