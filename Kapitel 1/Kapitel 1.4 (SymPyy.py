
import sympy as sp

A = sp.Matrix([[1,1,1],
               [2,2,1],
               [-4,5,6]])
b = sp.Matrix([1,-3, 1])


print(A.det())
print(A.gauss_jordan_solve(b))  # Solve using Gauss-Jordan elimination
print(A.inv() * b)  # algebraische Lösung

Ab = A.row_join(b)
print(Ab.LUdecomposition())  # LU decomposition of the augmented matrix
print(Ab.rref())  # Reduced row echelon form of the augmented matrix
