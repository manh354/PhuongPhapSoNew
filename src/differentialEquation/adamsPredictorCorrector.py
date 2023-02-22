import numpy as np
import sympy as sp


def mulTwoPoly(polyA, polyB):
    """
    Nhân 2 đa thức với nhau
    ---
    Multiply 2 polynomials
    """
    newPoly = np.zeros(len(polyA)+len(polyB)-1)
    for i in range(0, len(polyA)):
        for j in range(0, len(polyB)):
            newPoly[i+j] += polyA[i]*polyB[j]
    return newPoly

def createRootPoly(root):
    """
    Tạo đa thức có dạng sau : t - root
    ---
    Create a polynomial with this form : t - root
    """
    newPoly = np.zeros(2)
    newPoly[0] = -root
    newPoly[1] = 1
    return newPoly

def createPascalTriangleCoefficients(n):
    array = np.zeros(1)
    array[0] = 1
    result = [array]
    for i in range(1, n):
        array = np.zeros(i+1)
        array[0] = 1
        array[len(array)-1] = 1 
        for j in range(1, i):
            array[j] = result[i-1][j] + result[i-1][j-1]
        result.append(array)
    return result

def makeNegativePascalTriangleCoefficients(coefs):
    for i in range(1, len(coefs)):
        for j in range(1, i+1):
            if(j % 2 == 1):
                coefs[i][j] = -coefs[i][j]
    return coefs

def createForwardNewtonPolys(n):
    """Tạo danh sách các đa thức newton tiến t(t+1)(t+2)...(t+k) với k từ 0 đến n-1, kể cả đa thức bậc 0 là hệ số 1"""
    result = [np.ones(1)]
    for i in range(1, n):
        result.append(mulTwoPoly(createRootPoly(-i+1), result[i-1]))
    print( result)
    return result

def createFactorialTable(n):
    """
    Tạo bảng giá trị Giai thừa (cách làm này tiết kiệm tính toán)
    ---
    Create factorial table
    """
    arr = np.zeros(n)
    arr[0] = 1
    for i in range(1,n):
        arr[i] = arr[i-1]*i
    return arr

def integratePolynomialFrom0To1(poly : list):
    """ poly nhận giá trị bậc từ 0 đến n theo chiều tăng
    """
    n = len (poly)
    np_poly = np.array(poly)
    for i in range(0,n):
        np_poly[i] /= i+1
    return np.sum(np_poly)

def createLookupTableForABMethod(n):
    newtonPolys = createForwardNewtonPolys(n)
    pascal_triangle_coefs = createPascalTriangleCoefficients(n)
    neg_pascal_triangle_coefs = makeNegativePascalTriangleCoefficients(pascal_triangle_coefs)
    factCoefs = createFactorialTable(n)
    array = np.ones(1)
    result = [array]
    for i in range(1,n):
        mulCoef = integratePolynomialFrom0To1(newtonPolys[i])
        add_to_previous_result = np.divide(np.multiply(neg_pascal_triangle_coefs[i], mulCoef), factCoefs[i])
        previous_result = np.append(result[i-1].copy(),0)
        array = np.add(previous_result, add_to_previous_result)
        result.append(array)
    
    #for i in range(0,n):
    #    print(result[i])
    return result

def integratePolynomialFrom_1To0(poly : list):
    """ poly nhận giá trị bậc từ 0 đến n theo chiều tăng
    """
    n = len (poly)
    np_poly = np.array(poly)
    for i in range(0,n):
        np_poly[i] /= i+1
        np_poly[i] *= pow(-1,i)
    return np.sum(np_poly)


def createLookupTableForAMMethod(n):
    newtonPolys = createForwardNewtonPolys(n)
    pascal_triangle_coefs = createPascalTriangleCoefficients(n)
    neg_pascal_triangle_coefs = makeNegativePascalTriangleCoefficients(pascal_triangle_coefs)
    factCoefs = createFactorialTable(n)
    array = np.ones(1)
    result = [array]
    for i in range(1,n):
        mulCoef = integratePolynomialFrom_1To0(newtonPolys[i])
        add_to_previous_result = np.divide(np.multiply(neg_pascal_triangle_coefs[i], mulCoef), factCoefs[i])
        previous_result = np.append(result[i-1].copy(),0)
        array = np.add(previous_result, add_to_previous_result)
        result.append(array)
    
    for i in range(0,n):
        print(result[i])
    return result

def makeAPCWorks(number_of_points_used, symbolic_function_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , multiple_points_vars_start: list[list[float]], multiple_points_t_start: list[float], t_end: float,h : float):
    if(multiple_points_t_start is float or int):
        return mainRungeKutta4_Classic(symbolic_function_system,symbolic_vars,symbolic_t,multiple_points_vars_start,multiple_points_t_start,multiple_points_t_start + (3.1)*h,h)
    if(number_of_points_used < len(multiple_points_t_start)):
        position = len (multiple_points_t_start) -1
        return mainRungeKutta4_Classic(symbolic_function_system,symbolic_vars,symbolic_t,multiple_points_vars_start[position],multiple_points_t_start[position],multiple_points_t_start[position]+(number_of_points_used - position + 0.1)*h, h)
    return multiple_points_t_start, multiple_points_vars_start

def mainRungeKutta4_Classic(symbolic_function_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , vars_start: list[float], t_start: float, t_end: float,h : float):
    # khởi tạo tất cả giá trị, bao gồm biến chạy t, các biến giải vars, khởi tạo phương trình lambda để thuật toán xử lý dễ dàng hơn
    list_result_t = []
    list_result_vars = []
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_function_system]

    vars_iterate = vars_start.copy()
    t_iterate = t_start
    list_result_t.append(t_iterate)
    list_result_vars.append(vars_iterate)
    while t_iterate < t_end:
        equation_system_values_k1 = [equation((vars_iterate),t_iterate) for equation in lamdified_equation_system]
        vars_added_k1 = np.add(vars_iterate, np.multiply(0.5*h,equation_system_values_k1))
        equation_system_values_k2 = [equation((vars_added_k1),t_iterate + 0.5*h) for equation in lamdified_equation_system]
        vars_added_k2 = np.add(vars_iterate,np.multiply(0.5*h,equation_system_values_k2))
        equation_system_values_k3 = [equation((vars_added_k2),t_iterate + 0.5*h) for equation in lamdified_equation_system]
        vars_added_k3 = np.add(vars_iterate,np.multiply(h,equation_system_values_k3))
        equation_system_values_k4 = [equation((vars_added_k3),t_iterate + h) for equation in lamdified_equation_system]
        vars_added_all =                       np.multiply(1/6, equation_system_values_k1)
        vars_added_all = np.add(vars_added_all,np.multiply(1/3, equation_system_values_k2))
        vars_added_all = np.add(vars_added_all,np.multiply(1/3, equation_system_values_k3))
        vars_added_all = np.add(vars_added_all,np.multiply(1/6, equation_system_values_k4))
        vars_iterate = np.add(vars_iterate,np.multiply(h,vars_added_all))
        t_iterate = t_iterate + h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)
    return list_result_t,list_result_vars


def mainAdamsPredictorCorrector(number_of_points_used : int,symbolic_function_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , multiple_points_vars_start: list[list[float]], multiple_points_t_start: list[float], t_end: float,h : float):
    ab_lookup_table = createLookupTableForABMethod(number_of_points_used)
    am_lookup_table = createLookupTableForAMMethod(number_of_points_used)
    multiple_points_t_start, multiple_points_vars_start = makeAPCWorks(number_of_points_used, symbolic_function_system , symbolic_vars, symbolic_t , multiple_points_vars_start, multiple_points_t_start, t_end,h)
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_function_system]
    list_result_t = multiple_points_t_start.copy()
    list_result_vars = multiple_points_vars_start.copy()
    list_result_vars_p = multiple_points_vars_start.copy()
    t_iterate = multiple_points_t_start[len(multiple_points_t_start)-1]
    while t_iterate < t_end:
        position = len(list_result_vars) - 1
        vars_iterate = list_result_vars[position]
        t_iterate = list_result_t[position]
        equation_system_values_p = np.zeros(len(symbolic_vars))
        # Customizable Module
        for i in range(0, number_of_points_used):
            equation_system_values_p_at_i_points_back = [equation((list_result_vars[position - i]),list_result_t[position -i]) for equation in lamdified_equation_system]
            equation_system_values_p_at_i_points_back = np.multiply(equation_system_values_p_at_i_points_back, ab_lookup_table[number_of_points_used - 1][i])
            equation_system_values_p = np.add(equation_system_values_p_at_i_points_back,equation_system_values_p)
        vars_iterate_p = np.add(vars_iterate, np.multiply(h,equation_system_values_p)) # var = var + h * d(var)/dt 
        # End of this Customizable Module
        list_result_vars_p.append(vars_iterate_p)
        equation_system_values = np.zeros(len(symbolic_vars))
        for i in range(0, number_of_points_used):
            equation_system_values_at_i_points_back = [equation((list_result_vars[position - i]),list_result_t[position -i]) for equation in lamdified_equation_system]
            equation_system_values_at_i_points_back = np.multiply(equation_system_values_at_i_points_back, am_lookup_table[number_of_points_used - 1][i])
            equation_system_values = np.add(equation_system_values_at_i_points_back,equation_system_values)
        vars_iterate = np.add(vars_iterate, np.multiply(h, equation_system_values))
        t_iterate = t_iterate+h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)

    return list_result_t,list_result_vars
