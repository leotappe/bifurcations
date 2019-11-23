"""
Task 1/5
"""
import numpy as np
import matplotlib.pyplot as plt


def create_book_figure():
    """
    Create figures similar to Fig. 2.5 from
    https://www.springer.com/de/book/9780387219066
    """
    vector_fields = [node, focus, saddle]

    fig, axes = plt.subplots(nrows=1, ncols=len(vector_fields))
    fig.suptitle('Figure similar to Fig 2.5 from Kuznetsov book')

    alpha = 1
    xs = 10
    ys = 10
    X = np.linspace(-1, 1, xs)
    Y = np.linspace(-1, 1, ys)
    X, Y = np.meshgrid(X, Y)
    U = np.zeros((xs, ys))
    V = np.zeros((xs, ys))

    for v, ax in zip(vector_fields, axes):
        for i in range(xs):
            for j in range(ys):
                xy = np.array([X[i, j], Y[i, j]])
                uv = v(xy, alpha)
                U[i, j] = uv[0]
                V[i, j] = uv[1]

        ax.set_aspect('equal')
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.streamplot(X, Y, U, V)

    plt.show()


def create_assignment_figure(xlim=(-1, 1), ylim=(-1, 1), samples=16):
    """
    Create the phase portraits from the problem sheet.
    """
    alphas = [0.1, 0.5, 2.0, 10.0]

    fig, axes = plt.subplots(nrows=1, ncols=len(alphas))
    fig.suptitle('Phase diagrams for system from problem sheet')

    t = 10000
    dt = 0.01
    x_min, x_max = xlim
    y_min, y_max = ylim
    X1 = np.linspace(x_min, x_max, samples)
    X2 = np.linspace(y_min, y_max, samples)
    X1, X2 = np.meshgrid(X1, X2)
    dX1 = np.zeros((samples, samples))
    dX2 = np.zeros((samples, samples))

    for alpha, ax in zip(alphas, axes):
        for i in range(samples):
            for j in range(samples):
                x = np.array([X1[i, j], X2[i, j]])
                dx = derivative(x, alpha)
                dX1[i, j] = dx[0]
                dX2[i, j] = dx[1]

        ax.set_title(rf'$\alpha$ = {alpha}')
        ax.set_aspect('equal')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_xlabel(r'$x_1$')
        ax.set_ylabel(r'$x_2$')
        ax.quiver(X1, X2, dX1, dX2)

        x = np.array([0.01, -0.01])
        X1_orbit = [x[0]]
        X2_orbit = [x[1]]

        for i in range(t):
            x += dt * derivative(x, alpha)
            if x[0] > x_max or x[0] < x_min or x[1] > y_max or x[1] < y_min:
                break
            X1_orbit.append(x[0])
            X2_orbit.append(x[1])

        ax.plot(X1_orbit, X2_orbit, 'r')

    plt.show()


def derivative(x, alpha):
    """
    Equation (5) from the problem sheet.
    """
    A = np.array([[alpha, alpha], [-0.25, 0]])
    return A @ x


def node(x, alpha):
    A = np.array([[alpha, 0], [0, 2 * alpha]])
    return A @ x


def focus(x, alpha):
    A = np.array([[0, -2.89], [1, -1.6]])
    return A @ x


def saddle(x, alpha):
    A = np.array([[alpha, 0], [0, -alpha]])
    return A @ x


if __name__ == '__main__':
    create_assignment_figure()
    create_book_figure()
