import numpy as np

A = np.array([[1.14, -5.03, 3.01, 0.12],
                 [4.77, 1.03, 0.58, -1.17],
                 [2.11, 1.17, 4.89, 0.88],
                 [0.14, -0.18, 1.28, 2.10]])

b = np.array([-10.91, 12.19, 0.79, -3.46], dtype=float)
x_exact = np.array([2, 2, -1, -1], dtype=float)

def make_strongly_diagonally_dominant(A, b):
    n = len(A)
    for i in range(n):
        row = max(range(i, n), key=lambda r: abs(A[r, i]) / sum(abs(A[r, :])) if sum(abs(A[r, :])) != 0 else 0)
        if row != i:
            A[[i, row]] = A[[row, i]]
            b[[i, row]] = b[[row, i]]
    return A, b

def seidel_method(A, b, tol=1e-4, max_iter=100):
    A, b = make_strongly_diagonally_dominant(A, b)
    n = len(b)
    x = np.zeros(n)
    x_old = np.copy(x)
    
    for iteration in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, iteration + 1
        x_old = np.copy(x)
    
    return x, max_iter

# Решение методом Зейделя
x_seidel, iterations = seidel_method(A.copy(), b.copy())
abs_error_seidel = np.linalg.norm(x_seidel - x_exact, ord=np.inf)
rel_error_seidel = abs_error_seidel/np.linalg.norm(x_seidel)*100

# Проверка условия сходимости
strongA, strongB = make_strongly_diagonally_dominant(A, b)
D = np.diag(np.diag(strongA))
L = np.tril(strongA, -1)
U = np.triu(strongA, 1)
B = -np.linalg.inv(D + L) @ U
spectral_radius = max(abs(np.linalg.eigvals(B)))
convergence = spectral_radius < 1

print("\nРешение методом Зейделя:", x_seidel)
print("Число итераций:", iterations)
print("Погрешности метода Зейделя:", abs_error_seidel, rel_error_seidel)
print("\nПреобразованная матрица для метода Зейделя:\n", strongA, strongB)
print(f"Спектральный радиус матрицы B:{spectral_radius:.3f}")
print("Условие сходимости выполнено:", convergence)

print(f'{D=}')
print(f'{L=}')
print(f'{U=}')
print(f'{B=}')
