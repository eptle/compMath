import math

# Функции f, f', f''
def f(x):
    return math.log10(x)

def df(x):
    return 1 / (x * math.log(x))

def d2f(x):
    return - 1 / (x**2 * math.log(x))

# Структура для хранения результатов (используем словарь)
class Result:
    def __init__(self, x, f_prime_left, f_prime_right, f_prime_center,
                 exact_first_derivative, error_left, error_right, error_center,
                 f_second, exact_second_derivative, error_second):
        self.x = x
        self.f_prime_left = f_prime_left
        self.f_prime_right = f_prime_right
        self.f_prime_center = f_prime_center
        self.exact_first_derivative = exact_first_derivative
        self.error_left = error_left
        self.error_right = error_right
        self.error_center = error_center
        self.f_second = f_second
        self.exact_second_derivative = exact_second_derivative
        self.error_second = error_second


# Параметры
a = 2
b = 2.5
n = 5
h = (b - a) / (n - 1)

# Генерируем точки
x_values = [a + i * h for i in range(n)]
results = []

for i in range(n):
    xi = x_values[i]
    exact_1st = df(xi)
    exact_2nd = d2f(xi)

    f_prime_left = (f(xi) - f(xi - h)) / h if i > 0 else float('nan')
    f_prime_right = (f(xi + h) - f(xi)) / h if i < n - 1 else float('nan')
    f_prime_center = (f(xi + h) - f(xi - h)) / (2 * h) if 0 < i < n - 1 else float('nan')

    f_second = (f(xi + h) - 2 * f(xi) + f(xi - h)) / (h * h) if 0 < i < n - 1 else float('nan')

    error_left = abs(exact_1st - f_prime_left) if i > 0 else float('nan')
    error_right = abs(exact_1st - f_prime_right) if i < n - 1 else float('nan')
    error_center = abs(exact_1st - f_prime_center) if 0 < i < n - 1 else float('nan')
    error_second = abs(exact_2nd - f_second) if 0 < i < n - 1 else float('nan')

    results.append(Result(xi, f_prime_left, f_prime_right, f_prime_center,
                          exact_1st, error_left, error_right, error_center,
                          f_second, exact_2nd, error_second))

# Вывод таблицы
print(f"{'x':>6} {'f\'(x) Лев.':>12} {'f\'(x) Прав.':>12} {'f\'(x) Центр':>14} {'Точная f\'(x)':>14} "
      f"{'Погр. Лев.':>14} {'Погр. Прав.':>16} {'Погр. Центр':>16} {'f\'\'(x)':>12} {'Точная f\'\'(x)':>14} {'Погр. 2-я':>12}")
for r in results:
    def format_val(val, width):
        return f"{val:.4f}".rjust(width) if not math.isnan(val) else "N/A".rjust(width)

    print(f"{r.x:6.2f} "
          f"{format_val(r.f_prime_left, 12)} "
          f"{format_val(r.f_prime_right, 12)} "
          f"{format_val(r.f_prime_center, 14)} "
          f"{format_val(r.exact_first_derivative, 14)} "
          f"{format_val(r.error_left, 14)} "
          f"{format_val(r.error_right, 16)} "
          f"{format_val(r.error_center, 16)} "
          f"{format_val(r.f_second, 12)} "
          f"{format_val(r.exact_second_derivative, 14)} "
          f"{format_val(r.error_second, 12)}")
