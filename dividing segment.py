import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / np.tan(x) - 0.5*x

a = 1
b = 2
eps = 0.0001

x = np.linspace(a, b)
plt.plot(x, f(x))
plt.axhline(y=0, color='black', lw=0.5)

while abs(b - a) >2* eps:
    c = (a + b) / 2
    print(f'Root: {c:.4f}')
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

plt.plot(c, f(c), 'ro')
print(f'Result with accuracy {eps}: {c:.4f}')
plt.show()