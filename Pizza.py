
import random
import math
import sys

class Pizza:
	def findIntersectionXValueBetweenFunc_iAndFunc_j(m1, m2, x1, x2, y1, y2):
		return ((y1 - y2) + (m2 * x2) - (m1 * x1)) / (m2 - m1)

	def findYValueFromXValueAndEquation(x, m, x1, y1):
		return m * (x - x1) + y1

	def checkIfInUnitCircle(t):
		return (t[0] * t[0] + t[1] * t[1]) < 1

	n = 3

	arrayOfLines = []
	for i in range(0, n):
		
		x1 = math.cos(random.random()*2*math.pi)
		y1 = math.sin(random.random()*2*math.pi)
		x2 = math.cos(random.random()*2*math.pi)
		y2 = math.sin(random.random()*2*math.pi)

		arrayOfLines += [((x1, y1),(x2,y2))]
	
	arrayOfSlopes = []

	vertices = 2 * len(arrayOfLines)
	edges = 2 * len(arrayOfLines)

	for i in range(0, len(arrayOfLines)):
		dx = arrayOfLines[i][0][0] - arrayOfLines[i][1][0]
		dy = arrayOfLines[i][0][1] - arrayOfLines[i][1][1]
		m = dy / dx 
		arrayOfSlopes += [m]

	for i in range(0, len(arrayOfLines)):
		for j in range(0, len(arrayOfLines)):
			if (arrayOfLines[i] == arrayOfLines[j]):
				continue
			else:
				m1 = arrayOfSlopes[i]
				m2 = arrayOfSlopes[j]

				x1 = arrayOfLines[i][0][0]
				x2 = arrayOfLines[j][0][0]

				y1 = arrayOfLines[i][0][1]
				y2 = arrayOfLines[j][0][1]

				x = findIntersectionXValueBetweenFunc_iAndFunc_j(m1, m2, x1, x2, y1, y2)
				y = findYValueFromXValueAndEquation(x, m1, x1, y1)

				p = (x, y)
				#sys.stdout.write(str(p[0]) + " " + str(p[1]) + "     ")
				if (checkIfInUnitCircle(p)):
					vertices += 1
					edges += 2

				
	sys.stdout.write(str(vertices))
	sys.stdout.write(str(edges))
					
	


