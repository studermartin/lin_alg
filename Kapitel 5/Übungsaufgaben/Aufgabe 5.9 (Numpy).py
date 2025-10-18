import numpy as np

M = np.array([  [0  , 0.63, 1  , 0.9],
                [0.6, 0   , 0  , 0],
                [0  , 0.57, 0  , 0],
                [0  , 0   , 0.57,0.4]], dtype=np.float64)
eig = np.linalg.eig(M)

# Spektrum
print("Spektrum:", eig.eigenvalues)

# Perron-Frobenius-Eigenvektor normiert
print(eig.eigenvectors[:,0])
print(eig.eigenvectors[:,0].sum())
print(eig.eigenvectors[:,0]/eig.eigenvectors[:,0].sum())

