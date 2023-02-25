import pandas as pd
import sys
sys.path.append("../PhuongPhapSoNew/")

discrete_data_vertical_path = "data/discreteDataVertical.csv"

def readVertical():
    data = pd.read_csv(discrete_data_vertical_path)
    dataX = list(data['x'])
    dataY = list(data['y'])
    return dataX,dataY
