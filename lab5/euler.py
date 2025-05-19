import math

# Заданное дифференциальное уравнение y' = cos(1 + x) - 0.5*y^2
def f(x, y):
    return math.cos(x + 1) - 0.5 * y**2

def euler(f, a, b, y0, epsilon):
    n = 2
    last_y = [y0]
    while True:
        h = (b - a)/n
        x, y = [a], [y0]
        for i in range(n):
            x.append(x[i] + h)
            y_t = y[i] + h * f(x[i], y[i])  # Метод Эйлера (предварительный шаг)
            y.append(y[i] + (h / 2) * (f(x[i], y[i]) + f(x[i], y_t)))  # Итоговый шаг

        diffs = [abs(y[i*2]-last_y[i]) for i in range(n//2)]

        if max(diffs) < epsilon and n > 4:
            for i in range(16):
                    if i % 2 == 0:
                        print(f'{x[-16+i]:<10.4f} {'-':<25} {y[-16+i]:<25.4f} {'-':<15}')
                    else:
                        print(f'{x[-16+i]:<10.4f} {last_y[-8+i//2]:<25.4f} {y[-16+i]:<25.4f} {diffs[-i//2]:<15.4f}')
            return len(x)
        last_y = y
        n *= 2

a, b = 0, 0.5
y0 = 0
epsilon = 0.001

print("Метод Эйлера-Коши:")
print(f"{'x_k':<10}{'Y_k (предпосл. итерация)':<25}{'Y_k (послед. итерация)':<25}{'Разность':<15}")
print('Количество итераций:', euler(f, a, b, y0, epsilon))
