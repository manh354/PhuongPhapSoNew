import sympy as sp
import numpy as np

def FindM4OfFunc(func : sp.Function , var, segment_a: float,segment_b : float, alpha,epsilon,maxIteration):
    sp_4thDerivative = Find4thDerivative(func, var)
    return FindMaxOfFunc(sp_4thDerivative,var,segment_a,segment_b,alpha,epsilon,maxIteration)

def FindMaxOfFunc(func: sp.Function,var, segment_a: float,segment_b : float, alpha,epsilon,maxIteration):
    diff_func = sp.diff(func)
    grad_xval, grad_yval = GradientDescent(func,diff_func,var,segment_a,segment_b,alpha,epsilon,maxIteration)
    all_yvals = [float(func.subs(var,segment_a)),float(func.subs(var,segment_b)), grad_yval]  
    return abs(max(all_yvals))

def Find4thDerivative(func : sp.Function, var):
    sp_func = sp.diff(func,var)
    sp_func = sp.diff(sp_func,var)
    sp_func = sp.diff(sp_func,var)
    sp_func = sp.diff(sp_func,var)
    return sp_func

def GradientDescent(func : sp.Function, diff_func : sp.Function,var, segment_a: float, segment_b:float, alpha : float,epsilon: float, maxIteration: int):
    startpos = (segment_a+segment_b)/2
    x = startpos
    ld_func = sp.lambdify(var, func,"numpy")
    ld_diff_func = sp.lambdify(var, diff_func, "numpy" )
    for i in range(0,maxIteration):
        xnew = x + float(alpha*ld_diff_func(x))
        if(xnew > segment_b ):
            return segment_b, float(ld_func(segment_b))
        if(xnew < segment_a):
            return segment_a, float(ld_func(segment_a))
        if(abs(xnew-x) < epsilon):
            return xnew,float(ld_func(xnew))
        x = xnew
    return x, float(func.subs(var,xnew))

def main(func, var, eps0 : float ,segment_a: float, segment_b : float, alpha: float, epsilon : float, gradDescentIter : int):
    m4 = FindM4OfFunc(func,var,segment_a,segment_b, alpha, epsilon,gradDescentIter)
    print("M4 = {}".format(m4))
    step = eps0 / (m4/180*(segment_b-segment_a))
    return np.power(step,0.25)
