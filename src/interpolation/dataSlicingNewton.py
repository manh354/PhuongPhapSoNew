def sliceInputNewtonForward(dataX, dataY):
    print("Chọn mốc bắt đầu của newton tiến: ")
    start = float(input())
    nearest_node_value, index_of_nearest_node = findNearestPoint(dataX, start)
    print("Đã chọn mốc gần nhất: {0}, index: {1}".format(nearest_node_value,index_of_nearest_node))
    left, right , center = AutoFindSliceWhenIndexIsKnown(dataX,dataY, index_of_nearest_node)
    print("Chọn được tối đa: {0} mốc về bên phải".format( right))
    print("Chọn số mốc kết nạp bên phải: ")
    number = int(input())
    result = trySliceNewtonForward(dataX,dataY,index_of_nearest_node,number)
    while(result == False):
        print("Kết nạp {0} điểm thất bại, giảm đi 1".format(number))
        number -=1
        result = trySliceNewtonForward(dataX,dataY,index_of_nearest_node,number)
    dataX, dataY = result
    return dataX, dataY

def trySliceNewtonForward(dataX, dataY, center_index, number_of_points : int):
    right_offset = int(number_of_points)
    if(center_index + right_offset >= len(dataX)):
        print("Mốc chọn về bên phải vượt khỏi biên")
        return False
    return SliceFromTo(dataX,dataY, center_index,center_index + right_offset)

def sliceInputNewtonBackward(dataX, dataY):
    print("Chọn mốc bắt đầu của newton lùi: ")
    start = float(input())
    nearest_node_value, index_of_nearest_node = findNearestPoint(dataX, start)
    print("Đã chọn mốc gần nhất: {0}, index: {1}".format(nearest_node_value,index_of_nearest_node))
    left, right , center = AutoFindSliceWhenIndexIsKnown(dataX,dataY, index_of_nearest_node)
    print("Chọn được tối đa: {0} mốc về bên trái".format( left))
    print("Chọn số mốc kết nạp bên trái: ")
    number = int(input())
    result = trySliceNewtonBackward(dataX,dataY,index_of_nearest_node,number)
    while(result == False):
        print("Kết nạp {0} điểm thất bại, giảm đi 1".format(number))
        number -=1
        result = trySliceNewtonBackward(dataX,dataY,index_of_nearest_node,number)
    dataX, dataY = result
    return dataX, dataY

def trySliceNewtonBackward(dataX, dataY, center_index, number_of_points : int):
    left_offset = int(number_of_points)
    if(center_index - left_offset < 0):
        print("Mốc chọn về bên trái vượt khỏi biên")
        return False
    return SliceFromTo(dataX,dataY, center_index - left_offset,center_index)

def findNearestPoint(dataX, pointX):
    distances = [abs(pointX - x) for x in dataX]
    _, index_of_min = min((min_distance, index_of_min) for (index_of_min, min_distance) in enumerate(distances))
    return dataX[index_of_min], index_of_min

def AutoFindSliceWhenIndexIsKnown(dataX, dataY, index):
    right = (len(dataX) -1) - (index+1) +1
    left = (index -1) - 0 + 1
    center = 2*min((left,right))
    return left, right, center

def SliceFromTo(dataX, dataY, _from, _to):
    return dataX[_from:_to+1], dataY[_from:_to+1]