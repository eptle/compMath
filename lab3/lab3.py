import math

# Функция
def f(x):
    return math.sin(x) * math.exp(2 * x)

# Метод левых прямоугольников
def left_rectangle(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + i * h)
    return result * h

# Метод правых прямоугольников
def right_rectangle(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(1, n + 1):
        result += f(a + i * h)
    return result * h

# Метод средних прямоугольников
def middle_rectangle(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + (i + 0.5) * h)
    return result * h

# Метод трапеций
def trapezoid(f, a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

# Метод Симпсона
def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 == 1 else 2
        result += coef * f(a + i * h)
    return result * h / 3


if __name__ == "__main__":
    a = 0
    b = math.pi / 2
    eps = 1e-4
    n = 2
    delta = 0
    h = 0

    exact = (2*(math.e**math.pi) + 1) / 5
    print(f"Точное значение интеграла: {exact:.8f}\n")

    methods = [
        ("Левые прямоугольники", left_rectangle),
        ("Правые прямоугольники", right_rectangle),
        ("Средние прямоугольники", middle_rectangle),
        ("Метод трапеций", trapezoid),
        ("Метод Симпсона", simpson),
    ]

    for name, method in methods:
        n_curr = n
        while True:
            approx = method(f, a, b, n_curr)
            error = abs(approx - exact)
            if error < eps:
                break
            n_curr *= 2

        delta = error / approx * 100
        h = (b - a) / n_curr
        
        print(f"{name}:")
        print(f"  Приближённое значение = {approx:.8f}")
        print(f"  Погрешность = {error:.8f}")
        print(f"  Число разбиений n = {n_curr}")
        print(f"  Относительная погрешность: {delta:8f}%")
        print(f"  Шаг интегрирования: {h:.8f}")
