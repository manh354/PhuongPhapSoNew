import numpy as np
import sympy as sp


def CustomPredictorCorrectorOneIteration(predictor, corrector,lamdified_equation_system,vars_iterate, t_iterate,h, EPS, ITR_MAX):
    vars_iterate_predicted = predictor(lamdified_equation_system,vars_iterate,t_iterate,h)
    vars_iterate_corrected = corrector(lamdified_equation_system,vars_iterate_predicted,t_iterate,h, EPS, ITR_MAX)
    return vars_iterate_predicted,vars_iterate_corrected


def CustomPredictorCorrector(predictor, corrector,symbolic_function_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , vars_start: list[float], t_start: float, t_end: float,h : float, EPS: float, ITR_MAX:int):
    list_result_t = []
    list_result_vars_predicted = []
    list_result_vars_corrected = []
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_function_system]
    vars_iterate_corrected = vars_start.copy()
    t_iterate = t_start
    list_result_t.append(t_iterate)
    list_result_vars_predicted.append(vars_iterate_corrected)
    list_result_vars_corrected.append(vars_iterate_corrected)
    while t_iterate < t_end:
        vars_iterate_predicted,vars_iterate_corrected = CustomPredictorCorrectorOneIteration(predictor,corrector,lamdified_equation_system,vars_iterate_corrected,t_iterate,h,EPS,ITR_MAX)
        t_iterate += h
        list_result_t.append(t_iterate)
        list_result_vars_predicted.append(vars_iterate_predicted)
        list_result_vars_corrected.append(vars_iterate_corrected)
    return list_result_t, list_result_vars_predicted, list_result_vars_corrected

def getCustomPredictorCorrector (predictor, corrector):
    return lambda symbolic_function_system , symbolic_vars , symbolic_t , vars_start, t_start, t_end,h , EPS, ITR_MAX : CustomPredictorCorrector(predictor,corrector,symbolic_function_system,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h,EPS,ITR_MAX)