
def sliceInputFromCenterGauss1(dataX, dataY):
    print("Chọn mốc nội suy trung tâm trái: ")
    center = float(input())
    nearest_node_value, index_of_nearest_node = findNearestPoint(dataX, center)
    print("Đã chọn mốc gần nhất: {0}, index: {1}".format(nearest_node_value,index_of_nearest_node))
    left, right , center = AutoFindSliceWhenIndexIsKnown(dataX,dataY, index_of_nearest_node)
    print("Chọn được tối đa: {0} mốc về bên phải, {1} mốc về bên trái, {2} mốc tổng cộng".format( left, right, center))
    print("Chọn tổng số mốc kết nạp về CẢ HAI bên: ")
    number = int(input())
    result = trySliceFromCenterGauss1(dataX,dataY,index_of_nearest_node,number)
    while(result == False):
        print("Kết nạp {0} điểm thất bại, giảm đi 1".format(number))
        number -=1
        result = trySliceFromCenterGauss1(dataX,dataY,index_of_nearest_node,number)
    dataX, dataY = result
    return dataX, dataY

def sliceInputFromCenterGauss2(dataX, dataY):
    print("Chọn mốc nội suy trung tâm phải: ")
    center = float(input())
    nearest_node_value, index_of_nearest_node = findNearestPoint(dataX, center)
    print("Đã chọn mốc gần nhất: {0}, index: {1}".format(nearest_node_value,index_of_nearest_node))
    left, right , center = AutoFindSliceWhenIndexIsKnown(dataX,dataY, index_of_nearest_node)
    print("Chọn được tối đa: {0} mốc về bên phải, {1} mốc về bên trái, {2} mốc tổng cộng".format( left, right, center))
    print("Chọn tổng số mốc kết nạp về CẢ HAI bên: ")
    number = int(input())
    result = trySliceFromCenterGauss2(dataX,dataY,index_of_nearest_node,number)
    while(result == False):
        print("Kết nạp {0} điểm thất bại, giảm đi 1".format(number))
        number -=1
        result = trySliceFromCenterGauss2(dataX,dataY,index_of_nearest_node,number)
    dataX, dataY = result
    return dataX, dataY


def sliceInputFromCenterBessel(dataX,dataY):
    print("Chọn mốc nội suy trung tâm trái")
    center = float(input())
    nearest_node_value, index_of_nearest_node = findNearestPoint(dataX, center)
    print("Đã chọn mốc gần nhất: {0}, index: {1}".format(nearest_node_value,index_of_nearest_node))
    left, right , center = AutoFindSliceWhenIndexIsKnown(dataX,dataY, index_of_nearest_node)
    print("Chọn được tối đa: {0} mốc về bên phải, {1} mốc về bên trái, {2} mốc tổng cộng".format( left, right, center))
    print("Chọn số mốc kết nạp về MỘT bên: ")
    number = int(input())
    result = trySliceFromCenterBessel(dataX,dataY,index_of_nearest_node,number)
    while(result == False):
        print("Kết nạp {0} điểm thất bại, giảm mỗi bên đi 1".format(number*2))
        number -=1
        result = trySliceFromCenterBessel(dataX,dataY,index_of_nearest_node,number)
    dataX, dataY = result
    return dataX, dataY

def sliceInputFromCenterStirling(dataX, dataY):
    print("Chọn mốc nội suy trung tâm chính giữa")
    center = float(input())
    nearest_node_value, index_of_nearest_node = findNearestPoint(dataX, center)
    print("Đã chọn mốc gần nhất: {0}, index: {1}".format(nearest_node_value,index_of_nearest_node))
    left, right , center = AutoFindSliceWhenIndexIsKnown(dataX,dataY, index_of_nearest_node)
    print("Chọn được tối đa: {0} mốc về bên phải, {1} mốc về bên trái, {2} mốc tổng cộng".format( left, right, center))
    print("Chọn số mốc kết nạp về MỘT bên: ")
    number = int(input())
    result = trySliceFromCenterStirling(dataX,dataY,index_of_nearest_node,number)
    while(result == False):
        print("Kết nạp {0} điểm thất bại, giảm mỗi bên đi 1".format(number*2+1))
        number -=1
        result = trySliceFromCenterStirling(dataX,dataY,index_of_nearest_node,number)
    dataX, dataY = result
    return dataX, dataY


def findNearestPoint(dataX, pointX):
    distances = [abs(pointX - x) for x in dataX]
    _, index_of_min = min((min_distance, index_of_min) for (index_of_min, min_distance) in enumerate(distances))
    return dataX[index_of_min], index_of_min

def trySliceFromCenterGauss1(dataX, dataY, center_index, number_of_points : int):
    left_offset = int((number_of_points-1)/2)
    right_offset = int(number_of_points/2)
    if left_offset < 0 :
        left_offset = 0
    if(center_index - left_offset < 0):
        print("Mốc chọn về bên trái vượt khỏi biên")
        return False
    if(center_index + right_offset >= len(dataX)):
        print("Mốc chọn về bên phải vượt khỏi biên")
        return False
    return SliceFromTo(dataX,dataY, center_index-left_offset,center_index + right_offset)


def trySliceFromCenterGauss2(dataX, dataY, center_index, number_of_points : int):
    left_offset = int(number_of_points/2)
    right_offset = int((number_of_points-1)/2)
    if right_offset < 0 :
        right_offset = 0
    if(center_index - left_offset < 0):
        print("Mốc chọn về bên trái vượt khỏi biên")
        return False
    if(center_index + right_offset >= len(dataX)):
        print("Mốc chọn về bên phải vượt khỏi biên")
        return False
    return SliceFromTo(dataX,dataY, center_index-left_offset,center_index + right_offset)

def trySliceFromCenterBessel(dataX, dataY, center_index, number_of_points_on_one_side: int):
    left_offset = number_of_points_on_one_side-1
    right_offset = number_of_points_on_one_side
    if(left_offset < 0):
        left_offset = 0
    if(center_index - left_offset < 0):
        print("Mốc chọn về bên trái vượt khỏi biên")
        return False
    if(center_index + right_offset >= len(dataX)):
        print("Mốc chọn về bên phải vượt khỏi biên")
        return False
    return SliceFromTo(dataX,dataY, center_index-left_offset,center_index + right_offset)

def trySliceFromCenterStirling(dataX, dataY, center_index, number_of_points_on_one_side: int):
    left_offset = number_of_points_on_one_side
    right_offset = number_of_points_on_one_side
    if(center_index - left_offset < 0):
        print("Mốc chọn về bên trái vượt khỏi biên")
        return False
    if(center_index + right_offset >= len(dataX)):
        print("Mốc chọn về bên phải vượt khỏi biên")
        return False
    return SliceFromTo(dataX,dataY, center_index-left_offset,center_index + right_offset)


def AutoFindSliceWhenIndexIsKnown(dataX, dataY, index):
    right = (len(dataX) -1) - (index+1) +1
    left = (index -1) - 0 + 1
    center = 2*min((left,right))
    return left, right, center

def SliceFromTo(dataX, dataY, _from, _to):
    return dataX[_from:_to+1], dataY[_from:_to+1]
"""dataX = [i for i in range(1,11)]
dataY = [1 + 0.1*2**i for i in range(1,11)]
print(dataX)
print(dataY)
sliceInputFromCenterBessel(dataX,dataY)"""