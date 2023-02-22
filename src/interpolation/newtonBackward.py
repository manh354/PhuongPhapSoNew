import sys
from dataSlicingNewton import sliceInputNewtonBackward
from dataOutputNewton import outputAny, outputEqui
sys.path.append('../PhuongPhapSo')

from tableAndPolynomial import *
from valuesConvert import *

def mainAny(dataX, dataY):
    """
    Newton lùi với mốc bất kì (giữ nguyên biến x)
    """
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    #print(polyTable[0])
    divTable = CreateDividedTable(dataX, dataY)
    print("Bảng tỷ sai phân:")
    print(divTable)
    for i in range(1,length):
        polyTable.append(MulTwoPoly(polyTable[i-1],CreateRootPoly(dataX[-i])))
    for i in range(0,length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], divTable[-1,i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly

def wrapperNewtonBackwardAny(dataX, dataY, x):
    dataX, dataY = sliceInputNewtonBackward(dataX,dataY)
    divtable, polytable, poly = mainAny(dataX,dataY)
    value = CalcPolyReversedInput(poly,x)
    outputAny(dataX,dataY,divtable,polytable,poly,x,value)
    return poly

def mainEqui(dataX, dataY):
    """
    Newton lùi với mốc cách đều (đổi biến sang t)
    """
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    #print(polyTable[0])
    diffTable = CreateDifferenceTable(dataX, dataY)
    facTable = CreateFactorialTable(length)
    print("Bảng sai phân:")
    print(diffTable)
    for i in range(1,length):
        polyTable.append(MulTwoPoly(polyTable[i-1],CreateRootPoly(-i+1)))
    for i in range(0,length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[-1,i] / facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    x0 = dataX[len(dataX)-1]
    return diffTable, polyTable, poly, x0


def wrapperNewtonBackwardEqui(dataX, dataY, x):
    h = dataX[1] - dataX[0]
    dataX, dataY = sliceInputNewtonBackward(dataX,dataY)
    diffTable, polyTable, poly, x0 = mainEqui(dataX,dataY)
    t = (x-x0)/h
    value = CalcPolyReversedInput(poly,t)
    outputEqui(dataX,dataY,diffTable,polyTable,poly,x,value)
    return poly
