# NumPy: numerische Lösung
import numpy as np

A = np.array([
    [1, -1, -1],
    [4,  5,  0],
    [4,  0,  1]], dtype=np.float64)


b = np.array([0, 3, 2])

print(np.linalg.solve(A, b))

# SymPy: algebraische Lösung
import sympy as sp

A = sp.Matrix([
    [1, -1, -1],
    [4,  5,  0],
    [4,  0,  1]])

b = sp.Matrix([0, 3, 2])

print(A.inv() * b)  # algebraische Lösung