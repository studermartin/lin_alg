import numpy as np

M = np.array([  [ 0 ,1/4, 0 , 1 , 0 , 0 ],
                [1/2, 0 ,1/3, 0 , 1 , 0 ],
                [ 0 ,1/4, 0 , 0 , 0 , 1 ],
                [1/2,1/4, 0 , 0 , 0 , 0 ],
                [ 0 , 0 ,1/3, 0 , 0 , 0 ],
                [ 0 ,1/4,1/3, 0 , 0 , 0 ],], dtype=np.float64)
eig = np.linalg.eig(M)

# Spektrum
print("Spektrum:", eig.eigenvalues)

# Perron-Frobenius-Eigenvektor normiert
print(eig.eigenvectors[:,0])
print(eig.eigenvectors[:,0].sum())
print(eig.eigenvectors[:,0]/eig.eigenvectors[:,0].sum())

