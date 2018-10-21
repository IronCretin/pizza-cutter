from fasterPizza import calcshiz
import sys
import time
from collections import Counter
import matplotlib.pyplot as plt


def main():
    lines = int(sys.argv[1])
    runs = int(sys.argv[2])
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 30

    amts = Counter()

    start = time.perf_counter()
    for i in range(runs):
        amts[calcshiz(lines)[3]] += 1
    end = time.perf_counter()

    big = max(amts.values())

    for n, amt in sorted(amts.items()):
        print(f'{n:>2d}: {100*amt/runs:>5.2f}% ' +
            f'{"#"*(width*amt//big):<{width+5}} | {amt}')

    print(f'Completed in {end-start} sec')

    xs, ys = zip(*amts.items())

    plt.title(f'Number of slices for {lines} cuts')
    plt.xlabel('Slices')
    plt.ylabel('Probability')

    plt.bar(xs,[y/runs for y in ys])

    plt.show()


if __name__ == '__main__':
    main()