"""
Test renderer for point generation
"""

import matplotlib.pyplot as plt
import numpy as np
from genline import gen_point
import sys


def main():
    amt = int(sys.argv[1])
    # point test
    fig, ax = plt.subplots()

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')

    ax.add_artist(plt.Circle((0, 0), 1, fill=False))
    pts = np.vstack([gen_point() for _ in range(amt)]).T
    plt.plot(pts[0], pts[1], '.', markersize=1, alpha=.5)

    plt.show()


if __name__ == '__main__':
    main()
