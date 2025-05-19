import numpy as np
import math

# Заданное дифференциальное уравнение y' = cos(1 + x) - 0.5*y^2
def f(x, y):
    return math.cos(x + 1) - 0.5 * y**2
def runge(f, a, b, y0, epsilon):
    n = 2
    last_y = [y0]
    while True:
        h = (b - a)/n
        x, y = [a], [y0]
        for i in range(n):
            x.append(x[i] + h)
            k1 = f(x[i], y[i])
            k2 = f(x[i] + h / 2, y[i] + h * k1 / 2)
            k3 = f(x[i] + h / 2, y[i] + h * k2 / 2)
            k4 = f(x[i] + h, y[i] + h * k3)
            y_d = h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            y.append(y[i] + y_d)
            
        diffs = [abs(last_y[i] - y[2 * i]) for i in range(n//2)]

        if max(diffs) < epsilon and math.log(n, 2) > 3:
            for i in range(16):
                    if i % 2 == 0:
                        print(f'{x[-16+i]:<10.4f} {'-':<25} {y[-16+i]:<25.4f} {'-':<15}')
                    else:
                        print(f'{x[-16+i]:<10.4f} {last_y[-8+i//2]:<25.4f} {y[-16+i]:<25.4f} {last_y[-8+i//2]-y[-16+i]:<15.8f}')

            return len(x), h, f'{h**4:.8f}'
        last_y = y
        n *= 2


a, b = 0, 0.5
y0 = 0
epsilon = 0.001

print('Метод Рунге-Кутта')
print(f"{'x_k':<10}{'Y_k (предпосл. итерация)':<25}{'Y_k (послед. итерация)':<25}{'Разность':<15}")
print(runge(f, a, b, y0, epsilon))
