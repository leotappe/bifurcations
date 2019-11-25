"""
Task 5/5
"""
import os
import json
import matplotlib.pyplot as plt


def plot_coordinates_over_time(pedestrian_id=1):
    """
    Plot coordinates of specified pedestrian over time.
    """
    for directory, _, _ in os.walk('simulation_data'):
        if directory == 'simulation_data':
            continue

        with open(os.path.join(directory, 'Bottleneck bifurcation.scenario')) as file:
            scenario = json.load(file)
            y_obstacle = scenario['scenario']['topography']['obstacles'][0]['shape']['y']

        T, X, Y = [], [], []

        with open(os.path.join(directory, 'postvis.trajectories')) as file:
            _ = file.readline()

            for line in file.readlines():
                t, pid, x, y, _ = line.split()
                if int(pid) != pedestrian_id:
                    continue
                T.append(int(t))
                X.append(float(x))
                Y.append(float(y))

        fig, ax = plt.subplots()
        fig.suptitle(rf'Coordinates of pedestrian {pedestrian_id} with obstacle at $y$ = {y_obstacle}')
        ax.plot(T, X, label=r'$x$')
        ax.plot(T, Y, label=r'$y$')
        ax.legend()
        plt.show()


if __name__ == '__main__':
    plot_coordinates_over_time()
