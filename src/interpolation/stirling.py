from .dataSlicingCenter import sliceInputFromCenterStirling
from .dataOutputCenter import output
from .tableAndPolynomial import *
import matplotlib.pyplot as plt
import numpy as np

# cách chọn chỉ số của Stirling trên bảng sai phân (lẻ số mốc)
#===============================
#   0   1   2   3   4   5   6
#===============================
#
#
#
#   -   -
#       -   -   -
#               -   -   -
#                       -   -
#===============================

def mainStirling(dataX, dataY):
    """
    Tạo đa thức Stirling , cần 2n+1 điểm đầu vào
    ---
    Create Stirling polynomial
    """
    length = len(dataX)
    diffTable = CreateDifferenceTable(dataX,dataY)
    facTable = CreateFactorialTable(length)
    middle = int(len(dataX)/2) #khai bao vị trí giữa
    polyTable = []
    polyTable.append([1])
    if length != 1:
        # đoạn này cần thiết vì thuật toán không xử lý được trường hợp độ dài = 3
        # do phép nhân trong công thức Stirling có tích đa thức dạng (t^2 - root^2)
        # chỉ bắt đầu từ số hạng thứ 4 và 5
        polyTable.append([0,1]) # thêm đa thức t
        polyTable.append([0,0,1]) # thêm đa thức t^2
        if length != 3: # Với đa thức chỉ số lớn hơn 3, ta xử lý như bình thường
            for i in range(3,length):
                if i%2==0:
                    # Các đa thức với hệ số i là chẵn chỉ cần tăng bậc lên 1 so với bậc lẻ trước nó
                    polyTable.append(CreateChangedPolynomialDegreeByXamount(polyTable[i-1],1))
                else:
                    # Các đa thức với hệ số i là lẻ thì cần nhân đa thức bậc lẻ trước nó với đa thức hiệu nghiệm bình phương (t^2-root^2)
                    polyTable.append(MulTwoPoly(polyTable[i-2], CreateRootPolySqr(int(i/2))))
    for i in range(0, length):
        # đoạn này khai báo vị trí giữa giống Gauss 1
        currentPos = middle+ int((i+1)/2)
        # để hiểu hơn thì có thể xem biểu đồ chọn chỉ số ở trên
        if i%2 == 0:
            # nếu đa thức vị trí i là chẵn thì chỉ bị ảnh hưởng bởi 1 hệ số trên bảng sai phân 
            polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[currentPos,i]/ facTable[i])
        else:
            # nếu đa thức vị trí i là lẻ thì bị ảnh hưởng bởi 2 hệ số trên bảng sai phân (2 hệ số cộng vào chia đôi)
            polyTable[i] = MulPolyWithCoef(polyTable[i], (diffTable[currentPos,i] + diffTable[currentPos-1,i])/ (2*facTable[i]))
    poly = ConvertPolyTableToPoly(polyTable)
    x0 = dataX[middle]
    return diffTable,polyTable, poly,x0

def wrapperStirling(dataX, dataY, x):
    h = dataX[1] - dataX[0]
    dataX, dataY = sliceInputFromCenterStirling(dataX, dataY)
    diffTable,polytable, poly, x0 = mainStirling(dataX,dataY)
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