def output(dataX, dataY,w,all_polynomials,final_polynomial, x, interpolate_polynomial_value_at_x):
    print("Dữ liệu X: ", dataX)
    print("Dữ liệu Y: ", dataY)
    print("Đa thức W tích Langrange: ",w)
    print("Đa thức nội suy thu được:", final_polynomial)
    print("Giá trị nội suy tại x = {0} là: {1}".format(x, interpolate_polynomial_value_at_x))