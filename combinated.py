import math
# Define the input data
a = 7
b = 6.5
eps = 0.0001
# Define the function and its derivative
def f(x):
    return 1 / math.tan(x) - 0.5 * x
def f_derivative(x):
    return -1 / math.sin(x) ** 2 - 0.5
# Perform the combined method of tangents and chords
def root_combination(f, f_derivative, a, b, eps):
    # Set the starting points
    x0 = a
    x1 = b
    # Print the table header
    print(' | x0 | x1 | x2 | x3 | f(x3) ')
    print('---------------------------------------------------')
    # Start the iteration cycle
    for i in range(1, 101):  # The maximum number of iterations is 100
        # Calculate x2 and x3
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x3 = x2 - f(x2) / f_derivative(x2)
        # Print the data of the current iteration
        print(f'{i:3d} | {x0:.4f} | {x1:.4f} | {x2:.4f} | {x3:.4f} | {f(x3):.4f}')
        # Check the stop condition
        if abs(x3 - x2) < eps:
            return x3
        # Move the points for the next iteration
        x0 = x1
        x1 = x3
root = root_combination(f, f_derivative, a, b, eps)
print('---------------------------------------------------')
print(f'Root = {root:.4f}')