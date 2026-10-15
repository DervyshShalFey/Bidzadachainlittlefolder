from transformation import *
from math import *
try:
    x = float(input('Insert 1st number: '))
    y = float(input('Insert 2nd number: '))
    x = transform(x)
    y = transform(y)
    print(f'A) y = 7(x^2) - 3x + 6 \n   If x is equal to {x}, then y will be equal to {transform(7*(x**2)-3*x+6)}')
except ValueError:
    print('Not a number!')