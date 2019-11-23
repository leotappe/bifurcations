"""
Task 3/5
"""
from mpl_toolkits.mplot3d import Axes3D     # Do not remove, needed for 3D plot
import numpy as np
import matplotlib.pyplot as plt


def andronov_hopf_phase_diagrams(xlim=(-1, 1), ylim=(-1, 1), x1s=20, x2s=20):
    """
    Subtask 1:
    Visualize Andronov-Hopf bifurcation by plotting three phase diagrams at
    representative values of alpha.
    """
    alphas = [-1, 0, 1]
    fig, axes = plt.subplots(nrows=1, ncols=len(alphas))
    fig.suptitle('Andronov-Hopf phase diagrams')

    x1_min, x1_max = xlim
    x2_min, x2_max = ylim
    X1 = np.linspace(x1_min, x1_max, x1s)
    X2 = np.linspace(x2_min, x2_max, x2s)
    X1, X2 = np.meshgrid(X1, X2)
    dX1 = np.zeros((x1s, x2s))
    dX2 = np.zeros((x1s, x2s))

    for alpha, ax in zip(alphas, axes):
        for i in range(x1s):
            for j in range(x2s):
                x = np.array([X1[i, j], X2[i, j]])
                dx = andronov_hopf(x, alpha)
                dX1[i, j] = dx[0]
                dX2[i, j] = dx[1]

        ax.set_title(rf'$\alpha$ = {alpha}')
        ax.set_aspect('equal')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_xlabel('$x_1$')
        ax.set_ylabel('$x_2$')
        ax.streamplot(X1, X2, dX1, dX2)

    plt.show()


def andronov_hopf_orbits():
    """
    Subtask 2:
    Visualize two orbits in Andronov-Hopf system for alpha = 1 using Euler's
    method.
    """
    alpha = 1
    dt = 0.01
    num_steps = 1000
    initial_points = [np.array([2.0, 0.0]), np.array([0.5, 0.0])]
    fig, ax = plt.subplots()
    fig.suptitle(rf'Orbits in Andronov Hopf system for $\alpha$ = {alpha}')
    ax.set_xlabel(r'$x_1$')
    ax.set_ylabel(r'$x_2$')

    for x0 in initial_points:
        ax.annotate(xy=x0, s=rf'$x_0$ = ({x0[0]}, {x0[1]})')
        X1, X2 = orbit(x0, lambda x: andronov_hopf(x, alpha), dt, num_steps)
        ax.plot(X1, X2)

    plt.show()


def cusp_bifurcation_surface():
    """
    Subtask 3:
    Visualize the bifurcation surface of the cusp bifurcation.
    We're using a scatter plot instead of a surface plot as there may be
    multiple values for x given alpha1 and alpha2 s.t. the derivative is 0.
    """
    alphas = np.linspace(-1, 1)
    alpha1s = []
    alpha2s = []
    xs = []

    fig = plt.figure()
    fig.suptitle('Cusp bifurcation surface')
    ax = fig.add_subplot(projection='3d')

    for alpha1 in alphas:
        for alpha2 in alphas:
            for x in np.roots([-1, 0, alpha2, alpha1]):
                if np.isreal(x):
                    alpha1s.append(alpha1)
                    alpha2s.append(alpha2)
                    xs.append(np.real(x))

    ax.set_xlabel(r'$\alpha_1$')
    ax.set_ylabel(r'$\alpha_2$')
    ax.set_zlabel(r'$x$')
    ax.scatter(alpha1s, alpha2s, xs)
    plt.show()


def orbit(x, v, dt, num_steps):
    """
    Generate an orbit starting at x using Euler's method.
    """
    X1, X2 = [x[0]], [x[1]]

    for _ in range(num_steps):
        x += dt * v(x)
        X1.append(x[0])
        X2.append(x[1])

    return np.array(X1), np.array(X2)


def andronov_hopf(x, alpha):
    """
    Equation (8) from the problem sheet.
    """
    x1, x2 = x
    dx1 = alpha * x1 - x2 - x1 * (x1**2 + x2)**2
    dx2 = x1 + alpha * x2 - x2 * (x1**2 + x2)**2
    return np.array([dx1, dx2])


if __name__ == '__main__':
    andronov_hopf_phase_diagrams()
    andronov_hopf_orbits()
    cusp_bifurcation_surface()
