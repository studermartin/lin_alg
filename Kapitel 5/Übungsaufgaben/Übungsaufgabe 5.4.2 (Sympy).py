import sympy as sp

ev = sp.Matrix([[0  , 1  , 2  , 1.5],
                [0.5, 0  , 0  , 0  ],
                [0  , 0.7, 0  , 0  ],
                [0  , 0  , 0.6, 0  ]]).eigenvects()
print(ev)
