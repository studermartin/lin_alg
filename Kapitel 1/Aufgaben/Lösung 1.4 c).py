
import numpy as np

"""
Aufgabe 1.4 c)
Implementiere die Rückwärts-Elimination für die Matrix Ab aus Aufgabe 1.4 c)
und gib die Lösung des Gleichungssystems aus.
"""

Ab = np.array(
    [[ 2,  4,  2,  60],
     [ 0, -8, -5, -88],
     [ 0,  0,  1,  16]]
     , dtype=np.float64)

rows = Ab.shape[0]  # number of rows
cols = Ab.shape[1]  # number of columns


# Aufgabe 1: Lösung in Teilschritten

# Rückwärts-Elimination

# Rückwärts-Elimination in der 3. Spalte 

# Teilaufgabe a): Rückwärts-Elimination der -5 an der Stelle [1,2]
Ab[1,:] = Ab[1,:] - Ab[1,2]/ Ab[2,2] * Ab[2,:]

assert np.isclose(Ab[1,2], 0), "Die -5 an der Stelle [1,2] sollte eliminiert sein."

# Teilaufgabe b): Rückwärts-Elimination der 2 an der Stelle [0,2]
Ab[0,:] = Ab[0,:] - Ab[0,2] / Ab[2,2] * Ab[2,:]

assert np.isclose(Ab[0,2], 0), "Die 2 an der Stelle [0,2] sollte eliminiert sein"

# Teilaufgabe c): Rückwärts-Elimination der 4 an der Stelle [0,1]
Ab[0,:] = Ab[0,:] - Ab[0,1] / Ab[1,1] * Ab[1,:]

assert np.isclose(Ab[0,1], 0), "Die 4 an der Stelle [0,1] sollte eliminiert sein."

# Teilaufgabe d) Normalisiere alle Zeilen, sodass die Diagonaleinträge 1 sind
for i in range(rows):
    Ab[i,:] = Ab[i,:] / Ab[i,i]


# Aufgabe 2: Allgemeine Lösung
Ab = np.array(
    [[ 2,  4,  2,  60],
     [ 0, -8, -5, -88],
     [ 0,  0,  1,  16]]
     , dtype=np.float64)

rows = Ab.shape[0]  # number of rows
cols = Ab.shape[1]  # number of columns

# Teilaufgabe a): Nutze eine Schleife, um die Rückwärts-Elimination und die Normalisierung für alle Zeilen durchzuführen
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




