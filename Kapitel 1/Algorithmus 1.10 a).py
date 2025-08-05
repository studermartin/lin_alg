import numpy as np

Ab= np.array([[1,1,2,6],
              [3,3,-1,11],
              [1,2,-4,2]], dtype=np.float64)

# dimension
rows = Ab.shape[0]  # number of rows
cols = Ab.shape[1]  # number of columns

# Forward elimination für 3x3 matrix
# for pivot_row in range(0, 3):
#     for row in range(pivot_row+1, 3):
#         factor = Ab[row,pivot_row]/Ab[pivot_row,pivot_row]
#         Ab[row,:] = Ab[row,:] - factor * Ab[pivot_row,:]
    
# Forward elimination for nxn matrix
# for pivot_row in range(0, rows):
#     for row in range(pivot_row+1, rows):
#         factor = Ab[row,pivot_row]/Ab[pivot_row,pivot_row]
#         Ab[row,:] = Ab[row,:] - factor * Ab[pivot_row,:]

# Swapping rows if pivot is zero
for pivot_row in range(0, rows):
    if Ab[pivot_row,pivot_row] == 0:
        for row in range(pivot_row+1, 3):
            if Ab[row,pivot_row] != 0:
                # Zeile r und row tauschen
                Ab[[pivot_row, row], :] = Ab[[row, pivot_row], :]
                break
    if Ab[pivot_row,pivot_row] == 0:
        assert False, "no row with non-zero pivot found."
    # Forward elimination
    for row in range(pivot_row+1, rows):
        factor = Ab[row,pivot_row]/Ab[pivot_row,pivot_row]
        Ab[row,:] = Ab[row,:] - factor * Ab[pivot_row,:]

print(Ab)