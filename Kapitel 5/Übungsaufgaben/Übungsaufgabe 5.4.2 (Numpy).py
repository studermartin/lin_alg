import numpy as np

M = np.array([  [0  , 1  , 2  , 1.5],
                [0.5, 0  , 0  , 0],
                [0  , 0.7, 0  , 0],
                [0  , 0  , 0.6, 0]], dtype=np.float64)
eig = np.linalg.eig(M)

# Spektrum
print("Spektrum:", eig.eigenvalues)

# Eigenvektoren/-räume
print("Eigenvektoren:", eig.eigenvectors)

# Perron-Frobenius-Eigenvektor normiert
print(eig.eigenvectors[:,0])
print(eig.eigenvectors[:,0].sum())
print(eig.eigenvectors[:,0]/eig.eigenvectors[:,0].sum())

