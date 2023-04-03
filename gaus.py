import numpy as np
B = np.array([[7.5, 1.8, -2.1, -7.7, 1.1],
              [-10, 1.3, -20, -1.4, 1.5],
              [2.8, -1.7, 3.9, 4.8, 1.2],
              [10, 31.4, -2.1, -10, -1.1]])
# triangular view
for i in range(len(B)):
    for j in range(i+1, len(B)):
        F = B[j][i] / B[i][i].
        B[j] -= F * B[i]
# backtrack
x = np.zeros(len(B))
for i in range(len(B)-1, -1, -1):
    x[i] = (B[i][-1] - np.dot(B[i][i+1:-1], x[i+1:])) / B[i][i]
print("Solution of the system:")
for i in range(len(x)):
    print(f "x_{i+1} = {x[i]}")