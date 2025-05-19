import matplotlib.pyplot as plt
import numpy as np


def urmat(ux0, ut1, f, a, h):
    x = np.arange(0, 1 + h, h)
    tau = - h / a
    t = np.arange(0, 10 + tau, tau)
    u = np.zeros((len(x), len(t)))

    for i in range(len(x)):
        u[i][0] = ux0(x[i])

    for i in range(len(x) - 2, -1, -1):
        for j in range(len(t)):
            u[-1][j] = ut1(t[j])
        for j in range(len(t) - 1):
            u[i][j + 1] = u[i][j] - (a * tau / h) * (u[i + 1][j] - u[i][j]) + tau * f(x[i], t[j])

    x, T = np.meshgrid(x, t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, T, u[:].T, cmap='plasma')

    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('U(x, t)')

    plt.show()



ux0 = lambda x: x**2 - 2
f = lambda x, t: 2 * x
ut = lambda t: t**2 - 1
a = -2
h = 0.1
urmat(ux0, ut, f, a, h)
