import numpy as np

"""
Allgemeine Lösung mit Rückwärts-Elimination und Zeilenvertauschung
"""

Ab = np.array(
    [[ 2,  4,  2,  60],
     [ 0, -8, -5, -88],
     [ 0,  0,  1,  16]]
     , dtype=np.float64)

rows = Ab.shape[0]  # number of rows
cols = Ab.shape[1]  # number of columns


# Aufgabe 1: Lösung mit Rückwärts-Elimination und Zeilenvertauschung

# Forward elimination
for pivot_row in range(0, rows):
    # Check if pivot is zero, if so, swap with a non-zero row
    if Ab[pivot_row,pivot_row] == 0:
        for row in range(pivot_row+1, 3):
            if Ab[row,pivot_row] != 0:
                # Zeile r und row tauschen
                Ab[[pivot_row, row], :] = Ab[[row, pivot_row], :]
                break
        assert False, "no row with non-zero pivot found."
    # Forward elimination
    for row in range(pivot_row+1, rows):
        factor = Ab[row,pivot_row]/Ab[pivot_row,pivot_row]
        Ab[row,:] = Ab[row,:] - factor * Ab[pivot_row,:]

# Backward elimination
for pivot_row in range(rows-1, -1, -1):
    for row in range(pivot_row-1, -1, -1):
        factor = Ab[row,pivot_row]/Ab[pivot_row,pivot_row]
        Ab[row,:] = Ab[row,:] - factor * Ab[pivot_row,:]
    Ab[pivot_row,:] = Ab[pivot_row,:] / Ab[pivot_row,pivot_row]


print(Ab[:, -1])  # Last column contains the solutions
