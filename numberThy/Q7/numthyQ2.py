import numpy as np
import math
import random

# this function returns the Jacobi symbol (a/p)

def Jacobi(a, p):
    if p % 2 == 0 or p <= 0:
        raise ValueError("'p' must be an odd prime")
    a %= p
    Jacobi_sym = 1
    while a != 0:
        while a % 2 == 0:   # this while loop ensures that a is odd now
            a /= 2
            pmod8 = p % 8
            if pmod8 == 3 or pmod8 == 5:
                Jacobi_sym = -Jacobi_sym  
        a, p = p, a
        if a % 4 == 3 and p % 4 == 3:  # this uses the law of quadratic reciprocity for Jacobi symbol
            Jacobi_sym = -Jacobi_sym
        a %= p
    if p == 1:
        return Jacobi_sym
    else:
        return 0
