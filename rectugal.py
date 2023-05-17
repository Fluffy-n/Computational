import math

def f(x):
    return x**2 * math.cos(x/2)

def rectangular_integration(a, b, n):
    dx = (b - a) / n
    integral = 0.0
    for i in range(n):
        xi = a + i * dx
        integral += f(xi + dx/2) * dx
    return integral

# Параметри обчислення
a = 1.0
b = 2.0
n = 8
e = 0.5 * 10**(-8)

# Обчислення інтегралу
integral_approx = rectangular_integration(a, b, n)
integral_exact = math.sin(1) + 2*math.cos(1) - 2*math.sin(1)
error = abs(integral_exact - integral_approx)

# Виведення результатів
print(f"Інтеграл від f(x) на [{a}, {b}] з точністю {e}:")
print(f"За формулою прямокутників з {n} підінтервалами: {integral_approx:.9f}")
print(f"Точне значення: {integral_exact:.9f}")
print(f"Абсолютна похибка: {error:.9f}")