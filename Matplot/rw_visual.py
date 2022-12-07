import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw = RandomWalk(50)
    rw.fill_walk()
    # plt.figure(dpi=300, figsize=(20, 10))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, color='black', linewidth=1)
    plt.scatter(rw.x_values, rw.y_values, c='none', edgecolors='black', s=15)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # plt.axes = 'none'
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break