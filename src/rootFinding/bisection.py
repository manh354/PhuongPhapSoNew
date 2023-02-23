import numpy as np
import sympy as sp


# Use bisection method to find roots
def mainBisection(left, right, func, var, eps):
    if(func is str):
        func = sp.lambdify(var, func, 'numpy')
    i = 0
    while (right-left)>=eps:
        middle = (left + right)/2
        f_mid = func(middle)
        f_right = func(right)
        if(f_mid * f_right > 0):
            right = middle
        else: 
            left = middle
        i += 1
    return middle