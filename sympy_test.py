
from sympy import solve, Symbol
from sympy.abc import x
import numpy as np
a = 1
b = -1 
c=4

print(solve(a*x**2+b*x+c))
print(np.roots([a,b,c]))