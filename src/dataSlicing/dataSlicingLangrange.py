
def sliceInputFromLeftToRight(dataX, dataY):
    print("Chọn mốc nội suy ngoài cùng bên trái: ")
    left = float(input())
    print("Chọn mốc nội suy ngoài cùng bên phải: ")
    right = float(input())
    ndataX, ndataY = SliceByHand(dataX,dataY,left, right)
    return ndataX, ndataY


def SliceFromTo(dataX, dataY, _from, _to):
    return dataX[_from:_to+1], dataY[_from:_to+1]

def SliceByHand(dataX, dataY, leftNodeValue, rightNodeValue):
    leftIndex = 0
    for i in range(0, len(dataX)):
        if(dataX[i] < leftNodeValue):
            leftIndex += 1
        else:break
    rightIndex = len(dataX)-1
    for j in range(len(dataX)-1,0,-1):
        if(dataX[j] > rightNodeValue):
            rightIndex -= 1
        else: break
    return SliceFromTo(dataX,dataY,leftIndex,rightIndex)
