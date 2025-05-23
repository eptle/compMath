import matplotlib.pyplot as plt
import numpy as np


def urmat(ux0, ux1, ut0, ut1, d, h, tau):
    x = np.arange(0, 1 + h, h)
    t = np.arange(0, 10 + tau, tau)
    u = np.zeros((len(x), len(t)))
    for i in range(len(x)):
        u[i][0] = ux0(x[i])
        u[i][1] = tau * ux1(x[i]) + u[i][0]
    for j in range(len(t)):
        u[0][j] = ut0(t[j])
        u[-1][j] = ut1(t[j])
    l = ((d * tau / h)**2) / 2
    for j in range(1, len(t) - 1):
        D = [u[0][j + 1]]
        for i in range(1, len(x) - 1):
            D.append((1 + 2 * l) * u[i][j - 1] - l * (u[i + 1][j - 1] + u[i - 1][j - 1]) - 2 * u[i][j])
        a, b = [0], [1]
        for i in range(1, len(x) - 1):
            a.append(-l / (l * a[i - 1] - (1 + 2 * l)))
            b.append((D[i] - l * b[i - 1]) / (l * a[i - 1] - (1 + 2 * l)))
        for i in range(len(x) - 2, 0, -1):
            u[i][j + 1] = a[i] * u[i + 1][j + 1] + b[i]

    X, T = np.meshgrid(x, t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, u.T, cmap='plasma')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('U(x, t)')
    plt.show()


ux0 = lambda x: 1 - x
ux1 = lambda x: 1
ut0 = lambda t: 1
ut1 = lambda t: 0
D = 1
h = 0.1
tau = 0.01
urmat(ux0, ux1, ut0, ut1, D, h, tau)
