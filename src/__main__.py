from dataInput.dataInput import readVertical
from dataProcess.dataProcess import findSegmentContainsRoot
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

dataX, dataY = readVertical()