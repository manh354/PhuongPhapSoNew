from typing import List

def findMonotonicSegments(dataX, dataY):
    resultX = []
    resutlY = []
    # Nếu dộ dài của data nhỏ hơn bằng 2 thì chắc chắn chúng ở trong 1 khoảng đơn điệu
    # trong trường hợp data dài hơn, ta xét dấu giữa 2 phần tử
    # nếu giữa hai phần tử đổi dấu => sinh ra 2 khoảng đơn điệu tương ứng.
    if(len(dataX) <= 2 or len(dataY) <=2):
        resultX = [dataX]
        resutlY = [dataY]
        return resultX,resutlY
    sign = 1 if dataY[1] - dataY[0] > 0 else -1
    monotonicX = [dataX[0], dataX[1]]
    monotonicY = [dataY[0], dataY[1]]
    for i in range(2,len(dataY)):
        if i == len(dataY)-1:
            resultX.append(monotonicX)
            resutlY.append(monotonicY)
        if sign*(dataY[i] - dataY[i-1]) >= 0:
            monotonicX.append(dataX[i])
            monotonicY.append(dataY[i])
        else:
            sign = -sign
            resultX.append(monotonicX)
            resutlY.append(monotonicY)
            monotonicX = [dataX[i-1],dataX[i]]
            monotonicY = [dataY[i-1],dataY[i]]
    return resultX,resutlY

def findAllSegmentContainPointY(monotonic_segments_list_x : list[list], monotonic_segments_list_y: list[list], point_y):
    allSegmentX = []
    allSegmentY = []
    for i,segment in enumerate(monotonic_segments_list_y):
        if((segment[0] >= point_y and segment[-1] <= point_y) or (segment[0]<= point_y and segment[-1]>=point_y)):
            allSegmentX.append (monotonic_segments_list_x[i])
            allSegmentY.append( monotonic_segments_list_y[i])
    return allSegmentX,allSegmentY

def findUsableSegmentFromData(dataX,dataY, point_y):
    monotonic_segments_list_x, monotonic_segments_list_y = findMonotonicSegments(dataX, dataY)
    usable_segments_x, usable_segments_y = findAllSegmentContainPointY(monotonic_segments_list_x, monotonic_segments_list_y, point_y)
    if(usable_segments_x == None or usable_segments_y == None):
        return None,None
    print("Có các khoảng đơn điệu sau:")
    for i in range(0,len(usable_segments_x)):
        print("Dãy {0}: X = {1} ; Y = {2}".format(i, usable_segments_x[i],usable_segments_y[i]))
    print("Chọn khoảng đơn điệu cần tìm: (ấn số 1,2...)")
    number = int(input())
    return usable_segments_x[number],usable_segments_y[number]

