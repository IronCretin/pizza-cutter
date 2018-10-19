import matplotlib.pyplot as plt
import numpy as np
from genline import gen_point
import sys


def main():
    amt = int(sys.argv[1])
    # point test
    fig, ax = plt.subplots()
    
    plt.xlim(-.5, .5)
    plt.ylim(-.5, .5)
    plt.gca().set_aspect('equal', adjustable='box')

    ax.add_artist(plt.Circle((0, 0), .5, fill=False))
    pts = np.vstack([gen_point() for _ in range(amt)]).T
    plt.plot(pts[0], pts[1], 'o', markersize=1)

    plt.show()


if __name__ == '__main__':
    main()
