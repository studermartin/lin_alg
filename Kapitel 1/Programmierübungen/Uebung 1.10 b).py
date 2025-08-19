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
# ---> Hier kommt dein Code


print(Ab[:, -1])  # Last column contains the solutions


# Aufgabe 2: Lösung als Funktion verpacken
def solve_linear_system(Ab):
    # ---> Hier kommt dein Code
    pass
