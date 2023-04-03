import math
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1 / np.tan(x) - 0.5*x
a = 1
b = 2
eps = 0.0001
# Determine the initial values of x0 and x1
x0 = a
x1 = b
while abs(x1 - x0) > 2* eps:
    # Calculate the values of f(x0) and f(x1)
    f_x0 = f(x0)
    f_x1 = f(x1)
    # Calculate the next approximation x2
    x2 = x1 - f_x1*(x1 - x0)/(f_x1 - f_x0)
    print(f'Root approximation: {x2:.5f}')
    # Update the values of x0 and x1
    x0 = x1
    x1 = x2
print(f'Result with an accuracy of {eps}: {x2:.5f}')
plt.show()  