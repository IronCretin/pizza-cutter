import random
import math
import sys
def calculateAndReturnVertices(n):
    #In my code i use this array to store, for each line, a set that contains lines that intersect with it
    #The code also doesn't allow the same intersections to be in two different sets
    arrayOfSetsOfIntersects = []

    #initialize a set for every line
    for i in range(n):
        arrayOfSetsOfIntersects += [set()]


    #will use a dictionary with an angle mapped to a tuple detailing which one it is
    dictOfLineIds = {}

    #need an array to quickly sort these angles smallest to largest for code to work
    arrayOfPointAngles = []

    pi = math.pi

 


    for i in range(n):
        #for each line, i, two angles are made
        angle1 = random.random() * 2 * pi
        angle2 = random.random() * 2 * pi

        #each angle has a separate entry in the dictionary
        #the dictionary stores a tuple storing two things:
        #whether it is smaller angle or not and the line # id
        dictOfLineIds[min(angle1, angle2)] = (0, i)
        dictOfLineIds[max(angle1, angle2)] = (1, i)

        #put angles in array of angles
        arrayOfPointAngles += [angle1] + [angle2]

    #code doesn't work unless we know we are going around the circle in one direction
    #ie the angles need to be in order
    arrayOfPointAngles.sort()

    #the gist of the scary show ahead is that:

    #in the array are sorted angles, half of which represent entry points to the circle and
    #half represent exit points. Ive made it so all entry points are smaller angles than exit points
    #so that they occur first powering the rest.

    #important realization:
    #when a line x enters it will only intersect with any lines which enter afterwards
    #and dont exit before line x exits

    #based on that simple truth of lines on a circle the code is as follows:

    #in the code I need setOfActiveLines to store lines which have entered but not exited yet
    setOfActiveLines = set()
    #for each angle a in my sorted array of angles, which each represent a point on the circle:
    for a in arrayOfPointAngles:
        #if this is the entry point of the respective line as the tuple in the dict tells me:
        if (dictOfLineIds[a][0] == 0): 

            #for each line s which it may be intersecting with
            for s in setOfActiveLines:   

                #add a's line id to set of lines that may intersect with s
                arrayOfSetsOfIntersects[s].add(dictOfLineIds[a][1])

            #now future lines may be able to intersect with a so add its line to active lines
            setOfActiveLines.add(dictOfLineIds[a][1])
        else:
            #if this is the exit point of the respective line as the tuple in the dict tells me
            #remove this line from active lines, it can no longer intersect with anything else
            setOfActiveLines.remove(dictOfLineIds[a][1])
            
            #for each active line, remove a's line because it exited before 
            #any of the active lines got a chance to so no active line has a possibility of
            #intersecting with a
            for s in setOfActiveLines:
                arrayOfSetsOfIntersects[s].discard(dictOfLineIds[a][1])
    #sys.stdout.write(str(arrayOfSetsOfIntersects))

    sys.stdout.write("Vertices: ")
    count = 2*n

    #the sum of all the intersections stored in array here is very much the number of vertices
    for s in arrayOfSetsOfIntersects:
        count += len(s)
    return count
def printshiz(n = 3):
    verts = calculateAndReturnVertices(n)
    edges = 3*n + 2*(verts - 2*n)
    faces = 1 - verts + edges
    sys.stdout.write("Vertices: " + str(verts) + "\n")
    sys.stdout.write("Edges: " + str(edges) + "\n")
    sys.stdout.write("Faces: " + str(faces) + "\n")

if __name__ == '__main__':
	printshiz()
	