import matplotlib.pyplot as plt
from .customPredictorCorrector import getCustomPredictorCorrector
from .adamsBashforth import getAdamsBashforthMethod
from .adamsMoulton import getAdamsMoultonMethod
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

def deSolveABAndDraw2D(number_of_points,deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h):
    func = getAdamsBashforthMethod(number_of_points)
    list_result_t , list_result_var = func(deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h)
    array_of_result = np.array(list_result_var).T
    variables_count = len(symbolic_vars)
    fig, ax = plt.subplots(1,variables_count+1)
    fig.set_size_inches(4*(variables_count+1),4)
    ax[0].plot(*array_of_result)
    for i in range(1,variables_count+1) :
        ax[i].plot(list_result_t,array_of_result[i-1])
    return list_result_t, list_result_var

def deSolveAMAndDraw2D(number_of_points,deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h):
    func = getAdamsMoultonMethod(number_of_points)
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
    ax[0,0].plot(*array_of_result_predicted, color = 'orange')
    ax[0,0].plot(*array_of_result_corrected, color = 'green')
    ax[1,0].plot(*np.subtract(array_of_result_corrected,array_of_result_predicted), color = 'red')
    for i in range(1,variables_count+1) :
        ax[0,i].plot(list_result_t,array_of_result_predicted[i-1], color = 'orange')
        ax[0,i].plot(list_result_t,array_of_result_corrected[i-1], color = 'green')
    for i in range(1,variables_count+1) :
        ax[1,i].plot(list_result_t, np.abs(np.subtract(array_of_result_corrected[i-1],array_of_result_predicted[i-1])), color = 'red')
    return list_result_t, list_result_vars_predicted, list_result_vars_corrected


def deSolveAndDraw2DMultipleFunc(funcs:list,deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h):
    list_result_t_s = []
    list_result_var_s = []
    for func in funcs:
        list_result_t , list_result_var = func(deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h)
        list_result_t_s .append(list_result_t)
        list_result_var_s.append(list_result_var)
    array_of_result_s = [np.array(list_result_var).T for list_result_var in list_result_var_s]
    variables_count = len(symbolic_vars)
    fig, ax = plt.subplots(len(funcs),variables_count+1)
    fig.set_size_inches(4*(variables_count+1),len(funcs)*4)
    for i,array_of_result in enumerate(array_of_result_s):
        ax[i,0].plot(*array_of_result)
        for j in range(1,variables_count+1) :
            ax[i,j].plot(list_result_t,array_of_result[j-1])
    return list_result_t_s, list_result_var_s