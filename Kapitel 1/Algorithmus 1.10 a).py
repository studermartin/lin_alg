import numpy as np

gl= np.array([[1,1,2,6],
              [3,3,-1,11],
              [1,2,-4,2]], dtype=np.float64)

# dimension
rows = gl.shape[0]  # number of rows
cols = gl.shape[1]  # number of columns

# Forward elimination für 3x3 matrix
for pivot_row in range(0, 3):
    for row in range(pivot_row+1, 3):
        factor = gl[row,pivot_row]/gl[pivot_row,pivot_row]
        gl[row,:] = gl[row,:] - factor * gl[pivot_row,:]
    
# Forward elimination for nxn matrix
for pivot_row in range(0, rows):
    for row in range(pivot_row+1, rows):
        factor = gl[row,pivot_row]/gl[pivot_row,pivot_row]
        gl[row,:] = gl[row,:] - factor * gl[pivot_row,:]

# Swapping rows if pivot is zero
for pivot_row in range(0, rows):
    if gl[pivot_row,pivot_row] == 0:
        for row in range(pivot_row+1, 3):
            if gl[row,pivot_row] != 0:
                # Zeile r und row tauschen
                gl[[pivot_row, row], :] = gl[[row, pivot_row], :]
                break
        assert False, "no row with non-zero pivot found."
    # Forward elimination
    for row in range(pivot_row+1, rows):
        factor = gl[row,pivot_row]/gl[pivot_row,pivot_row]
        gl[row,:] = gl[row,:] - factor * gl[pivot_row,:]

