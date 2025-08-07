import sympy as sp

A = sp.Matrix([
    [0,0,1,1],
    [0,1,1,0],
    [1,0,0,1],
    [1,1,0,0]])

b=sp.Matrix([
    [300],
    [200],
    [600],
    [500]])

print(sp.linsolve((A, b)))

