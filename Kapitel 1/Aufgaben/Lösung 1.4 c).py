
import numpy as np

"""
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


# Lösung in Teilschritten

# Rückwärts-Elimination

# Rückwärts-Elimination in der 3. Spalte 

# Aufgabe 1: Rückwärts-Elimination der -5 an der Stelle [1,2]
Ab[1,:] = Ab[1,:] - Ab[1,2]/ Ab[2,2] * Ab[2,:]

assert np.isclose(Ab[1,2], 0), "Die -5 an der Stelle [1,2] sollte eliminiert sein."

# Aufgabe 2: Rückwärts-Elimination der 2 an der Stelle [0,2]
Ab[0,:] = Ab[0,:] - Ab[0,2] / Ab[2,2] * Ab[2,:]

assert np.isclose(Ab[0,2], 0), "Die 2 an der Stelle [0,2] sollte eliminiert sein"

# Aufgabe 3: Rückwärts-Elimination der 4 an der Stelle [0,1]
Ab[0,:] = Ab[0,:] - Ab[0,1] / Ab[1,1] * Ab[1,:]

assert np.isclose(Ab[0,1], 0), "Die 4 an der Stelle [0,1] sollte eliminiert sein."

# Aufgabe 4: Normalisiere alle Zeilen, sodass die Diagonaleinträge 1 sind
for i in range(rows):
    Ab[i,:] = Ab[i,:] / Ab[i,i]

assert np.allclose(Ab[:,0:3], np.eye(3)), "Die Diagonaleinträge sollten 1 sein und alle anderen Einträge 0."


# Aufgabe 5: Gib die Lösung als Vektor aus
print(Ab[:, -1])  # Last column contains the solutions




