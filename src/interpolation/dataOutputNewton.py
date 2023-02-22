def outputAny(dataX, dataY,divtable, polytable, poly, x, value):
    print("Dữ liệu X: ", dataX)
    print("Dữ liệu Y: ", dataY)
    print("Bảng tỷ sai phân: ")
    print(divtable)
    print("Đa thức cộng gộp thu được : ", poly)
    print("Giá trị nội suy tại x = {0} là:  {2}".format(x,value))

def outputEqui(dataX, dataY, diffTable, polytable, poly, x, t , value):
    print("Dữ liệu X: ", dataX)
    print("Dữ liệu Y: ", dataY)
    print("Bảng sai phân: ")
    print(diffTable)
    print("Đa thức cộng gộp thu được đổi biến theo t: ", poly)
    print("Giá trị nội suy tại x = {0}, tương đương t = {1} là:  {2}".format(x,t,value))