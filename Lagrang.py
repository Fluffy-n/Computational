import numpy as np
y = np.array([0.30452, 1.02652, 2.12928, 3.62686, 6.0502, 11.0765])
x = np.array([0.3, 0.9, 1.5, 2, 2.5, 3.1])
# Function for Lagrange interpolation
def L(X):
    L = 0 # Initializing the variable L as 0
    for i in range(len(x)):  # Loop for each point x
        k = 1 # Initializing the variable k as 1
        for j in range(len(x)):  # Loop for each point x except the i-th
            if i != j: # Checking if i is not equal to j
                k *= (X - x[j]) / (x[i] - x[j]) # Calculating each product
        L += k * y[i] # Adding to L the product of the corresponding value of y
    return L # Return the interpolated value
# Calculation and printing of interpolated values for given x
x_values = [0.5, 1.7, 2.9]
total = 0
for x_val in x_values:
    total += L(x_val)
    print(f "L({x_val}) = {L(x_val)}")
print("Total:", total)