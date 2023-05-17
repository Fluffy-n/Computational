import math

def f(x):
    return x**2 * math.cos(x/2)

def simpson_rule(a, b, N):
    h = (b-a)/N
    
    sum_1 = 0
    for i in range(1, N, 2):
        sum_1 += f(a + i*h)
        
    sum_2 = 0
    for i in range(2, N, 2):
        sum_2 += f(a + i*h)
        
    integral = (h/3) * (f(a) + 4*sum_1 + 2*sum_2 + f(b))
    return integral

a = 1
b = 2
N_0 = 8
e = 0.5 * 10**(-8)
integral_prev = simpson_rule(a, b, N_0)
print(f"The integral of f(x) from {a} to {b} is approximately {integral_prev:.9f} ")