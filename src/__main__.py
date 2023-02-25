import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

from dataInput.dataInput import readVertical
from dataProcess.dataProcess import findSegmentContainsRoot
from dataProcess.dataAdvanceProcess import getLamdifiedFunction
from intergration.simpson import simpsonQuadraticGrid
# result, num_step = simpsonQuadraticGrid(equation, variable,a,b, 10, 5e-8)
# print("Kết quả cuối cùng thu được: {0} \tsau số bước: {1}".format(result,num_step))
from intergration.simpsonDiscrete import simpsonQuadraticDiscrete, halvesGrid
# error_limit = 1.0/3.0 * abs(integrated_result - integrated_result2)
# print("Đánh giá sai số nhỏ hơn: ", error_limit)
from dataSlicing.dataSlicingCenter import sliceInputFromCenterGauss1, sliceInputFromCenterGauss2,sliceInputFromCenterBessel,sliceInputFromCenterStirling
from dataSlicing.dataSlicingLangrange import sliceInputFromLeftToRight
from dataSlicing.dataSlicingNewton import sliceInputNewtonForward,sliceInputNewtonBackward
from interpolation.dataOutputCenter import output as outputDataCenter
from interpolation.dataOutputLangrange import output as outputDataLangrange
from interpolation.dataOutputNewton import outputAny as outputDataNewtonAny 
from interpolation.dataOutputNewton import outputEqui as outputDataNewtonEqui
from interpolation.gauss import wrapperGauss1, wrapperGauss2
from interpolation.langrange import wrapperLangrange
from interpolation.bessel import wrapperBesselNorm,wrapperBesselSkewed
from interpolation.newtonForward import wrapperNewtonForwardAny,wrapperNewtonForwardEqui
from interpolation.newtonBackward import wrapperNewtonBackwardAny, wrapperNewtonBackwardEqui
from interpolation.stirling import wrapperStirling
from leastSquare.leastSquare import wrapperLeastSquare as lqLeastSquare
from leastSquare.leastSquare import drawLeastSquare
# adjustable_parameters = sp.symbols("a c")
# independent_variable = sp.Symbol("x")
# test_function = "0"
# fitting_function = "a*x**2  + c"
# param_start = [1,1]
from reverseInterpolation.newtonFixedPointIteration import mainNewtonBackwardReverse, mainNewtonForwardReverse
from reverseInterpolation.reverseLangrange import mainReverseLangrange
from differentialEquation.eulerForward import mainEulerForward
from differentialEquation.eulerBackward import mainEulerBackward
from differentialEquation.trapezoid import mainTrapezoid
from differentialEquation.rungeKutta import mainRungeKutta2_Heun, mainRungaKutta3_Kutta, mainRungaKutta3_Heun, mainRungeKutta4_Classic
from differentialEquation.adamsBashfort import mainAdamsBashfort
from differentialEquation.adamsMoulton import mainAdamsMoulton
# t = sp.symbols('t') 
# 
# variables = sp.symbols("x y")
# deriv_equations = ["1.5*(1-x/20)*x - 0.5*x**2*y/(1+15*x**2)","-0.35*y+0.35*x**2*y/(1+15*x**2)"]
# groundtruth_equations=["-cos(t)","sin(t)"]
# vars_start = [6,4]
# t_start = 0
# t_end = 10
# h = 0.1
# Test = False

dataX, dataY = readVertical()
x = sp.Symbol("x")
simpsonQuadraticGrid(fitting)

#x,y,a,b = findSegmentContainsRoot(dataX, dataY, 0.90912)
#
#adjustable_parameters = sp.symbols("a c")
#independent_variable = sp.Symbol("x")
#fitting_function = str("a*x**2  + c")
#
#param_start = [1,1]
#
#i, param = lqLeastSquare(dataX,dataY,adjustable_parameters,independent_variable,fitting_function,param_start)
#fitting_function = getLamdifiedFunction(fitting_function, adjustable_parameters,independent_variable)
#drawLeastSquare(dataX,dataY,fitting_function,param)
