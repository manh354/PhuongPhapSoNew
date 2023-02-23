# da thuc Langrange co cong thuc la : Tong sigma (0,n) yi/Di  * (w_n+1(x))/(x-xi)

import numpy as np
from .tableAndPolynomial import *

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