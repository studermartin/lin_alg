
# NumPy: numerische Lösung
import numpy as np

Ab=np.array([
    [0.85,0.75,0.60,0.70],
    [0.10,0.15,0.20,0.16],
    [0.05,0.10,0.20,0.14]])

A = np.array([
    [0.85,0.75,0.60],
    [0.10,0.15,0.20],
    [0.05,0.10,0.20]])


b = np.array([0.70, 0.16, 0.14])

print(np.linalg.solve(A, b))


# SymPy: algebraische Lösung
import sympy as sp

A = sp.Matrix([
    [0.85,0.75,0.60],
    [0.10,0.15,0.20],
    [0.05,0.10,0.20]])

b = sp.Matrix([0.70, 0.16, 0.14])

print(A.solve(b))
# Erstaunlicherweise eine numerische Lösung ?!

print(A.inv() * b)  # algebraische Lösung