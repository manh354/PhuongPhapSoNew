import InputInterface
import numpy as np
import matplotlib.pyplot as plt

dataX = np.linspace(1,2,21)
dataY = [1.0,0.97350,0.95135,0.93304,0.91817,0.90640, 0.89747, 0.89115, 0.88726, 0.88565,0.88623, 0.88887, 0.89352, 0.90012, 0.90864, 0.91906, 0.93138, 0.94561, 0.96177, 0.97988, 1.00000]
dataY = np.array(dataY)

plt.plot(dataX,dataY)

plt.show()