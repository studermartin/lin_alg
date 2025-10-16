import numpy as np

M = np.array([[3,  3,  3],
              [0, -3, -6],
              [0, -3,  0]], dtype=np.float64)


eig = np.linalg.eig(M)

# Spektrum
print("Spektrum:", eig.eigenvalues)

# Eigenvektoren/-räume
print("Eigenvektoren:", eig.eigenvectors)

