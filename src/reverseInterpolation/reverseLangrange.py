# da thuc Langrange co cong thuc la : Tong sigma (0,n) yi/Di  * (w_n+1(x))/(x-xi)

import numpy as np
from .tableAndPolynomial import *
import matplotlib.pyplot as plt

def CalculateDiValue(roots: list, position):
    result = 1
    for i in range(0,len(roots)):
        if(i != position):
            result *= roots[position] - roots[i]
    return result

def CalcWPolynomial(roots: list):
    poly = CreateRootPoly(roots[0])
    for i in range(1, len(roots)):
        poly = MulTwoPoly(poly,CreateRootPoly(roots[i]))
    return poly

def ConvertLangrangeTableToPoly(table: list):
    poly = np.zeros(len(table))
    for j in range(0, len(table)):
        for i in range(0, len(table)):
            poly[j] += table[i][j]
    return poly

def mainLangrange(dataX, dataY):
    polynomials = []
    length = len(dataX)
    w = CalcWPolynomial(dataX)
    for i in range(0,length):
        Di = CalculateDiValue(dataX,i)
        ithPolynomial = HornerDivideReversedInput(w,dataX[i])
        #print(ithPolynomial)
        ithPolynomial = MulPolyWithCoef(ithPolynomial, dataY[i]/Di)
        polynomials.append(ithPolynomial)
    poly = ConvertLangrangeTableToPoly(polynomials)
    return w, polynomials, poly

def mainReverseLangrange(dataX, dataY):
    return mainLangrange(dataY,dataX)

def output(dataY, dataX,w,all_polynomials,final_polynomial, y, interpolate_polynomial_value_at_x):
    print("Dữ liệu Y: ", dataY)
    print("Dữ liệu X: ", dataX)
    print("Đa thức W tích Langrange: ",w)
    print("Đa thức nội suy ngược thu được:", final_polynomial)
    print("Giá trị nội suy ngược tại y = {0} là: {1}".format(y, interpolate_polynomial_value_at_x))

def drawGraph(poly,dataY, dataX):
    max_y = max(dataY)
    min_y = min(dataY)
    plt.scatter(dataY,dataX)
    generate_dataY = np.linspace(min_y,max_y,200)
    generate_dataX = [CalcPolyReversedInput(poly,x) for x in generate_dataY]
    plt.plot(generate_dataY,generate_dataX)
    plt.show()

def wrapperReverseLangrange(dataX, dataY, y):
    w, all_polynomials, final_polynomial = mainLangrange(dataY,dataX)
    interpolate_polynomial_value_at_y = CalcPolyReversedInput(final_polynomial,y)
    output(dataY, dataX,w,all_polynomials,final_polynomial, y, interpolate_polynomial_value_at_y)
    drawGraph(final_polynomial, dataY,dataX)