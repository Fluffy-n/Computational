import math

# Оголошення функції для обчислення значення f(x)
def f(x):
    return x**2 * math.cos(x/2)

# Задання вхідних параметрів
a = 1
b = 2
N_0 = 8
e = 0.5 * 10**(-8)

# Обчислення величини кроку h
h = (b - a) / N_0

# Ініціалізація змінної для збереження попередньої суми
prev_sum = 0

# Початкове значення суми
sum = (f(a) + f(b)) / 2

# Обчислення значення суми з використанням інтегральної формули трапеції
for i in range(1, N_0):
    x_i = a + i*h
    sum += f(x_i)
    
# Обчислення значення інтегралу
integral = sum * h

# Виведення результату на екран з точністю до e знаків
print("Значення інтегралу: {:.9f}".format(integral))