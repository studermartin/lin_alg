"""
Matrix in Python using NumPy.
"""

import numpy as np

Ab = np.array([ [  2,  4,  2, 60],
                [  7,  6,  2,122],
                [ 12, 22, 11,342]]
                , dtype=np.float64)  
print(Ab)

# Accessing elements
print(Ab[1,3])

# Computing the shape of the matrix
print(Ab.shape)
print(Ab.shape[0])  # number of rows
print(Ab.shape[1])  # number of columns

"""
Gaussian elimination
"""

# Part 1: Forward elimination

# Part 1.1: Eliminate  element 7 in the first column and second row

# (ii)=(ii)-7/2*(i)
Ab[1,0]= Ab[1,0] - 7/2 * Ab[0,0]
Ab[1,1]= Ab[1,1] - 7/2 * Ab[0,1]
Ab[1,2]= Ab[1,2] - 7/2 * Ab[0,2]
Ab[1,3]= Ab[1,3] - 7/2 * Ab[0,3]
print(Ab)

# Using for in-loop
for col in range(0, 4):
    Ab[1,col]= Ab[1,col] - 7/2 * Ab[0,col]
print(Ab)

# Compute factor
factor = Ab[1,0]/Ab[0,0]
for col in range(0, 4):
    Ab[1,col]= Ab[1,col] - factor * Ab[0,col]
print(Ab)

# Compute with rows
# (ii)=(ii)-7/2*(i)
factor = Ab[1,0]/Ab[0,0]
Ab[1,0:4] = Ab[1,0:4] - factor * Ab[0,0:4]
print(Ab)

# Shortcut: 0:4 means all columns
# (ii)=(ii)-7/2*(i)
factor = Ab[1,0]/Ab[0,0]
Ab[1,:] = Ab[1,:] - factor * Ab[0,:]
print(Ab)

# Shortcut: include factor in the loop
Ab[1,:] = Ab[1,:] - Ab[1,0]/Ab[0,0] * Ab[0,:]
print(Ab)

# Part 1.2: Eliminate element 12 in the first column and third row
Ab[2,:] = Ab[2,:] - Ab[2,0]/Ab[0,0] * Ab[0,:]
print(Ab)

# Part 1.3: Summary of forward elimination of first column
Ab = np.array([ [  2,  4,  2, 60],
                [  7,  6,  2,122],
                [ 12, 22, 11,342]]
                , dtype=np.float64)  

for row in range(1, 3):
    Ab[row,:] = Ab[row,:] - Ab[row,0]/Ab[0,0] * Ab[0,:]

# Part 1.4: Eliminate elements in the second column
for row in range(2, 3):
    Ab[row,:] = Ab[row,:] - Ab[row,1]/Ab[1,1] * Ab[1,:]
print(Ab)


# Part 1.4: Putting it all together
Ab = np.array([ [  2,  4,  2, 60],
                [  7,  6,  2,122],
                [ 12, 22, 11,342]]
                , dtype=np.float64)  
for pivot_row in range(0, 2):
    for row in range(pivot_row + 1, 3):
        Ab[row,:] = Ab[row,:] - Ab[row,pivot_row]/Ab[pivot_row,pivot_row] * Ab[pivot_row,:]
print(Ab)
