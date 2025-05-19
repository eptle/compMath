import matplotlib.pyplot as plt
import numpy as np


def urmat(a, b, uxc, uxd, uay, uby, f, step, eps):
    h = (b - a) / (step - 1)
    x = np.arange(a, b + h, h)
    y = np.arange(c, d + h, h)
    u = np.zeros((len(x), len(y)))
    v = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        u[i][0] = uxc(x[i])
        u[i][-1] = uxd(x[i])
    for j in range(len(y)):
        u[0][j] = uay(y[j])
        u[-1][j] = uby(y[j])
    M = float('inf')
    iterations = 0
    while M >= eps:
        M = 0
        for i in range(1, len(x) - 1):
            for j in range(1, len(y) - 1):
                v[i][j] = (u[i + 1][j] + u[i - 1][j] + u[i][j + 1] + u[i][j - 1] - h**2 * f(x[i], y[j])) / 4
                M = max(M, np.linalg.norm(u[i][j] - v[i][j]))
        u = v.copy()
        iterations += 1
    print(iterations)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, u.T, cmap='plasma')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('U(x, y)')
    plt.show()


a, b = 0, 10
c, d = a, b
uxc = lambda x: x + c
uxd = lambda x: x + d
uay = lambda y: a + y
uby = lambda y: b + y
f = lambda x, y: 3 * x + y
epsilon = 0.01
urmat(a, b, uxc, uxd, uay, uby, f, 5, epsilon)
urmat(a, b, uxc, uxd, uay, uby, f, 10, epsilon)
