import matplotlib.pyplot as plt
from genline import gen_point
import sys


def main():
    amt = int(sys.argv[1])
    print('boff')
    # point test
    fig, ax = plt.subplots()
    
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')

    ax.add_artist(plt.Circle((0.5, 0.5), 0.5, fill=False))

    plt.show()


if __name__ == '__main__':
    main()
