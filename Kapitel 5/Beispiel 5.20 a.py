import numpy as np

M = np.array([[2, 3],
              [-1, 6]], dtype=np.float64)


# eigen
eigvals = np.linalg.eigvals(M)
print(eigvals)
eigval = eigvals[0]  # Take the first eigenvalue
print(eigval)

diag = np.diag(np.full(2,1)) 
print(diag)
N = M-eigval * diag
print(N)

# solve the system
# b = np.array([0, 0], dtype=np.float64)
# x = np.linalg.solve(N, b)
# print(x)

# Upps, the matrix is singular, so we cannot solve it directly.
# We can find the eigenvector corresponding to the eigenvalue.
# We can use the null space to find the eigenvector.
null_space = np.linalg.svd(N)[2][-1]
print(null_space)
null_space = null_space / np.linalg.norm(null_space)  # Normalize the eigenvector
print(null_space)

null_space = null_space / null_space[1]
print(null_space)

# Der Eigenraum ist ein Raum. Es gibt also nicht nur eine Lösung, sondern unendlich viele.
# Ist eine gute Frage, wie überhaupt eine Lösung aussehen sollte, die ganzzahlige Werte hat.


# ev1 = eigenvalue.eigenvectors[:0]
# ev2 = eigenvalue.eigenvectors[:,-1]

# ev2 = ev2 / np.sum(ev2)
# print(ev2)



# print(M@ev2)
# print(ev2@M)
# print(f"Eigenvalues: {eigenvalue}")

