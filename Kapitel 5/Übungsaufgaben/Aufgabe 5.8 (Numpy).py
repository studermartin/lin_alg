import numpy as np

M = np.array([  [ 0     ,0.5/3.5, 0     , 1 , 0     , 0 ],
                [2/2.5  , 0     ,1.5/3  , 0 , 0.5/0.5, 0 ],
                [ 0     ,1/3.5  , 0     , 0 , 0     , 1/1 ],
                [0.5/2.5,1/3.5  , 0     , 0 , 0     , 0 ],
                [ 0     , 0     ,1/3    , 0 , 0     , 0 ],
                [ 0     ,1/3.5  ,0.5/3  , 0 , 0     , 0 ],], dtype=np.float64)
eig = np.linalg.eig(M)

# Spektrum
print("Spektrum:", eig.eigenvalues)

# Perron-Frobenius-Eigenvektor normiert
print(eig.eigenvectors[:,0])
print(eig.eigenvectors[:,0].sum())
print(eig.eigenvectors[:,0]/eig.eigenvectors[:,0].sum())

