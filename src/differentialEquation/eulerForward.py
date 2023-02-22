import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import time 



def mainEulerForward(symbolic_function_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , vars_start: list[float], t_start: float, t_end: float,h : float):
    list_result_t = []
    list_result_vars = []
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_function_system]
    vars_iterate = vars_start.copy()
    t_iterate = t_start
    list_result_t.append(t_iterate)
    list_result_vars.append(vars_iterate)
    while t_iterate < t_end:
        equation_system_values = [equation((vars_iterate),t_iterate) for equation in lamdified_equation_system]
        vars_iterate = np.add(vars_iterate, np.multiply(h,equation_system_values)) # var = var + h * d(var)/dt 
        t_iterate = t_iterate + h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)
    return list_result_t,list_result_vars
