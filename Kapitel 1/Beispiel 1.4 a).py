"""
Matrix in Python using a list of lists, access its elements, and compute its shape.
"""

# Matrix
Ab = [  [  2,  4,  2, 60],
        [  7,  6,  2,122],
        [ 12, 22, 11,342]]
print(Ab)

# Accessing elements
print(Ab[1][3])  # Accessing the element in the second row and fourth column

# Computing the shape of the matrix
rows = len(Ab)
cols = len(Ab[0])
print(f"Number of rows: {rows}, Number of columns: {cols}")

# Slicing the matrix
print(Ab[1:3])  # Slicing rows 1 to 2 (0-indexed)
print(Ab[1:])