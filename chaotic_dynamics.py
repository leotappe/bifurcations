"""
Task 4/5
"""
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def plot_bifurcation_diagram():
    """
    Subtask 1:
    Bifurcation diagram fro logistic map.
    """
    R = np.linspace(0.001, 4)
    X = 1 - 1 / R

    fig, ax = plt.subplots()
    fig.suptitle('Bifurcation diagram for logistic map')
    ax.plot(R, X)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 1)
    ax.set_xlabel(r'$r$')
    ax.set_ylabel(r'$x$')

    plt.show()


def lorenz(sigma, rho, beta):
    """
    Create rhs of lorenz system with given parameters.
    """
    def fun(t, x):
        return np.array([
            sigma * (x[1] - x[0]),
            x[0] * (rho - x[2]) - x[1],
            x[0] * x[1] - beta * x[2]
        ])
    return fun


def plot_trajectories(sigma, rho, beta):
    """
    Subtask 2:
    Plot 2 trajectories of Lorenz system from slightly different initial values.
    """
    fun = lorenz(sigma, rho, beta)
    fig = plt.figure()
    fig.suptitle(rf'Lorenz system with $\sigma$ = {sigma}, $\rho$ = {rho}, $\beta$ = {beta}')
    ax = fig.gca(projection='3d')
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_zlabel(r'$z$')
    t_span = (0, 100)

    for x0 in [np.array([10.0, 10.0, 10.0]), np.array([10.0 + 10**(-8), 10.0, 10.0])]:
        bunch = solve_ivp(fun, t_span, x0)
        ax.plot(bunch.y[0, :], bunch.y[1, :], bunch.y[2, :], label=rf'$x_0$ = ({x0[0]}, {x0[1]}, {x0[2]})')

    ax.legend()
    plt.show()


if __name__ == '__main__':
    plot_bifurcation_diagram()
    plot_trajectories(10, 28, 8 / 3)
    plot_trajectories(10, 0.5, 8 / 3)
