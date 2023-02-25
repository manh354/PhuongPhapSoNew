import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#dataX=np.array([0.038,0.194,0.425,0.626,1.253,2.500,3.740])
#dataY=np.array([0.050,0.127,0.094,0.2122,0.2729,0.2665,0.3317])

#adjustable_parameters = sp.symbols("a c")
#independent_variable = sp.Symbol("x")
#test_function = "0"
#fitting_function = "a*x**2  + c"
#param_start = [1,1]

def wrapperLeastSquare(dataX, dataY, adjustable_parameters,independent_variable,fitting_function,param_start):
    dataX = np.array(dataX)
    dataY = np.array(dataY)
    partial_derivatives = [(sp.diff(fitting_function, param)) for param in adjustable_parameters]
    print(partial_derivatives)
    if(isinstance(fitting_function, str)):
        fitting_function = sp.lambdify([independent_variable,[*adjustable_parameters]],fitting_function, 'numpy')
    partial_derivatives = [sp.lambdify([independent_variable,[*adjustable_parameters]],p_d, 'numpy') for p_d in partial_derivatives]

    fitting_function_values = np.array(fitting_function(dataX,param_start))
    residue_values = np.subtract(dataY, fitting_function_values)

    jacobian_matrix = np.array([[p_d(x,param_start) for p_d in partial_derivatives] for x in dataX])
    jacobian_matrix_T = jacobian_matrix.T
    #print(np.matmul(jacobian_matrix_T,jacobian_matrix))
    jjt_1_jt = np.matmul(np.linalg.inv(np.matmul(jacobian_matrix_T, jacobian_matrix)),jacobian_matrix_T)
    param_iterate_after = np.add(param_start, np.matmul(jjt_1_jt,residue_values))
    fitting_function_values = np.array(fitting_function(dataX,param_iterate_after))
    residue_values_new = np.subtract(dataY, fitting_function_values)
    i = 1
    print("lần lặp thứ :", i)
    print(*["{0} = {1};".format(adjustable_parameters[i],x) for (i,x) in enumerate(param_iterate_after)])
    while (np.abs(np.sum(np.subtract(residue_values_new , residue_values)))>= 0.005) and (i < 100):
        i+= 1
        residue_values = residue_values_new
        jacobian_matrix = np.array([[p_d(x,param_iterate_after) for p_d in partial_derivatives] for x in dataX])
        jacobian_matrix_T = jacobian_matrix.T
        jjt_1_jt = np.matmul(np.linalg.inv(np.matmul(jacobian_matrix_T, jacobian_matrix)),jacobian_matrix_T)
        param_iterate_after = np.add(param_iterate_after, np.matmul(jjt_1_jt,residue_values))
        fitting_function_values = np.array(fitting_function(dataX,param_iterate_after))
        residue_values_new = np.subtract(dataY, fitting_function_values)
        print("lần lặp thứ :", i)
        print(*["{0} = {1};".format(adjustable_parameters[i],x) for (i,x) in enumerate(param_iterate_after)])
    return i, param_iterate_after

def drawLeastSquare(dataX,dataY,fitting_function ,param_iterate_after):
    model_dataX = np.linspace(dataX[0], dataX[len(dataX)-1], num = 1000)
    fitted_dataY = [fitting_function(x,param_iterate_after) for x in model_dataX]
    new_dataY = [fitting_function(x,param_iterate_after) for x in dataX]
    mse = np.divide(np.sum(np.square(np.subtract(new_dataY,dataY))),len(dataY))
    print(mse)
    plt.plot(model_dataX,fitted_dataY, color = 'orange')
    plt.scatter(dataX,dataY)
    plt.show()
