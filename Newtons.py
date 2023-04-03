import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / np.tan(x) - 0.5*x

def df(x):
    return -1/(np.sin(x)**2) - 0.5

a = 1
b = 2
eps = 0.0001
x0 = a
while True:
    fx0 = f(x0)
    dfx0 = df(x0)
    x1 = x0 - fx0 / dfx0
    print(f'Root approximation: {x1:.6f}')
    if abs(x1 - x0) <2*eps:
        break
    x0 = x1

print(f'The result with an accuracy of {eps}: {x1:.5f}') 