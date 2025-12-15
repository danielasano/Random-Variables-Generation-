import numpy as np
from random import*
import matplotlib.pyplot as plt
from scipy.stats import*
np.random.seed(123)

def f(x):
  return 20*x*(1-x)**3
k = np.linspace(0,1,1000)
plt.plot(k,f(k), color='red')

def g(x):
  return 1

c = 135/64
def AR(n): #n = numero de amostras
  X = []
  aceitos = 0
  rejeitados = 0
  for i in range (0,n):
    while True:
      U1 = np.random.uniform(0,1)
      U2 = np.random.uniform(0,1)
      if U2 <= f(U1)/(c * g(U1)):
        X.append(U1)
        aceitos = aceitos + 1
        break
      else:
        rejeitados = rejeitados + 1
  return np.array(X), aceitos, rejeitados

l, aceitos, rejeitados = AR(1000)
print("Taxa de aceitação: ", aceitos / (aceitos + rejeitados))
print("Probabilidade de aceitação: ", 1/c)
plt.hist(l, bins=20, density=True)

