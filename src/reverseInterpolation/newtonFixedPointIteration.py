from tableAndPolynomial import *
import math
import numpy as np

def mainNewtonForwardReverse(dataX, dataY, diemCanNoiSuyNguoc, doChinhXac):
    """
    Hàm nội suy ngược Newton tiến
    
    Params:
        dataX: đầu vào X
        dataY: đầu vào Y
        diemCanNoiSuyNguoc: điểm cần nội suy ngược
        doChinhXac: độ chính xác cần đạt (sẽ tính 2 lần lặp liên tiếp mà độ lớn hiệu không vượt quá giá trị này)
    
    Return:
        Trả về giá trị là vị trí của t (phải convert ngược lại ra giá trị x)
    """
    # Tạo ra đa thức newton ban đầu
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    #print(polyTable[0])
    diffTable = CreateDifferenceTable(dataX, dataY)
    facTable = CreateFactorialTable(length)
    for i in range(1,length):
        polyTable.append(MulTwoPoly(polyTable[i-1],CreateRootPoly(i-1)))
    for i in range(0,length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[i,i] / facTable[i])
    
    # Đoạn này ta tạo đa thức lặp Phi (t) lặp bằng cách chuyển vế, chuyển số hạng bậc 1 chứa t sang vế trái và chuyển y_ (giá trị nội suy cần tính) sang vế phải
    y0 = diffTable[0,0]
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Đoạn này để tiết kiệm tính toán, trước hết đặt dấu trừ ra ngoài toàn bộ công thức vế phải
    # nên hệ số của đa thức đầu tiên nhận giá trị y0 - y_
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    polyTable[0][0] = y0 - diemCanNoiSuyNguoc
    deltaY0 = diffTable[1][1] # lấy delta y0 ra để dùng chia đa thức sau (xem công thức lặp newton)
    polyTable[1][1] = 0 # tương đương với việc chuyển số hạng bậc 1 sang vế trái nên vế phải không còn số hạng t bậc 1

    iteratePoly = ConvertPolyTableToPoly(polyTable)

    # để bắt đầu lặp, ta cần gán cho t0 giá trị ban đầu, lấy bằng (y_ - y0)/delta y0
    t0 = -polyTable[0][0]/deltaY0 # vừa tính ở trên : polyTable[0][0] = y0 - y_
    print("Giá trị khởi tạo: giá trị t0 = {1}".format(0,t0))
    t1 = -CalcPolyReversedInput(iteratePoly,t0)/deltaY0 # tính lần lặp đầu
    soLanLap = 1
    print("Lan lap thu:{0}; gia tri t{0} = {1}".format(soLanLap,t1))
    hoiTuHayKhong = True
    while(abs(t1-t0)>= doChinhXac):
        t0 = t1
        t1 = -CalcPolyReversedInput(iteratePoly,t0)/deltaY0
        if(math.isinf(t1)):
            hoiTuHayKhong = False
            print("Giá trị ra VÔ CÙNG")
            break
        if(soLanLap > 1000):
            hoiTuHayKhong = False
            print("Giá trị KHÔNG HỘI TỤ")
            break
        soLanLap += 1
        print("Lan lap thu:{0}; gia tri t{0} = {1}".format(soLanLap,t1))
    h = dataX[1] - dataX[0]
    x = dataX[0] + t1* h
    return soLanLap, hoiTuHayKhong, t1, x


def mainNewtonBackwardReverse(dataX, dataY, diemCanNoiSuyNguoc, doChinhXac):
    # Tạo ra đa thức newton ban đầu
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    #print(polyTable[0])
    diffTable = CreateDifferenceTable(dataX, dataY)
    facTable = CreateFactorialTable(length)
    for i in range(1,length):
        polyTable.append(MulTwoPoly(polyTable[i-1],CreateRootPoly(-i+1)))
    for i in range(0,length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[-1,i] / facTable[i])
    
    # Đoạn này ta tạo đa thức lặp Phi (t) lặp bằng cách chuyển vế, chuyển số hạng bậc 1 chứa t sang vế trái và chuyển y_ (giá trị nội suy cần tính) sang vế phải
    yn = diffTable[-1,0]
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Đoạn này để tiết kiệm tính toán, trước hết đặt dấu trừ ra ngoài toàn bộ công thức vế phải
    # nên hệ số của đa thức đầu tiên nhận giá trị yn - y_
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    polyTable[0][0] = yn - diemCanNoiSuyNguoc
    nablaYN = diffTable[-1,1] # lấy nabla yn ra để dùng chia đa thức sau (xem công thức lặp newton)
    polyTable[1][1] = 0 # tương đương với việc chuyển số hạng bậc 1 sang vế trái nên vế phải không còn số hạng t bậc 1

    iteratePoly = ConvertPolyTableToPoly(polyTable)

    # để bắt đầu lặp, ta cần gán cho t0 giá trị ban đầu, lấy bằng (y_ - yn)/nabla yn
    t0 = -polyTable[0][0]/nablaYN # vừa tính ở trên : polyTable[0][0] = yn - y_
    print(t0)
    print("Giá trị khởi tạo: giá trị t0 = {1}".format(0,t0))
    soLanLap = int(1)
    t1 = -CalcPolyReversedInput(iteratePoly,t0)/nablaYN # tính lần lặp đầu
    print(t1)
    print("Lần lặp thứ:{0}; giá trị t{0} = {1}".format(soLanLap,t1))
    hoiTuHayKhong = True
    while(abs(t1-t0)>= doChinhXac):
        t0 = t1
        t1 = -CalcPolyReversedInput(iteratePoly,t0)/nablaYN
        if(math.isinf(t1)):
            hoiTuHayKhong = False
            print("Giá trị ra VÔ CÙNG")
            break
        if(soLanLap > 1000):
            hoiTuHayKhong = False
            print("Giá trị không hội tụ")
            break
        soLanLap += 1
        print("Lần lặp thứ:{0}; giá trị t{0} = {1}".format(soLanLap,t1))
    h = dataX[1] - dataX[0]
    x = dataX[len(dataX)-1] + t1* h
    return soLanLap, hoiTuHayKhong, t1, x

a = 1; b = 2; h = 0.05
dataX = [1., 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2. ]
dataY = [1.00000, 0.97350, 0.95135, 0.93304, 0.91817, 0.90640, 0.89747, 0.89115, 0.88726, 0.88565, 0.88623, 0.88887, 0.89352, 0.90012, 0.90864, 0.91906, 0.93138, 0.94561, 0.96177, 0.97988, 1.00000]
print(list(zip(dataX,dataY)))

dataX = [1., 1.05, 1.1, 1.15, 1.2, 1.25]
dataY = [1.00000, 0.97350, 0.95135, 0.93304, 0.91817, 0.90640]
mainNewtonBackwardReverse(dataX,dataY,0.91106,0.0001)