import numpy as np

A = np.array([[1.14, -5.03, 3.01, 0.12],
                 [4.77, 1.03, 0.58, -1.17],
                 [2.11, 1.17, 4.89, 0.88],
                 [0.14, -0.18, 1.28, 2.10]])

b = np.array([-10.91, 12.19, 0.79, -3.46], dtype=float)
x_exact = np.array([2, 2, -1, -1], dtype=float)

def gauss_with_pivoting(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    
    # Прямой ход с выбором главного элемента
    for k in range(n):
        max_row = np.argmax(np.abs(A[k:n, k])) + k
        A[[k, max_row]] = A[[max_row, k]]  # Переставляем строки
        b[[k, max_row]] = b[[max_row, k]]
        
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
    
    # Обратный ход
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x, A

# Решение методом Гаусса
x_gauss, A_triangular = gauss_with_pivoting(A.copy(), b.copy())
abs_error_gauss = np.linalg.norm(x_gauss - x_exact, ord=np.inf)
rel_error_gauss = abs_error_gauss/np.linalg.norm(x_gauss)*100

# Вывод результатов
print("Решение методом Гаусса:", x_gauss)
print("Матрица после приведения к верхнетреугольному виду:\n", A_triangular)
print(f"Погрешности метода Гаусса:", abs_error_gauss, rel_error_gauss)
