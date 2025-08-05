import numpy as np

gl= np.array([[1,1,2,6],
              [3,3,-1,11],
              [1,2,-4,2]], dtype=np.float64)

# dimension
print(gl.shape)
print(gl.shape[0])  # number of rows
print(gl.shape[1])  # number of columns

# Forward elimination für 3x3 matrix
for pivot_row in range(0, 3):
    for row in range(pivot_row+1, 3):
        factor = gl[row,pivot_row]/gl[pivot_row,pivot_row]
        gl[row,:] = gl[row,:] - factor * gl[pivot_row,:]
    
print(gl)
for pivot_row in range(2, -1, -1):
    gl[pivot_row,:] = gl[pivot_row,:] / gl[pivot_row,pivot_row]
    for row in range(pivot_row-1, -1, -1):
        factor = gl[row,pivot_row]/gl[pivot_row,pivot_row]
        gl[row,:] = gl[row,:] - factor * gl[pivot_row,:]

    if gl[pivot_row,pivot_row] == 0:
        # Handle zero pivot replace row with a non-zero row
        for row in range(pivot_row+1, 3):
            if gl[row,pivot_row] != 0:
                # Zeile r und row tauschen
                gl[[pivot_row, row], :] = gl[[row, pivot_row], :]
                break
