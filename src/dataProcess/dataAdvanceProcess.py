# Use for these purpose :
# - Newton fixed-p
# oint iteration of interpolation polynomials : find all usable segments
import sympy as sp

def getLamdifiedFunction(string, symbol_params, symbol_var):
    return sp.lambdify((symbol_var,[*symbol_params]),string, 'numpy')