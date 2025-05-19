import matplotlib.pyplot as plt
import numpy as np


def urmat(ux0, a, b, c, d, h, tau, eps):
    x = np.arange(a, b + h, h)
    t = np.arange(c, d + tau, tau)
    u = np.zeros((len(x), len(t)))
    for i in range(len(x)):
        u[i][0] = ux0(x[i])
    for j in range(len(t) - 1):
        for i in range(1, len(x) - 1):
            u[i][j + 1] = (u[i][j] - (tau / h) * u[i][j] * (u[i][j] - u[i - 1][j]) - (eps ** 2 * tau / 2 / h ** 3) *
                           (u[i + 1][j] - u[i - 1][j]) * (u[i + 1][j] - u[i][j] + u[i - 1][j]))
            u[len(x) - 1][j + 1] = u[i][j] - tau / h * u[i][j] * (u[i][j] - u[i - 1][j])
    T, X = np.meshgrid(t, x)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(T, X, u, cmap='plasma')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('U(x, t)')
    plt.show()


def ut0(x):
    if x < 0.5:
        return 2
    else:
        return 1


a, b = 0, 1
c, d = 0, 1
h = 0.01
tau = 0.001
epsilon = 0.01
urmat(ut0, a, b, c, d, h, tau, epsilon)
