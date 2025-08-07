import numpy as np

A = np.array([
    [0,0,1,1],
    [0,1,1,0],
    [1,0,0,1],
    [1,1,0,0]])

b=np.array([
    [300],
    [200],
    [600],
    [500]])

# Fehlermeldung weil es sich um eine singuläre Matrix handelt
# print(np.linalg.solve(A, b))

# Determinante ist 0, also singuläre Matrix
print(np.linalg.det(A))

# Mit der Methode least squares erhält man eine mögliche Lösung
# (aber nicht die einzige, da die Matrix singulär ist)
print(np.linalg.lstsq(A, b))
