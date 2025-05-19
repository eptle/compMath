import matplotlib.pyplot as plt
import numpy as np


def urmat(ux0, ut0, ut1, D, h, tau):
    x = np.arange(0, 1 + h, h)
    t = np.arange(0, 10 + tau, tau)
    u = np.zeros((len(x), len(t)))
    for i in range(len(x)):
        u[i][0] = ux0(x[i])
    for j in range(len(t)):
        u[0][j] = ut0(t[j])
        u[-1][j] = ut1(t[j])
    l = D * tau / h**2
    for j in range(0, len(t) - 1):
        for i in range(1, len(x) - 1):
            u[i][j + 1] = l * u[i + 1][j] + (1 - 2 * l) * u[i][j] + l * u[i - 1][j]
    X, T = np.meshgrid(x, t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, u.T, cmap='plasma')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('U(x, t)')
    plt.show()


ux0 = lambda x: 1 - x
ut0 = lambda t: 1
ut1 = lambda t: 0
D = 1
h = 0.1
tau = 0.001
urmat(ux0, ut0, ut1, D, h, tau)
