import numpy as np

__all__ = ["CreateDifferenceTable","CreateDividedTable","CreateFactorialTable","HornerDivide","HornerDivideReversedInput","CreateNewPoly","CalcPoly","CalcPolyReversedInput",
"MulTwoPoly","MulPolyWithCoef","CreateRootPoly","ConvertPolyTableToPoly","CreateChangedPolynomialDegreeByXamount","CreateRootPolySqr","CreateRootPolySkewed"]

def CreateDifferenceTable(dataX,dataY):
    """
    Tạo bảng sai phân
    ---
    Create difference table
    """
    length = len(dataX)
    table = np.zeros((length, length))
    for i in range(0,length):
        table[i,0] = dataY[i]
    for j in range(1,length):
        for i in range (j,length):
            table[i, j] = table[i, j - 1] - table[i - 1, j - 1]
    return table

def CreateDividedTable(dataX, dataY):
    """
    Tạo bảng tỷ sai phân
    ---
    Create divided difference table
    """
    length = len(dataX)
    table = np.zeros((length, length))
    for i in range(0,length):
        table[i,0] = dataY[i]
    for j in range(1,length):
        for i in range (j,length):
            table[i, j] = (table[i, j - 1] - table[i - 1, j - 1]) / (dataX[i] - dataX[i - j])
    return table

def CreateFactorialTable(n):
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

def HornerDivide(polynomial, value):
    newPoly = np.zeros(len(polynomial))
    newPoly[0] = polynomial[0]
    for i in range(1, len(polynomial)):
        newPoly[i] = newPoly[i - 1] * value + polynomial[i]
    return newPoly

def HornerDivideReversedInput(polynomial: list, value):
    revPolynomial = polynomial[::-1]  # slicing operator to reverse list
    newPoly = np.zeros(len(polynomial))
    newPoly[0] = revPolynomial[0]
    for i in range(1, len(revPolynomial)):
        newPoly[i] = newPoly[i - 1] * value + revPolynomial[i]
    newPoly = newPoly[:-1]
    newPoly = newPoly[::-1]
    return newPoly

def CreateNewPoly(coefs: list):
    return np.array(coefs)

def CalcPoly(polynomial, x):
    """
    Tính toán đa thức với hệ số từ bậc cao đến bậc thấp ( xuôi) : an x^n + an-1 x^n-1 + ... + a1 x + a0
    ---
    Calculate polynomial input reversed from lower degree to higher degree : a0 + a1 x + a2 x^2 + a3 x^3 +...+ an x^n
    """
    newPoly = np.zeros(len(polynomial))
    newPoly[0] = polynomial[0]
    for i in range(1, len(polynomial)):
        newPoly[i] = newPoly[i - 1] * x + polynomial[i]
    return newPoly[-1]

def CalcPolyReversedInput(polynomial, x):
    """
    Tính toán đa thức với hệ số từ bậc thấp đến bậc cao ( ngược) : a0 + a1 x + a2 x^2 + a3 x^3 +...+ an x^n
    ---
    Calculate polynomial input reversed from lower degree to higher degree : a0 + a1 x + a2 x^2 + a3 x^3 +...+ an x^n
    """
    revPolynomial = polynomial[::-1]
    newPoly = np.zeros(len(polynomial))
    newPoly[0] = revPolynomial[0]
    for i in range(1, len(polynomial)):
        newPoly[i] = newPoly[i - 1] *x + revPolynomial[i]
    return newPoly[-1]

def MulTwoPoly(polyA, polyB):
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

def MulPolyWithCoef(poly, coef):
    """
    Nhân đa thức với hệ số coef
    ---
    Multiply polynomial poly with coefficient coef
    """
    return np.multiply(poly, coef)

def CreateRootPoly(root):
    """
    Tạo đa thức có dạng sau : t - root
    ---
    Create a polynomial with this form : t - root
    """
    newPoly = np.zeros(2)
    newPoly[0] = -root
    newPoly[1] = 1
    return newPoly

def CreateRootPolySqr(root):
    """
    Tạo đa thức có dạng sau : t^2 - root^2
    --------------------------
    Create a polynomial with this form : t^2 - root^2
    """
    newPoly = np.zeros(3)
    newPoly[0] = -root*root
    newPoly[1] = 0
    newPoly[2] = 1
    return newPoly

def CreateChangedPolynomialDegreeByXamount(p, x:int):
    """
    Hàm này tạo một đa thức mới có bậc tăng lên x đơn vị so với đa thức p cũ. Tất cả hệ số được giữ nguyên.
    -------------
    This function create a new polynomial with increased degree by x amount.
    """
    newPoly = np.zeros(len(p)+x)
    for i in range(len(p)):
        newPoly[i+x] = p[i]
    return newPoly

def CreateRootPolySkewed(root):
    """
    !!! chỉ nên dùng cho đa thức nội suy Bessel không đổi biến u = t - 1/2!!!
    Tạo đa thức có dạng sau: (p+a-1)(p-a) = p^2 - p - a^2 + a
    ---
    !!! Should only be used for "normal" Bessel polynomial !!!
    Create a polynomial with this form : (p+a-1)(p-a) = p^2 - p - a^2 + a
    """
    newPoly = np.zeros(3)
    newPoly[0] = -root*root + root
    newPoly[1] = -1
    newPoly[2] = 1
    return newPoly

def ConvertPolyTableToPoly(table : list):
    """
    Từ bảng các đa thức, cộng tất cả các đa thức lại với nhau để tạo đa thức nội suy hoàn chỉnh
    ---
    From table of polynomials, add all coefficients together to create final interpolation polynomial
    """
    poly = np.zeros(len(table))
    for i in range(len(table)):
        for j in range(len(table[i])):
            poly[j] += table[i][j]
    return poly

def ConvertPolyTableToAllPolys(table: list):
    """
    Từ bảng các đa thức, cộng tất cả các đa thức lại với nhau tạo thành tất cả đa thức nội suy hoàn chỉnh theo từng bước
    ---
    ...
    """
    polies = []
    for k in range(len(table)):
        poly = np.zeros(len(table))
        for i in range(k):
            for j in range(len(table[i])):
                poly[j] += table[i][j]
        polies.append(poly)
    return polies