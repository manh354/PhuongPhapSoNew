import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

from dataInput.dataInput import readVertical
from dataProcess.dataProcess import findSegmentContainsRoot, findNewtonFixedPointSegments, findReverseLangrangeSegments
from dataProcess.dataAdvanceProcess import getLamdifiedFunction
from intergration.simpson import simpsonQuadraticGrid
# result, num_step = simpsonQuadraticGrid(equation, variable,a,b, 10, 5e-8)
# print("Kết quả cuối cùng thu được: {0} \tsau số bước: {1}".format(result,num_step))
from intergration.simpsonDiscrete import simpsonQuadraticDiscrete, halvesGrid
# error_limit = 1.0/15.0 * abs(resultH - result2H)
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
# Spline
from interpolation.spline import mainNaturalCubicSpline, plotCubicSpline,getCubicSpline
from leastSquare.leastSquare import wrapperLeastSquare as lqLeastSquare
from leastSquare.leastSquare import drawLeastSquare
# adjustable_parameters = sp.symbols("a c")
# independent_variable = sp.Symbol("x")
# test_function = "0"
# fitting_function = "a*x**2  + c"
# param_start = [1,1]
from reverseInterpolation.newtonFixedPointIteration import mainNewtonBackwardReverse, mainNewtonForwardReverse
from reverseInterpolation.reverseLangrange import wrapperReverseLangrange

from differentialEquation.eulerForward import deEulerForward , eulerForwardPredictor
from differentialEquation.eulerBackward import deEulerBackward, eulerBackwardCorrector
from differentialEquation.trapezoid import deTrapezoid, trapezoidCorrector
from differentialEquation.rungeKutta import deRungeKutta2_Heun, deRungaKutta3_Kutta, deRungaKutta3_Heun, deRungeKutta4_Classic
from differentialEquation.adamsBashfort import deAdamsBashfort, adamsBashfortPredictor
from differentialEquation.adamsMoulton import deAdamsMoulton
from differentialEquation.solutionDrawer import deSolveAndDraw2D, deSolveAdamsBashfortAndDraw2D, deSolvePCAndDraw2D


dataX, dataY = readVertical()

symbolic_t = sp.symbols('x') 
symbolic_vars = sp.symbols("y")
if(isinstance(symbolic_vars, sp.Symbol)):
    symbolic_vars = [symbolic_vars]
deriv_equations = ["1.5*(1-x/20)*x - 0.5*x**2*y/(1+15*x**2)"]
vars_start = [6]
t_start = 0
t_end = 10
h = 0.1

equation = "1/(1+x**2)"
var = sp.Symbol('x')
start = 0
end = 3
num_step =2
eps = 0.0000001

results = simpsonQuadraticGrid(equation,var, start, end, num_step,eps)
for i,result in enumerate(results):
    print("Số lượng khoảng grid {0}: {1}, giá trị: {2}".format(i,result[1], result[0]))
diffs = np.diff(results)
errors = np.multiply(1/15,np.abs(diffs))
for i, diffs in enumerate(diffs):
    print("Sai số grid {0}, giá trị {1}".format())

''' PP giải nhiều bước PTVP'''

#i_to_print = [1,2,3,-1,-2,-3]
#list_result_t, list_result_vars = deSolveAdamsBashfortAndDraw2D(4,deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h)
#for i in i_to_print:
#    print("t {0}: ".format(i) + " ; ".join("{} = {}".format(*s) for s in zip(symbolic_vars,list_result_vars[i])))
#plt.show()

''' PP giải 1 bước PTVP'''
#i_to_print = [1,2,3,-1,-2,-3]
#list_result_t, list_result_vars = deSolveAndDraw2D(deEulerBackward,deriv_equations,symbolic_vars,symbolic_t,vars_start,t_start,t_end,h)
#for i in i_to_print:
#    print("t {0}: ".format(i) + " ; ".join("{} = {}".format(*s) for s in zip(symbolic_vars,list_result_vars[i])))
#plt.show()
''' SPLINE bậc 3'''
#all_splines = mainNaturalCubicSpline(dataX,dataY)
#for i, spline_coefs in enumerate(all_splines):
#    output = "spline số {0}, Hệ số: {1} \nĐiểm bắt đầu: {2}, điểm kết thúc {3}".format(i, spline_coefs, dataX[i], dataX[i+1] )
#    print(output)
#plotCubicSpline(dataX, dataY, all_splines)

''' LEASTSQUARE '''
#adjustable_parameters = sp.symbols("a b c d")
#independent_variable = sp.Symbol('x')
#fitting_function = "a*x**3 + b*x**2 + c*x**1 + d"
#param_start = [0,0,0,0]
#
#i, result = lqLeastSquare(dataX,dataY,adjustable_parameters,independent_variable, fitting_function, param_start)
#fitting_function = getLamdifiedFunction(fitting_function, adjustable_parameters,independent_variable)
#drawLeastSquare(dataX,dataY,fitting_function,result)

''' SIMPSON hàm biết trước '''
#equation = "1/(1+x**2)"
#var = sp.Symbol('x')
#start = 0
#end = 3
#num_step =2
#eps = 0.0000001
#
#results = simpsonQuadraticGrid(equation,var, start, end, num_step,eps)
#for i,result in enumerate(results):
#    print("Số lượng khoảng grid {0}: {1}, giá trị: {2}".format(i,result[1], result[0]))
#diff = np.diff()
''' SIMPSON hàm không biết trước, đánh giá sai số'''
#resultH = simpsonQuadraticDiscrete(dataX[1]-dataX[0],dataY,len(dataX)-1)
#dataY2H = halvesGrid(dataY)
#result2H = simpsonQuadraticDiscrete(dataX[2]-dataX[0], dataY2H, len(dataY2H)-1)
#error_limit = 1.0/15.0 * abs(resultH - result2H)
#print("Giá trị tích phân: {0}, sai số nhỏ hơn {1}: ".format(resultH, error_limit))

''' Nội suy ngược LAGRANGE '''
#all_segments = findReverseLangrangeSegments(dataX,dataY,0.91106,7)
#for segment_x, segment_y in all_segments:
#    wrapperReverseLangrange(segment_x,segment_y,0.91106)

''' Nội suy ngược lặp NEWTON'''
#forward, backward = findNewtonFixedPointSegments(dataX,dataY,0.91106)
#result = []
#for X,Y in forward:
#    result.append(mainNewtonForwardReverse(X, Y, 0.91106, 0.00001))
#for i,(solanlap, hoituhaykhong, t,x) in enumerate(result):
#    print("Đoạn số {0}, số lần lặp: {1}, hội tụ: {2}, t = {3}, x = {4}".format(i,solanlap,hoituhaykhong,t,x))
#wrapperGauss1(dataX,dataY,1.43)

''' BÌNH PHƯƠNG TỐI THIỂU LeastSquare xử lý phức tạp'''
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
