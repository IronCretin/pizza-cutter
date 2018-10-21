
import sys
import fasterPizza
import Pizza
import time
import math
def main():
    count = 0
    tally = 0
    """
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
    """
    n = 2
    count;
    numberThrees = 0
    numberFours = 0

    for i in range(1000000):
        verts = fasterPizza.calculateAndReturnVertices(n)[0]
        faces = 1 - verts + 3*n + 2 * (verts - 2*n)
        count += faces
        if (faces == 3):
            numberThrees += 1
        if (faces == 4):
            numberFours += 1
    sys.stdout.write("average: " + str(count / 1000000)+ " PercentThree: " + str(numberThrees/1000000) + " PercentFours: " + str(numberFours/1000000) )

    """
    
    for n in range(1, 20):
        fasterdata = fasterPizza.calculateAndReturnVertices(n)

        arrayOfLines = []
        for i in fasterdata[1]:
            arrayOfLines += [((math.cos(i[0]), math.sin(i[0])),(math.cos(i[1]), math.sin(i[1])))]
    #sys.stdout.write("\n" + str(len(arrayOfLines))+"\n")

        normalverts = Pizza.Pizza.main(arrayOfLines, n)
        fasterverts = fasterdata[0]

        #sys.stdout.write(str(normalverts) + " " + str(fasterverts)+"\n")
        if (normalverts != fasterverts):
            raise EnvironmentError
    sys.stdout.write("success!")
    """

if __name__ == '__main__':
    main()					
	