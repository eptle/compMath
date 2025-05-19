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


def adams4(yn, zn, xn, b, f, eps):
    n = 2
    last_y = yn[:]
    last_z = zn[:]
    x = xn[:]
    while True:
        x = xn[:]
        h = (b - xn[3]) / n
        y = yn[:]
        z = zn[:]
        for i in range(3, n + 3):
            x.append(x[i] + h)
            y.append(y[i] + h * (55 * z[i] - 59 * z[i - 1] + 37 * z[i - 2] - 9 * z[i - 3]) / 24)
            z.append(z[i] + h * (55 * f(x[i], y[i]) - 59 * f(x[i - 1], y[i - 1]) \
                                 + 37 * f(x[i - 2], y[i - 2]) - 9 * f(x[i - 3], y[i - 3])) / 24)
        max_diff_y_and_z = 0
        for i in range(n // 2):
            max_diff_y_and_z = max(max_diff_y_and_z, abs(last_y[i + 3] - y[2 * i + 3]), abs(last_z[i + 3] - z[2 * i + 3]))
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
    print("разность значений:")
    for i in range(8):
        print(round(abs(last_y[-i - 1] - y[- 2 * i - 1]), 4))
        print('-')
    print("Количество разбиений :", len(x))

def f(x, y):
    return 1 + 0.4 * y * sin(x) - 3.5 * y**2

print('Адамс 4 порядок')
a, b = 0, 0.5
y0, z0 = 0, 1
eps = 0.001
yn, zn, xn = eiler(a, b, y0, z0, f, eps, 4)
adams4(yn, zn, xn, b, f, eps)
