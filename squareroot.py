import numpy as np

# Inputting the initial matrix
A = np.array([[1.17, -0.65, 1.54],
              [-0.65, 1.16, -1.73],
              [1.54, -1.73, 2.15]])

# Transpose the matrix
A_T = np.transpose(A)

# Entering a column of free terms
b = np.array([-1.43, 0.68, 1.87])

# Decomposition of matrix A_T into matrix Q and R using the Gram-Schmidt orthogonalization method
n = len(A_T)
Q = np.zeros((n, n))
R = np.zeros((n, n))

for j in range(n):
    v = A_T[:, j]
    for i in range(j):
        R[i, j] = np.dot(Q[:, i], A_T[:, j])
        v = v - R[i, j]*Q[:, i]
    R[j, j] = np.linalg.norm(v)
    Q[:, j] = v/R[j, j]

# Solving the system of linear equations Ax = b using the square root method
y = np.dot(Q.T, b)
x = np.zeros(n)
for j in range(n-1, -1, -1):
    x[j] = y[j]/R[j, j]
    y[0:j] = y[0:j] - R[0:j, j]*x[j]

# Print the solution
print("Solution: x =", x)