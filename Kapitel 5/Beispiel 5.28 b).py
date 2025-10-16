import sympy as sp

ev = sp.Matrix([[3,  3,  3],
                [0, -3, -6],
                [0, -3,  0]]).eigenvects()
print(ev)
