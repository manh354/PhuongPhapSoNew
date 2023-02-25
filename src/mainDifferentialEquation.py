from differentialEquation.eulerForward import deEulerForward
from differentialEquation.eulerBackward import deEulerBackward
from differentialEquation.trapezoid import deTrapezoid
from differentialEquation.rungeKutta import deRungeKutta4_Classic, deRungaKutta3_Heun, deRungaKutta3_Kutta, deRungeKutta2_Heun
from differentialEquation.adamsBashfort import deAdamsBashfort
from differentialEquation.adamsMoulton import deAdamsMoulton
from differentialEquation.adamsPredictorCorrector import mainAdamsPredictorCorrector
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t') 

variables = sp.symbols("x y")
deriv_equations = ["1.5*(1-x/20)*x - 0.5*x**2*y/(1+15*x**2)","-0.35*y+0.35*x**2*y/(1+15*x**2)"]
groundtruth_equations=["-cos(t)","sin(t)"]
vars_start = [6,4]
t_start = 0
t_end = 10
h = 0.1
Test = False


def main2D(func):
    if(func == deAdamsBashfort or func == mainAdamsPredictorCorrector or func == deAdamsMoulton):
        list_result_t , list_result_var = func(7,deriv_equations,variables,t,vars_start,t_start,t_end,h)
    else: 
        list_result_t , list_result_var = func(deriv_equations,variables,t,vars_start,t_start,t_end,h)
    array_of_result = np.array(list_result_var).T
    variables_count = len(variables)
    fig, ax = plt.subplots(1,variables_count+1)
    fig.set_size_inches(6*(variables_count+1),6)
    ax[0].plot(*array_of_result)
    for i in range(1,variables_count+1) :
        ax[i].plot(list_result_t,array_of_result[i-1])
    return

def mainTest2D(func):
    lamdified_equation_system = [sp.lambdify(t,func) for func in groundtruth_equations]
    groundtruth_t = np.linspace(t_start,t_end+h,1000)
    groundtruth_var = [[lamdified_equation(t) for t in groundtruth_t] for lamdified_equation in lamdified_equation_system]

    if(func == deAdamsBashfort or func == deAdamsMoulton or func == mainAdamsPredictorCorrector):
        list_result_t , list_result_var = func(7,deriv_equations,variables,t,vars_start,t_start,t_end,h)
    else: 
        list_result_t , list_result_var = func(deriv_equations,variables,t,vars_start,t_start,t_end,h)

    groundtruth_var_of_sampled_t = np.array([[lamdified_equation(t) for t in list_result_t] for lamdified_equation in lamdified_equation_system])
    array_of_result = np.array(list_result_var).T
    array_of_error = np.abs(np.subtract(groundtruth_var_of_sampled_t,array_of_result))
    error_of_2d_graph = np.sqrt(np.add(
        np.square(array_of_error[0]),
        np.square(array_of_error[1])))
    variables_count = len(variables)
    fig, ax = plt.subplots(2,variables_count+1)
    fig.set_size_inches(6*(variables_count+1),12)
    ax[0,0].plot(*array_of_result)
    ax[1,0].plot(list_result_t,error_of_2d_graph)
    ax[0,0].plot(groundtruth_var[0],groundtruth_var[1])
    for i in range(1,variables_count+1) :
        ax[0,i].plot(list_result_t,array_of_result[i-1])
        ax[1,i].plot(list_result_t,array_of_error[i-1])
        ax[0,i].plot(groundtruth_t,groundtruth_var[i-1])
    return

def main3D(func):
    list_result_t , list_result_var = func(deriv_equations,variables,t,vars_start,t_start,t_end,h)
    array_of_result = np.array(list_result_var).T
    variables_count = len(variables)
    fig = plt.figure()
    ax = fig.add_subplot(1,4,1,projection = "3d")
    X = array_of_result[0]
    Y = array_of_result[1]
    Z = array_of_result[2]
    fig.set_size_inches(6*(variables_count+1),6)
    ax.plot(*array_of_result, lw = 0.5)
    for i in range(1,variables_count+1) :
        ax = fig.add_subplot(1,4,i+1)
        ax.plot(list_result_t,array_of_result[i-1])
    return

def test():
    print("Euler hiện: ")
    print("=============================================================================")
    mainTest2D(deEulerForward)
    plt.show()
    print("Euler ẩn: ")
    print("=============================================================================")
    mainTest2D(deEulerBackward)
    plt.show()
    print("Thang ẩn: ")
    print("=============================================================================")
    mainTest2D(deTrapezoid)
    plt.show()
    print("RK3 Heun: ")
    print("=============================================================================")
    mainTest2D(deRungaKutta3_Heun)
    plt.show()
    print("RK3 Kutta: ")
    print("=============================================================================")
    mainTest2D(deRungaKutta3_Kutta)
    plt.show()
    print("RK4 Cổ điển: ")
    print("=============================================================================")
    mainTest2D(deRungeKutta4_Classic)
    plt.show()
    print("AB tuỳ chọn: ")
    print("=============================================================================")
    mainTest2D(deAdamsBashfort)
    plt.show()
    print("AM 4: ")
    print("=============================================================================")
    mainTest2D(deAdamsMoulton)
    plt.show()
    print("AB-AM PC 4: ")
    print("=============================================================================")
    mainTest2D(mainAdamsPredictorCorrector)
    plt.show()


def solve():
    typeOfGraph = chooseFunc()
    if(typeOfGraph == '3d'):
        print("Euler hiện: ")
        print("=============================================================================")
        main3D(deEulerForward)
        plt.show()
        print("Euler ẩn: ")
        print("=============================================================================")
        main3D(deEulerBackward)
        plt.show()
        print("Thang ẩn: ")
        print("=============================================================================")
        main3D(deTrapezoid)
        plt.show()
        print("RK3 Heun: ")
        print("=============================================================================")
        main3D(deRungaKutta3_Heun)
        plt.show()
        print("RK3 Kutta: ")
        print("=============================================================================")
        main3D(deRungaKutta3_Kutta)
        plt.show()
        print("RK4 Cổ điển: ")
        print("=============================================================================")
        main3D(deRungeKutta4_Classic)
        plt.show()
    if(typeOfGraph == '2d'):
        print("Euler hiện: ")
        print("=============================================================================")
        main2D(deEulerForward)
        plt.show()
        print("Euler ẩn: ")
        print("=============================================================================")
        main2D(deEulerBackward)
        plt.show()
        print("Thang ẩn: ")
        print("=============================================================================")
        main2D(deTrapezoid)
        plt.show()
        print("RK3 Heun: ")
        print("=============================================================================")
        main2D(deRungaKutta3_Heun)
        plt.show()
        print("RK3 Kutta: ")
        print("=============================================================================")
        main2D(deRungaKutta3_Kutta)
        plt.show()
        print("RK4 Cổ điển: ")
        print("=============================================================================")
        main2D(deRungeKutta4_Classic)
        plt.show()
        print("RK 2 heun: ")        
        print("=============================================================================")
        main2D(deRungeKutta2_Heun)
        plt.show()
        #print("AB 4: ")
        #print("=============================================================================")
        #main2D(mainAdamsBashfort)
        #plt.show()
        #print("AM 4: ")
        #print("=============================================================================")
        #main2D(mainAdamsMoulton)
        #plt.show()
        #print("AB-AM PC: ")
        #print("=============================================================================")
        #main2D(mainAdamsPredictorCorrector)
        #plt.show()
        dummy()

def dummy():
    return

def chooseFunc():
    if(len(variables) ==3):
        return "3d"
    else:
        return "2d"

if(Test):
    test()
else:
    solve()
