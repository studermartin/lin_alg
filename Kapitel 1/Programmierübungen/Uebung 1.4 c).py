
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
# ---> Hier kommt dein Code
Ab[1] = Ab[1] + 5 * Ab[2]
print(Ab)

assert np.isclose(Ab[1,2], 0), "Die -5 an der Stelle [1,2] sollte eliminiert sein."

# Aufgabe 2 : Rückwärts-Elimination der 2 an der Stelle [0,2]
# ---> Hier kommt dein Code

assert np.isclose(Ab[0,2], 0), "Die 2 an der Stelle [0,2] sollte eliminiert sein"

# Aufgabe 3: Rückwärts-Elimination der 4 an der Stelle [0,1]
# ---> Hier kommt dein Code

assert np.isclose(Ab[0,1], 0), "Die 4 an der Stelle [0,1] sollte eliminiert sein."

# Aufgabe 4: Normalisiere alle Zeilen, sodass die Diagonaleinträge 1 sind
# ---> Hier kommt dein Code

assert np.isclose(Ab[0,1], 0), "Die 4 an der Stelle [0,1] sollte eliminiert sein."

# Aufgabe 5: Gib die Lösung als Vektor aus
# ---> Hier kommt dein Code
