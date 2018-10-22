from fasterPizza import calcshiz
import sys
import time
from collections import Counter
import matplotlib.pyplot as plt
import statistics
import scipy.stats as stats
import numpy as np


def main():
    lines = int(sys.argv[1])
    runs = int(sys.argv[2])
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 30

    amts = Counter()

    start = time.perf_counter()
    for i in range(runs):
        amts[calcshiz(lines)[3]] += 1

    big = max(amts.values())

    for n, amt in sorted(amts.items()):
        print(f'{n:>3d}: {100*amt/runs:>5.2f}% ' +
            f'{"#"*(width*amt//big):<{width+5}} | {amt}')

    els = [*amts.elements()]
    mean = statistics.mean(els)
    stdev = statistics.stdev(els, xbar=mean)
    skew = stats.skew(els)
    kurt = stats.kurtosis(els)
    print(f'Mean:     {mean}')
    print(f'Stddev:   {stdev}')
    print(f'Skewness: {skew}')
    print(f'Kurtosis: {kurt}')

    
    end = time.perf_counter()
    print(f'Completed in {end-start} sec')

    xs, ys = zip(*amts.items())
    # xx = np.linspace(min(xs)-1, max(xs)+1, 100)
    # norm = stats.norm.pdf(xx, mean, stdev)

    plt.title(f'Number of slices for {lines} cuts')
    plt.xlabel('Slices')
    plt.ylabel('Probability')

    plt.bar(xs,[y/runs for y in ys])

    # plt.plot(xx, norm, 'k')

    plt.show()


if __name__ == '__main__':
    main()