
import sys
import fasterPizza
import Pizza
import time
count = 0
tally = 0

n = 100
fastertime = time.time()
for j in range(0, 10):
    fastertime = time.time()
    for i in range(n):
        count += fasterPizza.calculateAndReturnVertices(j * 100)[0]
    sys.stdout.write("faster: " + str(time.time() - fastertime) + " " + str(count / n) + "\n")

normaltime = time.time()
#for i in range(n):
    #tally += Pizza.Pizza.main()
sys.stdout.write("normal: " + str(time.time() - normaltime) + " " + str(tally / n))