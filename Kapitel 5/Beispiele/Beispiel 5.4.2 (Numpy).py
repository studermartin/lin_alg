import numpy as np

M = np.array([  [0  , 1  , 2  , 1.5],
                [0.5, 0  , 0  , 0],
                [0  , 0.7, 0  , 0],
                [0  , 0  , 0.6, 0]], dtype=np.float64)
eig = np.linalg.eig(M)

# Spektrum
print("Spektrum:\n", eig.eigenvalues)

# Eigenvektoren/-räume
print("Eigenvektoren:\n", eig.eigenvectors)

# Perron-Frobenius-Eigenvektor normiert
print("1. Eigenvektor:\n", eig.eigenvectors[:,0])
print("Komponentensumme des 1. Eigenvektors:\n", eig.eigenvectors[:,0].sum())
print("Normierter 1. Eigenvektor:\n", eig.eigenvectors[:,0]/eig.eigenvectors[:,0].sum())

