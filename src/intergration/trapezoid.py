import numpy as np

def trapezoidDiscrete(interval_size, dataY, num_step):
    trapezoidY = np.multiply(dataY,2)
    trapezoidY[0] = dataY[0]
    trapezoidY[len(dataY)-1] = dataY[len(dataY)-1]
    integrated_result =  np.multiply(interval_size/2,np.sum(trapezoidY))
    print("Giá trị tích phân với grid = {0} là: {1}".format(num_step,integrated_result))
    return integrated_result

def halvesGrid(dataY):
    dataY2 = []
    for i in range(len(dataY)):
        if i%2==0:
            dataY2.append(dataY[i])
    return dataY2