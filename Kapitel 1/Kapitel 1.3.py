import numpy as np

# Beispiel 1.48 a) resp. 1.52: Reguläre Matrix
A = np.array([[2,4,2],
              [7,6,2],
              [12,22,11]], dtype=np.float64)  


print(np.linalg.matrix_rank(A))

# Beispiel 1.48 b) resp. 1.53: Singuläre Matrix
A = np.array([[1,1,0,1],
              [1,-1,2,3],
              [3,-1,4,7],
              [-3,3,-6,-9]], dtype=np.float64)  

print(np.linalg.matrix_rank(A))

