import math

# Функция для вычисления логарифма
def f(x):
    return math.log(x)

# 4 Производная функции f
def d4f(x):
    return -6/(x**4)

# Функция для вычисления полинома Лагранжа
def lagrange_polynomial(x, xk, yk):
    n = len(xk)
    p = 0.0

    for i in range(n):
        l = 1.0
        for j in range(n):
            if i != j:
                l *= (x - xk[j]) / (xk[i] - xk[j])
        p += yk[i] * l

    return p

# Функция для оценки погрешности интерполяции
def error_estimate(x, xk, df4):
    n = len(xk)

    # Находим максимальное значение производной на интервале
    M = 0.0
    steps = 1000
    for i in range(steps + 1):
        xi = xk[0] + i * (xk[-1] - xk[0]) / steps
        M = max(M, abs(df4(xi)))

    # Вычисляем произведение (x - xk[i])
    w = 1.0
    for xi in xk:
        w *= (x - xi)

    return (M * abs(w)) / math.gamma(n + 1)  # gamma(n+1) = n!

# Основная программа
if __name__ == "__main__":
    # Узлы интерполяции
    xk = [3, 3.5, 4, 4.5]
    yk = [round(f(x), 4) for x in xk]  # округление до 4 знаков

    # Точка для вычисления
    x = 3.2

    # Аналитическое значение
    y_analytical = f(x)

    # Полином Лагранжа
    y_lagrange = lagrange_polynomial(x, xk, yk)

    # Погрешности
    error = error_estimate(x, xk, d4f)
    absolute_error = abs(y_analytical - y_lagrange)

    # Вывод
    print(f"{'Точка':>10} {'Значение f(x)':>20}")
    for xi, yi in zip(xk, yk):
        print(f"{xi:>10} {yi:>20.4f}")

    print("\n")
    print(f"Значение функции в точке x = {x} Аналитически: {y_analytical:.4f}")
    print(f"Значение функции в точке x = {x} По Лагранжу: {y_lagrange:.4f}")
    print(f"Абсолютная погрешность вычислений: {absolute_error:.4f}")
    print(f"Оценка погрешности формулы Лагранжа: {error:.8f}")
