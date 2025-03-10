import numpy as np
import matplotlib.pyplot as plt


class DiffFunction:
    def __init__(self, *derivatives):
        self.derivatives = derivatives

    def __call__(self, x, order=0):
        return self.derivatives[order](x)


def try_spread(arr_like):
    return list(arr_like) if hasattr(arr_like, '__iter__') else [arr_like]


def iterative_solver(start, step_func, epsilon=1e-7, halt_predicate=lambda pr, nx, e: abs(nx - pr) < e):
    steps = try_spread(start)
    steps.append(step_func(steps))
    while not halt_predicate(steps[-2], steps[-1], epsilon):
        steps.append(step_func(steps))
    return steps[-1], steps


def newton(f: DiffFunction, a, b, epsilon=1e-7): # метод Ньютона (метод касательных)
    step_function = lambda x: x[-1] - f(x[-1]) / f(x[-1], 1)
    start = a if f(a) * f(a, 2) > 0 else b
    return iterative_solver(start, step_function, epsilon)


def chords(f: DiffFunction, a, b, epsilon=1e-7): # метод хорд
    if f(b) * f(b, 2) <= 0:
        a, b = b, a
    step_function = lambda x: x[-1] - f(x[-1]) * (b - x[-1]) / (f(b) - f(x[-1]))
    return iterative_solver(a, step_function, epsilon)


def secants(f: DiffFunction, a, b, epsilon=1e-7): # метод секущих
    step_function = lambda x: x[-1] - f(x[-1]) * (x[-1] - x[-2]) / (f(x[-1]) - f(x[-2]))
    return iterative_solver([a, b], step_function, epsilon)


def finite_sum_newton(f: DiffFunction, a, b, epsilon=1e-7, h=0.01): # конечноразностный Нютона
    step_function = lambda x: x[-1] - h * f(x[-1]) / (f(x[-1] + h) - f(x[-1]))
    return iterative_solver(a, step_function, epsilon)


def steffensen(f: DiffFunction, a, b, epsilon=1e-7):
    step_function = lambda x: x[-1] - (f(x[-1]) ** 2) / (f(x[-1] + f(x[-1])) - f(x[-1]))
    return iterative_solver(a, step_function, epsilon)

def relaxation(f: DiffFunction, a, b, epsilon=1e-7):
    c = (a + b) / 2
    tau = 1 / f(c, 1) 
    print(tau)
    step_function = lambda x: x[-1] - tau * f(x[-1])
    return iterative_solver(a, step_function, epsilon)


if __name__ == "__main__":
    import math

    # определим функцию и её производные
    f = DiffFunction(lambda x: (1 / np.tan(x) - x**2),          # f(x)
                    lambda x: (-1 / np.sin(x)**2 - 2*x),        # f'(x)
                    lambda x: ((2*np.cos(x))/(np.sin(x)**3)) - 2) # f''(x)

    a, b = 0.5, 1  # Границы

    root_newton = newton(f, a, b)
    root_chords = chords(f, a, b)
    root_secants = secants(f, a, b)
    root_finite = finite_sum_newton(f, a, b)
    root_steffensen = steffensen(f, a, b)
    root_relaxation = relaxation(f, a, b)

    print("Метод Ньютона:\t", root_newton[1])
    print("Метод хорд:\t", root_chords[1])
    print("Метод секущих:\t", root_secants[1])
    print("Метод finite:\t", root_finite[1])
    print("Метод steff:\t", root_steffensen[1])
    print("Метод relax:\t", root_relaxation[1])

    # Определяем функцию
    def f_x(x):
        return 1 / np.tan(x) - x**2  # ctg(x) = 1 / tan(x)

    # Создаем массив значений x, исключая точки разрыва (кратные π)
    x = np.linspace(-2, 2, 1000)
    x = x[np.abs(np.sin(x)) > 0.1]  # Исключаем окрестности разрывов

    y = f_x(x)

    # Строим график
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=r"$f(x) = \cot(x) - x^2$", color="b")

    # Добавляем оси
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Настройки
    plt.ylim(-3, 3)
    plt.xlim(-3, 3)
    plt.legend()
    plt.grid(True)
    plt.title("График функции $f(x) = \cot(x) - x^2$")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # Показать график
    plt.show()