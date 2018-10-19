"""
Test renderer for point generation
"""

from typing import Sequence, Iterable, TypeVar
import matplotlib.pyplot as plt
from genline import gen_point, edge_points
import sys


T = TypeVar('T')


def transpose(arr: Iterable[Sequence[T]]) -> Sequence[Sequence[T]]:
    """
    Transposes 2d sequence. Useful for getting lists of x and y coordinate from
    a list of points.

    >>> transpose([(1, 2), (3, 4), (5, 6)])
    ((1, 3, 5), (2, 4, 6))
    """
    return tuple(zip(*arr))


def main():
    amt = int(sys.argv[1])
    # point test
    fig, ax = plt.subplots()

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')

    ax.add_artist(plt.Circle((0, 0), 1, fill=False))
    pts = transpose(gen_point() for _ in range(amt))
    plt.plot(pts[0], pts[1], '.', markersize=1)

    plt.show()


if __name__ == '__main__':
    main()
