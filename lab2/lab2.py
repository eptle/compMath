import numpy as np

# Метод Гаусса
def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        max_row = np.argmax(np.abs(A[i:, i])) + i
        if A[max_row, i] == 0:
            raise ValueError("Матрица вырождена")
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x, A

# матрица диагонально доминирующая
def is_diagonally_dominant(A):
    n = len(A)
    for i in range(n):
        if abs(A[i, i]) <= np.sum(np.abs(A[i, :])) - abs(A[i, i]):
            return False
    return True

# матрица симметричная и положительно определенная
def is_symmetric_positive_definite(A):
    if not np.allclose(A, A.T):
        return False
    eigenvalues = np.linalg.eigvals(A)
    return np.all(eigenvalues > 0)

# гарантирует отсутствие нулевых элементов на главной диагонали
def nonzero_main_elements(func):
    def wrapper(A: np.array, b: np.array):
        n = len(A)
        A, b = A.copy(), b.copy()

        for i in range(n):
            if abs(A[i, i]) < 1e-10:
                for j in range(i + 1, n):
                    if abs(A[j, i]) > 1e-10:
                        A[[i, j]], b[[i, j]] = A[[j, i]], b[[j, i]]
                        break
        return func(A, b)

    return wrapper

@nonzero_main_elements
def triangle_matrix(A: np.array, b: np.array):
    n = len(A)

    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]

    return A, b

# 
def gauss_seidel(A, b, tol=1e-4, max_iterations=100, verbose=False):
    n = len(A)
    x = np.zeros(n)

    D = np.diag(np.diag(A))
    D_inv = np.diag(1 / np.diag(D))
    B = -D_inv @ (A - D)
    f = D_inv @ b

    i = 0
    while i < max_iterations:
        x_new = B @ x + f

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, i + 1

        x = x_new
        i += 1

        if verbose:
            print(f"Итерация {i}: {x}")

    return x, i

if __name__ == "__main__":
    A = np.array([[1.14, -5.03, 3.01, 0.12],
                 [4.77, 1.03, 0.58, -1.17],
                 [2.11, 1.17, 4.89, 0.88],
                 [0.14, -0.18, 1.28, 2.10]], dtype=float)
    b = np.array([-10.91, 12.19, 0.79, -3.46], dtype=float)
    x_exact = np.array([-1, 2, -1, 2], dtype=float)

    x_gauss, A_triangular = gauss_elimination(A.copy(), b.copy())
    print("Матрица, *приведенная к треугольному виду:")
    print(A_triangular)
    print("\nРешение методом Гаусса:")
    print(x_gauss)
    print("Погрешность метода Гаусса:", np.linalg.norm(x_gauss - x_exact))

    if is_diagonally_dominant(A):
        print("\nМатрица A является строго диагонально доминирующей.")
    elif is_symmetric_positive_definite(A):
        print("\nМатрица A является симметричной и положительно определенной.")
    else:
        print("\nМатрица A не удовлетворяет условиям сходимости метода Зейделя.")

    try:
        A, b = triangle_matrix(A, b)
        x_seidel, iterations = gauss_seidel(A, b, verbose=True)
        print(f"Решение методом Зейделя: {x_seidel}")
        print(f"Количество итераций: {iterations}")
        print("\nПреобразованная матрица A (для метода Зейделя):")
        print(A)
        print("\nРешение методом Зейделя:")
        print(x_seidel)
        print("Количество итераций:", iterations)
        print("Погрешность метода Зейделя:", np.linalg.norm(x_seidel - x_exact))
    except ValueError as e:
        print(e)
