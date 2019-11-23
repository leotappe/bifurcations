"""
Task 2/5
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_bifurcation_diagrams(xlim=(-1, 3), ylim=(-2, 2)):
    """
    Plot bifurcation diagrams for systems specified by equations (6) and (7) on
    the problem sheet.
    """
    alphas = np.linspace(-1, 3, 10000)
    x, y = [], []

    fig, (ax_first, ax_second) = plt.subplots(nrows=1, ncols=2)
    fig.suptitle('Bifurcation diagrams')

    for alpha in alphas:
        for equilibrium in equilibria_first_system(alpha):
            x.append(alpha)
            y.append(equilibrium)

    ax_first.set_aspect('equal')
    ax_first.set_title(r'$\alpha - x^2$')
    ax_first.set_xlabel(r'$\alpha$')
    ax_first.set_ylabel(r'x')
    ax_first.set_xlim(xlim)
    ax_first.set_ylim(ylim)
    ax_first.scatter(x, y)

    x, y = [], []

    for alpha in alphas:
        for equilibrium in equilibria_second_system(alpha):
            x.append(alpha)
            y.append(equilibrium)

    ax_second.set_aspect('equal')
    ax_second.set_title(r'$\alpha - 2x^2 - 2$')
    ax_second.set_xlabel(r'$\alpha$')
    ax_second.set_ylabel(r'x')
    ax_second.set_xlim(xlim)
    ax_second.set_ylim(ylim)
    ax_second.scatter(x, y, color='r')

    plt.show()


def equilibria_first_system(alpha):
    """
    Given some alpha, find all values for x such that equation (6) is 0.
    """
    if alpha < 0:
        return []
    if alpha == 0:
        return [0]
    return [np.sqrt(alpha), -np.sqrt(alpha)]


def equilibria_second_system(alpha):
    """
    Given some alpha, find all values for x such that equation (7) is 0.
    """
    if alpha < 2:
        return []
    if alpha == 2:
        return [0]
    return [np.sqrt((alpha - 2) / 2), -np.sqrt((alpha - 2) / 2)]


if __name__ == '__main__':
    plot_bifurcation_diagrams()
