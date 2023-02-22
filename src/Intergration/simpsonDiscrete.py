import numpy as np

# đã kiểm thử ra kết quả đúng
a = 1
b = 2
h = 0.05
dataX = np.linspace(a,b,int((b-a)/h +1))
print(np.array(dataX))
dataY = [1.00000, 0.97350, 0.95135, 0.93304, 0.91817, 0.90640, 0.89747, 0.89115, 0.88726, 0.88565, 0.88623, 0.88887, 0.89352, 0.90012, 0.90864, 0.91906, 0.93138, 0.94561, 0.96177, 0.97988,1.00000]
simpsonsY = [4*y if i%2 != 0 else 2*y for (i,y) in enumerate(dataY)]
simpsonsY[0] = dataY[0]
simpsonsY[-1] = dataY[-1]
integrated_result =  np.multiply(h/3,np.sum(simpsonsY))
print(integrated_result)


dataX = np.linspace(0,1,num= 11)
dataY = np.array([np.e**x for x in dataX])
simpsonsY = [4*y if i%2 != 0 else 2*y for (i,y) in enumerate(dataY)]
simpsonsY[0] = dataY[0]
simpsonsY[-1] = dataY[-1]
integrated_result =  np.multiply(h/3,np.sum(simpsonsY))
print(integrated_result)