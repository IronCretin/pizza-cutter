import random
import math
import sys
def calculateAndReturnVertices(n):
    #In my code i use this array to store, for each line, a set that contains lines that intersect with it
    #The code also doesn't allow the same intersections to be in two different sets
    arrayOfSetsOfIntersects = []
    #in the 
    setOfActiveSets = set()

    for i in range(n):
        arrayOfSetsOfIntersects += [set()]


    #generate points

    dictOfLineIds = {}
    arrayOfPointAngles = []
    pi = math.pi

    for i in range(n):
        angle1 = random.random() * 2 * pi
        angle2 = random.random() * 2 * pi
        dictOfLineIds[min(angle1, angle2)] = (0, i)
        dictOfLineIds[max(angle1, angle2)] = (1, i)
        arrayOfPointAngles += [angle1] + [angle2]

    arrayOfPointAngles.sort()

    for a in arrayOfPointAngles:
    #sys.stdout.write(str(setOfActiveSets))
        if (dictOfLineIds[a][0] == 0): 
            for s in setOfActiveSets:          
                arrayOfSetsOfIntersects[s].add(dictOfLineIds[a][1])
            setOfActiveSets.add(dictOfLineIds[a][1])
        else:
            setOfActiveSets.remove(dictOfLineIds[a][1])
            for s in setOfActiveSets:
                arrayOfSetsOfIntersects[s].discard(dictOfLineIds[a][1])
    #sys.stdout.write(str(arrayOfSetsOfIntersects))

    sys.stdout.write("Vertices: ")
    count = 2*n

    for s in arrayOfSetsOfIntersects:
        count += len(s)
    return count
def printverts(n = 3):
    sys.stdout.write("Vertices: " + str(calculateAndReturnVertices(n)))
if __name__ == '__main__':
	printverts()
	