from fasterPizza import calcshiz
import sys
import time
from collections import Counter


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
        print(f'{n:2>}: {100*amt/runs:2.2f}% ' +
            f'{"#"*(width*amt//big):<{width+5}} | {amt}')

    print(f'Completed in {end-start} sec')



if __name__ == '__main__':
    main()