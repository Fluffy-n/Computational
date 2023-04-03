import numpy as np
def gauss_seidel(A, b, eps=0.001, max_iterations=1000):
    x = np.zeros_like(b, dtype=np.float64)
    n = A.shape[0]
    for iteration in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        
        if np.linalg.norm(x_new - x) < eps:
            return x_new
        x = x_new
    raise Exception(f"Gauss-Seidel method {max_iterations} not finded ")
A = np.array([
    [7.8, 5.3, 4.8],
    [3.3, 1.1, 1.8],
    [4.5, 3.3, 2.8]
])
b = np.array([1.8, 2.3, 3.4])
x = np.linalg.solve(A, b)
print(np.around(x, decimals=4))