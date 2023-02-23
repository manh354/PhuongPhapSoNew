import numpy as np
import matplotlib.pyplot as plt

def makeHValues(dataX):
    size = len(dataX)-1
    result = np.zeros(size)
    for i in range(0,size):
        result[i] = (dataX[i+1]-dataX[i])
    return np.array(result)

def makeGammaVector(dataY,dataH):
    size = len(dataY)-2
    result = np.zeros(size+2)
    for i in range(0,size):
        result[i] = (dataY[i+2] - dataY[i+1])/dataH[i+1] - (dataY[i+1]-dataY[i])/dataH[i]
    return result

def makeMatrix(dataX, dataY, dataH):
    size = len(dataX)
    result = np.zeros((size, size))
    # điều kiện ma trận
    for i in range(0,size-2):
        result[i,i] = dataH[i]/6
        result[i,i+1] = (dataH[i]+dataH[i+1])/3
        result[i,i+2] = dataH[i+1]/6    
    return result

def naturalSpline(matrix, h_vector ,gamma_vector, dataY):
    matrix[-2,0] = 1
    gamma_vector[-2] = 0
    matrix[-1,-1] = 1
    gamma_vector[-1] = 0

def calculateCubic(a,b,c,d,x):
    return d+x*(c+x*(b+x*a))

dataX = np.linspace(0,1,7)
dataY = [1.00000, 0.97350, 0.95135, 0.93304, 0.91817, 0.90640, 0.89747]
dataH = makeHValues(dataX)
gamma_vector = makeGammaVector(dataY,dataH)
gamma_vector = np.transpose(np.array(gamma_vector))
matrix = makeMatrix(dataX,dataY,dataH)
naturalSpline(matrix, dataH,gamma_vector,dataY)
print(matrix)
print(gamma_vector)
alphas = np.matmul(np.linalg.inv(matrix),gamma_vector)
all_splines = []

for k in range (0,len(alphas)-1):
    a = (alphas[k+1] - alphas[k])/(6*dataH[k])
    b = (3*alphas[k]*dataX[k+1]-3*alphas[k+1]*dataX[k])/(6*dataH[k])
    c = (-3*alphas[k]*dataX[k+1]**2+3*alphas[k+1]*dataX[k]**2)/(6*dataH[k]) + (dataY[k+1]-dataY[k])/dataH[k] - (alphas[k+1]-alphas[k])*dataH[k]/6
    d = (alphas[k]*dataX[k+1]**3 - alphas[k+1]*dataX[k]**3)/(6*dataH[k]) + (dataY[k]*dataX[k+1]-dataY[k+1]*dataX[k])/dataH[k] + (alphas[k+1]*dataX[k]-alphas[k]*dataX[k+1])*dataH[k]/6
    all_splines.append((a,b,c,d))

plt.scatter(dataX,dataY)
for i in range(0,len(dataX)-1):
    a,b,c,d = all_splines[i]
    dataX_i = np.linspace(dataX[i], dataX[i+1],10)
    dataY_i = [calculateCubic(a,b,c,d,x) for x in dataX_i]
    plt.plot(dataX_i,dataY_i)

plt.show()