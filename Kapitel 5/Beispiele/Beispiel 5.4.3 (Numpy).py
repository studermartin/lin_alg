import numpy as np

M = np.array([  [ 0 ,1/4, 0 , 1 , 0 , 0 ],
                [1/2, 0 ,1/3, 0 , 1 , 0 ],
                [ 0 ,1/4, 0 , 0 , 0 , 1 ],
                [1/2,1/4, 0 , 0 , 0 , 0 ],
                [ 0 , 0 ,1/3, 0 , 0 , 0 ],
                [ 0 ,1/4,1/3, 0 , 0 , 0 ],], dtype=np.float64)
eig = np.linalg.eig(M)

# Spektrum
print("Spektrum:\n", eig.eigenvalues)

# Perron-Frobenius-Eigenvektor normiert
print("1. Eigenvektor:\n", eig.eigenvectors[:,0])
print("Komponentesumme des 1. Eigenvektors:\n", eig.eigenvectors[:,0].sum())
print("Normierter 1. Eigenvektor:\n", eig.eigenvectors[:,0]/eig.eigenvectors[:,0].sum())

