import numpy as np
import sympy as sp


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
        equation_system_values_k1 = np.multiply(h,[equation((vars_iterate),t_iterate) for equation in lamdified_equation_system])
        vars_added_k1 = np.add(vars_iterate, np.multiply(0.5,equation_system_values_k1))
        equation_system_values_k2 = np.multiply(h,[equation((vars_added_k1),t_iterate + 0.5*h) for equation in lamdified_equation_system])
        vars_added_k2 = np.add(vars_iterate,np.multiply(0.5,equation_system_values_k2))
        equation_system_values_k3 = np.multiply(h,[equation((vars_added_k2),t_iterate + 0.5*h) for equation in lamdified_equation_system])
        vars_added_k3 = np.add(vars_iterate,np.multiply(1,equation_system_values_k3))
        equation_system_values_k4 = np.multiply(h,[equation((vars_added_k3),t_iterate + h) for equation in lamdified_equation_system])
        vars_added_all =                       np.multiply(1/6, equation_system_values_k1)
        vars_added_all = np.add(vars_added_all,np.multiply(1/3, equation_system_values_k2))
        vars_added_all = np.add(vars_added_all,np.multiply(1/3, equation_system_values_k3))
        vars_added_all = np.add(vars_added_all,np.multiply(1/6, equation_system_values_k4))
        vars_iterate = np.add(vars_iterate,vars_added_all)
        t_iterate = t_iterate + h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)
    return list_result_t,list_result_vars

def mainRungaKutta3_Heun(symbolic_function_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , vars_start: list[float], t_start: float, t_end: float,h : float):
    list_result_t = []
    list_result_vars = []
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_function_system]
    vars_iterate = vars_start.copy()
    t_iterate = t_start
    list_result_t.append(t_iterate)
    list_result_vars.append(vars_iterate)
    while t_iterate < t_end:
        equation_system_values_k1 = np.multiply(h,[equation((vars_iterate),t_iterate) for equation in lamdified_equation_system])
        vars_for_k2 = np.add(vars_iterate, np.multiply(1/3,equation_system_values_k1))
        equation_system_values_k2 = np.multiply(h,[equation(vars_for_k2,t_iterate + 1/3*h) for equation in lamdified_equation_system])
        vars_for_k3 = np.add(vars_iterate,np.multiply(2/3,equation_system_values_k2))
        equation_system_values_k3 = np.multiply(h,[equation(vars_for_k3,t_iterate + 2/3*h) for equation in lamdified_equation_system])
        vars_added_all =                       np.multiply(1/4, equation_system_values_k1)
        vars_added_all = np.add(vars_added_all,np.multiply(3/4, equation_system_values_k3))
        vars_iterate = np.add(vars_iterate,vars_added_all)
        t_iterate = t_iterate + h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)
    return list_result_t,list_result_vars

## Hay còn gọi là RK3 mốc Simpson 
def mainRungaKutta3_Kutta(symbolic_function_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , vars_start: list[float], t_start: float, t_end: float,h : float):
    list_result_t = []
    list_result_vars = []
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_function_system]
    vars_iterate = vars_start.copy()
    t_iterate = t_start
    list_result_t.append(t_iterate)
    list_result_vars.append(vars_iterate)
    while t_iterate < t_end:
        equation_system_values_k1 = np.multiply(h,[equation((vars_iterate),t_iterate) for equation in lamdified_equation_system])
        vars_for_k2 = np.add(vars_iterate, np.multiply(0.5,equation_system_values_k1))
        equation_system_values_k2 = np.multiply(h,[equation(vars_for_k2,t_iterate + 0.5*h) for equation in lamdified_equation_system])
        vars_for_k3 = np.subtract(np.add(vars_iterate,np.multiply(2,equation_system_values_k2)),equation_system_values_k1)
        equation_system_values_k3 = np.multiply(h,[equation(vars_for_k3,t_iterate + h) for equation in lamdified_equation_system])
        vars_added_all =                       np.multiply(1/6, equation_system_values_k1)
        vars_added_all = np.add(vars_added_all,np.multiply(2/3, equation_system_values_k2))
        vars_added_all = np.add(vars_added_all,np.multiply(1/6, equation_system_values_k3))
        vars_iterate = np.add(vars_iterate,vars_added_all)
        t_iterate = t_iterate + h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)
    return list_result_t,list_result_vars