import sympy as sp
import numpy as np

# Copy đoạn này mang vào chương trình chính và chỉnh sửa nếu cần
# Hoặc chạy trực tiếp code này trong file
# input
variable = sp.Symbol("x")
equation = "e**(1.5*x*x)"
start = 0
end = 1
num_step = 2
eps = 10e-9



# kĩ thuật lưới phủ simpson bậc 2 tìm tích phân hàm khó tính M4
def simpsonQuadraticGrid(equation ,variable, start, end, num_step,eps):
    # khởi tạo chung
    all_grid_result = []
    if(isinstance(equation,str)):
        equation = sp.lambdify(variable,equation,'numpy')

    # khởi tạo grid1
    gridX = np.linspace(start,end,num_step + 1)
    gridY = np.array([equation(x) for x in gridX])
    step_size = (end-start)/num_step
    # thuật toán
    simpsonsY = [4*y if i%2 != 0 else 2*y for (i,y) in enumerate(gridY)]
    simpsonsY[0] = gridY[0]
    simpsonsY[-1] = gridY[-1]
    result = np.multiply(step_size/3.0,np.sum(simpsonsY))

    # Kết quả result là 
    all_grid_result.append((result,num_step))

    compare_value1 = float(1000)
    compare_value2 = float(-1000)

    while(abs(compare_value1 - compare_value2) * 1.0/15.0 >=eps):
        # khởi tạo grid 2
        num_step *= 2
        gridX = np.linspace(start, end, num_step +1)
        gridY = np.array([equation(x) for x in gridX])
        step_size = (end-start)/num_step
        # thuật toán
        simpsonsY = [4*y if i%2 != 0 else 2*y for (i,y) in enumerate(gridY)]
        simpsonsY[0] = gridY[0]
        simpsonsY[-1] = gridY[len(gridY)-1]
        result = np.multiply(step_size/3.0,np.sum(simpsonsY))
        all_grid_result.append((result,num_step))
        # Xét 2 giá trị grid
        compare_value1 = all_grid_result[-1][0]
        compare_value2 = all_grid_result[-2][0]
    
    return all_grid_result

#___________________________________VD chạy code________________________________
# result, num_step = simpsonQuadraticGrid(equation, variable,a,b, 10, 5e-8)
# print("Kết quả cuối cùng thu được: {0} \tsau số bước: {1}".format(result,num_step))