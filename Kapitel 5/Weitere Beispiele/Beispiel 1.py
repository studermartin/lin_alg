import numpy as np

M = np.array([[0   ,  1.00, 0   , 0   , 0],
              [0.96,  0   , 0   , 0   , 0],
              [0   ,  0.98, 0   , 0   , 0],
              [0   ,  0   , 0.96, 0   , 0],
              [0   ,  0   , 0   , 0.80, 0]], dtype=np.float64)


eig = np.linalg.eig(M)

# Spektrum
print("Spektrum:", eig.eigenvalues)

# Eigenvektoren/-räume
print("Eigenvektoren:", eig.eigenvectors)
# Achtung: Eigenvektoren sind Zeilenvektoren!


