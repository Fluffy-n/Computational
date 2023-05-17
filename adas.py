import math

def f(x, y):
    return x * y**3 - y

def runge_kutta(x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6

a, b = 0, 1
h = 0.1  # step size for Runge-Kutta method
n = int((b-a) / h) + 1
x = [a + i*h for i in range(n)]
y = [0] * n
y[0] = 1  # initial condition

# use Runge-Kutta method to generate initial values
for i in range(1, 4):
    y[i] = runge_kutta(x[i-1], y[i-1], h)

# use Adams method to solve the differential equation
for i in range(3, n-1):
    y[i+1] = y[i] + h/24 * (55*f(x[i], y[i]) - 59*f(x[i-1], y[i-1]) + 37*f(x[i-2], y[i-2]) - 9*f(x[i-3], y[i-3]))

# print the solution
for i in range(n):
    print(f"x = {x[i]:.1f}, y = {y[i]:.4f}")