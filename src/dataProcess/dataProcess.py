import numpy as np
import sympy as sp


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


def findSegmentContainsRoot(dataX,dataY, value):
    monotonic_segments_list_x, monotonic_segments_list_y = findMonotonicSegments(dataX, dataY)
    usable_segments_x, usable_segments_y = findAllSegmentContainPointY(monotonic_segments_list_x, monotonic_segments_list_y, value)
    if(usable_segments_x == None or usable_segments_y == None):
        return None,None
    print("Có các khoảng đơn điệu sau:")
    for i in range(0,len(usable_segments_x)):
        print("Dãy {0}: X = {1} ; Y = {2}".format(i, usable_segments_x[i],usable_segments_y[i]))
    print("Chọn khoảng đơn điệu cần tìm: (ấn số 1,2...)")
    number = int(input())
    
    return usable_segments_x,usable_segments_y,usable_segments_x[number],usable_segments_y[number]

def findNewtonFixedPointSegments(dataX, dataY, value_to_iterate):
    monotonic_segments_list_x, monotonic_segments_list_y = findMonotonicSegments(dataX,dataY)
    usable_segments_x, usable_segments_y = findAllSegmentContainPointY(monotonic_segments_list_x, monotonic_segments_list_y, value_to_iterate)
    newton_forward_result = []
    newton_backward_result = []
    for segment_x, segment_y in zip(usable_segments_x,usable_segments_y):
        # newton forward, backward and langrange
        num_left = 0
        num_right = 0
        sign_of_segment = segment_y[0] - segment_y[1]
        for x,y in zip(segment_x,segment_y):
            if((y - value_to_iterate)*(sign_of_segment) >0):
                num_left +=1
            else :
                num_right += 1
        newton_forward_result.append((segment_x[num_left-1:], segment_y[num_left-1:]))
        newton_backward_result.append((segment_x[:num_left+1], segment_y[:num_left+1]))
    return newton_forward_result,newton_backward_result

def findReverseLangrangeSegments(dataX, dataY, value_to_iterate, count_all_points):
    monotonic_segments_list_x, monotonic_segments_list_y = findMonotonicSegments(dataX,dataY)
    usable_segments_x, usable_segments_y = findAllSegmentContainPointY(monotonic_segments_list_x, monotonic_segments_list_y, value_to_iterate)
    langrange_result = []
    for segment_x, segment_y in zip(usable_segments_x,usable_segments_y):
        num_left = 0
        num_right = 0
        sign_of_segment = segment_y[0] - segment_y[1]
        for x,y in zip(segment_x,segment_y):
            if((y - value_to_iterate)*(sign_of_segment) >0):
                num_left +=1
            else :
                num_right += 1
        index = num_left
        take_left = int(index - np.floor((count_all_points+1)/2))
        take_right = int(index + np.floor((count_all_points)/2))
        count_this_loop = count_all_points
        while take_right - take_left > count_all_points:
            print("Có đoạn không thể lấy được đủ {0} điểm, thử lấy ít đi 1 điểm.".format(count_all_points))
            count_this_loop -= 1
            take_left = int(index - np.floor((count_this_loop+1)/2))
            take_right = int(index + np.floor((count_this_loop)/2))
        langrange_result.append((segment_x[take_left: take_right], segment_y[take_left: take_right]))
    return langrange_result

# ____________________________TEST_________________________________
#dataX = [1., 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2. ]
#dataY = [1.00000, 0.97350, 0.95135, 0.93304, 0.91817, 0.90640, 0.89747, 0.89115, 0.88726, 0.88565, 0.88623, 0.88887, 0.89352, 0.90012, 0.90864, 0.91906, 0.93138, 0.94561, 0.96177, 0.97988, 1.00000]
##(x,y) = findNewtonFixedPointSegments(dataX,dataY, 0.91106)
#z = findReverseLangrangeSegments(dataX,dataY, 0.91106,7)
##for x1 in x:
##    print(x1)
##for y1 in y:
##    print(y1)
#for z1 in z:
#    print(z1)