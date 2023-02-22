import numpy as np
import sympy as sp

def mainTrapezoid(symbolic_equation_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , vars_start: list[float], t_start: float, t_end: float,h : float):
    list_result_t = []
    list_result_vars = []
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_equation_system]
    vars_iterate = vars_start.copy()
    t_iterate = t_start
    list_result_t.append(t_iterate)
    list_result_vars.append(vars_iterate)
    while t_iterate < t_end:
        vars_iterate = fixedpointIteration(lamdified_equation_system,vars_iterate, t_iterate,h, 1e-9, 100)
        t_iterate = t_iterate + h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)
    return list_result_t,list_result_vars


def fixedpointIteration(lamdified_equation_system ,vars_start : list, t_start, h : float ,epsilon, terminate_threshold):
    vars_iterate = vars_start.copy()
    t_iterate = t_start + h
    equation_system_values_at_start = [equation((vars_start),t_start) for equation in lamdified_equation_system]
    equation_system_values_at_iterate = [equation((vars_iterate),t_iterate) for equation in lamdified_equation_system]
    vars_iterate_new = np.add(vars_start,np.multiply(0.5*h, np.add(equation_system_values_at_start,equation_system_values_at_iterate)))
    i = 1
    while (np.sum(np.abs(np.subtract(vars_iterate_new, vars_iterate))) >= epsilon) and (i < terminate_threshold):
        vars_iterate = vars_iterate_new.copy()
        equation_system_values_at_iterate = [equation((vars_iterate),t_iterate) for equation in lamdified_equation_system]
        vars_iterate_new = np.add(vars_start,np.multiply(0.5*h, np.add(equation_system_values_at_start,equation_system_values_at_iterate)))
        i += 1
    return vars_iterate_new