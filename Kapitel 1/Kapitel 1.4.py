import numpy as np

gl= np.array([[1,1,1,1],
              [2,2,1,-3],
              [-4,5,6,1]], dtype=np.float64)  

A = gl[:, :-1]  # Coefficient matrix
b = gl[:, -1]   # Right-hand side vector
# print(A)
# print(b)

# print(np.linalg.det(A))
print(np.linalg.inv(A)@b)


