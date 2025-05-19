from math import log, sin

def eiler(a, b, y0, z0, f, eps, count):
    n = 2
    last_y = [y0]
    last_z = [z0]
    x = []
    while True:
        h = (b - a) / n
        x = [a]
        y = [y0]
        z = [z0]
        for i in range(n):
            y.append(y[i] + h * z[i])
            z.append(z[i] + h * f(x[i], y[i - 1]))
            x.append(x[i] + h)
        max_diff_y_and_z = 0
        for i in range(n // 2):
            max_diff_y_and_z = max(max_diff_y_and_z, abs(last_y[i] - y[2 * i]), abs(last_z[i] - z[2 * i]))
        if max_diff_y_and_z < eps and log(n, 2) > 2:
            return y[:count], z[:count], x[:count]
        last_y = y
        last_z = z
        n *= 2


def adams3(yn, zn, xn, b, f, eps):
    n = 2
    last_y = yn[:]
    last_z = zn[:]
    x = xn[:]
    while True:
        x = xn[:]
        h = (b - xn[2]) / n
        y = yn[:]
        z = zn[:]
        for i in range(2, n + 2):
            x.append(x[i] + h)
            y.append(y[i] + h * (23 * z[i] - 16 * z[i - 1] + 5 * z[i - 2]) / 12)
            z.append(z[i] + h * (23 * f(x[i], y[i]) - 16 * f(x[i - 1], y[i - 1]) + 5 * f(x[i - 2], y[i - 2])) / 12)
        max_diff_y_and_z = 0
        for i in range(n // 2):
            max_diff_y_and_z = max(max_diff_y_and_z, abs(last_y[i + 2] - y[2 * i + 2]), abs(last_z[i + 2] - z[2 * i + 2]))
        if max_diff_y_and_z < eps and log(n, 2) > 2:
            break
        last_y = y
        last_z = z
        n *= 2
    
    print("16 последних значений последней итерации:")
    for i in range(len(x) - 16, len(x)):
        print(round(x[i], 4))
    print("8 значений функции предпоследней итерации:")
    for i in range(len(last_y) - 8, len(last_y)):
        print(round(last_y[i], 4))
        print('-')
    print("16 значений функции последней итерации:")
    for i in range(len(y) - 16 , len(y)):
        print(round(y[i], 4))
    print("Разность значений между последней и предпоследней итерацией:")
    for i in range(8):
        print(round(abs(last_y[-i - 1] - y[- 2 * i - 1]), 5))
        print('-')
    print("Количество разбиений на последней итерации:", len(x))


def f(x, y):
    return 1 - sin(x + y)

print('Адамс 3 порядок')
a, b = 0, 0.5
y0, z0 = 0, 1
eps = 0.001
yn, zn, xn = eiler(a, b, y0, z0, f, eps, 3)
adams3(yn, zn, xn, b, f, eps)
