import numpy as np

M = np.array([[0,0.536],
              [1, 0.464]], dtype=np.float64)

v = np.array([0, 1], dtype=np.float64)
for i in range(10):
    v = M @ v
    # print(f"Iteration {i+1}: {v}")

# eigen
eigenvalue = np.linalg.eig(M)
print(eigenvalue)

ev1 = eigenvalue.eigenvectors[:,0]
ev2 = eigenvalue.eigenvectors[:,-1]

ev2 = ev2 / np.sum(ev2)
print(ev2)



# print(M@ev2)
# print(ev2@M)
# print(f"Eigenvalues: {eigenvalue}")

