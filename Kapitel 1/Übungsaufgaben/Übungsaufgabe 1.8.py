import numpy as np

Ab=np.array([
    [0,0,1,1,300],
    [0,1,1,0,200],
    [1,0,0,1,600],
    [1,1,0,0,500]])

print(np.linalg.solve(Ab[:,:-1], Ab[:,-1]))
