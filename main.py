import numpy as np
A = np.array([[-1, 0.52, 0.08, 0.13],
              [0.07, -1.38, -0.05, 0.41],
              [0.04, 0.42, -0.89, -0.07],
              [0.17, 0.18, -0.13, -0.81]])
b = np.array([0.22, -1.8, 1.3, -0.33])
def jacobi(A, b, eps=0.0001, max=100):
    x = np.zeros_like(b, dtype=np.double)
    T = A - np.diag(np.diagonal(A))
    steps = 0
    for k in range(max):
        x_old = x.copy()
        x[:] = (b - np.dot(T, x)) / np.diagonal(A)
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < eps:
            break
        steps += 1
    print(f"Number of iterations: {steps}")
    return x
x = jacobi(A, b)
print("Solution:", np.around(x, decimals=4))