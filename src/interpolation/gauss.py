import sys
sys.path.append('../PhuongPhapSo')
from dataSlicingCenter import sliceInputFromCenterGauss1, sliceInputFromCenterGauss2
from dataOutputCenter import output
import matplotlib.pyplot as plt
import numpy as np

from tableAndPolynomial import *

# cách chọn chỉ số của gauss1 trên bảng sai phân
#===============================
#
#
#
#   -  
#       -   -
#               -   -
#                       -   -
#===============================

def mainGauss1(dataX, dataY):
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    diffTable = CreateDifferenceTable(dataX,dataY)
    facTable = CreateFactorialTable(length)
    middle = int((len(dataX)-1)/2) #khai bao vi tri giua
    for i in range(1,length):
        offset:int #khai bao so chi p(p-1)(p+1)..(p+ offset)
        if i%2==0:
            offset = int(i/2)
        else:
            offset = int(-i/2)
        polyTable.append(MulTwoPoly(polyTable[i-1], CreateRootPoly(offset)))
    for i in range(0, length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[middle+ int((i+1)/2),i]/ facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    x0 = dataX[middle]
    return diffTable,polyTable, poly, x0

def wrapperGauss1(dataX, dataY,x):
    h = dataX[1] - dataX[0]
    dataX, dataY = sliceInputFromCenterGauss1(dataX, dataY)
    diffTable,polytable, poly, x0 = mainGauss1(dataX,dataY)
    t = (x-x0)/h
    interpolate_polynomial_value_at_x = CalcPolyReversedInput(poly,t)
    output(dataX,dataY,diffTable,polytable,poly,x,t,interpolate_polynomial_value_at_x)
    drawGraph(poly,dataX,dataY,x0,h)


# cách chọn chỉ số của gauss2 trên bảng sai phân
#===============================
#
#
#
#   -   -
#           -   -
#                   -   -
#                           -
#===============================
def mainGauss2(dataX, dataY):
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    diffTable = CreateDifferenceTable(dataX,dataY)
    facTable = CreateFactorialTable(length)
    middle = int(len(dataX)/2) #khai bao vi tri giua tuc la x0
    for i in range(1,length):
        offset:int #khai bao so chi p(p-1)(p+1)..(p + offset)
        if i%2!=0:
            offset = int(i/2)
        else:
            offset = int(-i/2)
        polyTable.append(MulTwoPoly(polyTable[i-1], CreateRootPoly(offset)))
    for i in range(0, length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[middle+ int(i/2),i]/ facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    x0 = dataX[middle]
    return diffTable,polyTable, poly,x0

def wrapperGauss2(dataX, dataY,x):
    h = dataX[1] - dataX[0]
    dataX, dataY = sliceInputFromCenterGauss2(dataX, dataY)
    diffTable,polytable, poly, x0 = mainGauss2(dataX,dataY)
    t = (x-x0)/h
    interpolate_polynomial_value_at_x = CalcPolyReversedInput(poly,t)
    output(dataX,dataY,diffTable,polytable,poly,x,t,interpolate_polynomial_value_at_x)
    drawGraph(poly,dataX,dataY,x0,h)

def drawGraph(poly, dataX, dataY,x0,h):
    max_x = max(dataX)
    min_x = min(dataX)
    plt.scatter(dataX,dataY)
    generate_dataX = np.linspace(min_x,max_x,200)
    generate_dataY = [CalcPolyReversedInput(poly,(x-x0)/h) for x in generate_dataX]
    plt.plot(generate_dataX,generate_dataY)
    plt.show()