import matplotlib.pyplot as plt
from .customPredictorCorrector import getCustomPredictorCorrector
from .adamsBashfort import getAdamsBashfortMethod
import numpy as np

def deSolveAndDraw2D(func, deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h):
    list_result_t , list_result_var = func(deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h)
    array_of_result = np.array(list_result_var).T
    variables_count = len(symbolic_vars)
    fig, ax = plt.subplots(1,variables_count+1)
    fig.set_size_inches(4*(variables_count+1),4)
    ax[0].plot(*array_of_result)
    for i in range(1,variables_count+1) :
        ax[i].plot(list_result_t,array_of_result[i-1])
    return list_result_t, list_result_var

def deSolveAdamsBashfortAndDraw2D(number_of_points,deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h):
    func = getAdamsBashfortMethod(number_of_points)
    list_result_t , list_result_var = func(deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h)
    array_of_result = np.array(list_result_var).T
    variables_count = len(symbolic_vars)
    fig, ax = plt.subplots(1,variables_count+1)
    fig.set_size_inches(4*(variables_count+1),4)
    ax[0].plot(*array_of_result)
    for i in range(1,variables_count+1) :
        ax[i].plot(list_result_t,array_of_result[i-1])
    return list_result_t, list_result_var

def deSolvePCAndDraw2D(predictor, corrector,deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h,EPS, ITR_MAX):
    func = getCustomPredictorCorrector(predictor,corrector)
    list_result_t , list_result_vars_predicted, list_result_vars_corrected = func(deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h,EPS,ITR_MAX)
    array_of_result_predicted = np.array(list_result_vars_predicted).T
    array_of_result_corrected = np.array(list_result_vars_corrected).T
    variables_count = len(symbolic_vars)
    fig, ax = plt.subplots(2,variables_count+1)
    fig.set_size_inches(4*(variables_count+1),4)
    ax[0].plot(*array_of_result_predicted)
    ax[0].plot(*array_of_result_corrected)
    for i in range(1,variables_count+1) :
        ax[0,i].plot(list_result_t,array_of_result_predicted[i-1], color = 'orange')
        ax[0,i].plot(list_result_t,array_of_result_corrected[i-1], color = 'green')
    for i in range(1,variables_count+1) :
        ax[1,0].plot(list_result_t, np.abs(np.subtract(array_of_result_corrected[i-1],array_of_result_predicted[i-1])), color = 'red')
    return list_result_t, list_result_vars_predicted, list_result_vars_corrected