import sympy as sp

ev = sp.Matrix([[0.99, 0.5], [0.01, 0.5]]).eigenvects()
print(ev)
