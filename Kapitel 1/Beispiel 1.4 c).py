import numpy as np

Ab = np.array([ [  2,  4,  2, 60],
                [  7,  6,  2,122],
                [ 12, 22, 11,342]]
                , dtype=np.float64)  

rows = Ab.shape[0]  # number of rows
cols = Ab.shape[1]  # number of columns
for pivot_row in range(0, rows-1):
    for row in range(pivot_row + 1, rows):
        Ab[row,:] = Ab[row,:] - Ab[row,pivot_row]/Ab[pivot_row,pivot_row] * Ab[pivot_row,:]
print(Ab)

# Part 1.5: Normalize the last row
Ab[2,:]=Ab[2,:]/Ab[2,2]
print(Ab)
