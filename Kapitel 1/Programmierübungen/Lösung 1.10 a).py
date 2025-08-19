import numpy as np

"""
Allgemeine Lösung
"""

Ab = np.array(
    [[ 2,  4,  2,  60],
     [ 0, -8, -5, -88],
     [ 0,  0,  1,  16]]
     , dtype=np.float64)

rows = Ab.shape[0]  # number of rows
cols = Ab.shape[1]  # number of columns

# Aufgabe 1 a): Nutze eine Schleife, um die Rückwärts-Elimination und die Normalisierung für alle Zeilen durchzuführen
for pivot_row in range(rows - 1, 0, -1):
    for row in range(pivot_row - 1, -1, -1):
        Ab[row,:] = Ab[row,:] - Ab[row,pivot_row] / Ab[pivot_row,pivot_row] * Ab[pivot_row,:]
for i in range(rows):
    Ab[i,:] = Ab[i,:] / Ab[i,i]


# Teilaufgabe b): Nutze die Variablen rows und cols, um die Schleifen zu steuern
for pivot_row in range(rows - 1, 0, -1):
    for row in range(pivot_row - 1, -1, -1):
        Ab[row,:] = Ab[row,:] - Ab[row,pivot_row] / Ab[pivot_row,pivot_row] * Ab[pivot_row,:]
for i in range(rows):
    Ab[i,:] = Ab[i,:] / Ab[i,i]


# Teilaufgabe c): Gib die Lösung als Vektor aus
print(Ab[:, -1])  # Last column contains the solutions
