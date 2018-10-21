import random
import math
import sys
import matplotlib.pyplot as plt

class Pizza:
	def findIntersectionXValueBetweenFunc_iAndFunc_j(m1, m2, x1, x2, y1, y2):
		
		"""
		This Function finds the X Value of the intersection between the two lines
		m1 is line1's slope, m2 is line2's slope
		(x1, y1) is a point in line 1
		(x2, y2) is a point in line 2
		This equation is derived from systems of linear equations, the proof is left as an exercise to the reader
		"""
		return ((y1 - y2) + (m2 * x2) - (m1 * x1)) / (m2 - m1)

	def findYValueFromXValueAndEquation(x, m, x1, y1):
		"""
		Just find the corresponding y value to an x value, given the slope and a point in line, (x1, y1)
		"""
		return m * (x - x1) + y1

	def checkIfInUnitCircle(p):
		"""
		p is a tuple which represents a point, p[0] is x value, p[1] is the y value
		p is in the unit circle only if the square of x plus square of y is less than 1
		"""
		return (p[0] * p[0] + p[1] * p[1]) < 1

	#def GiveCurrentIntersectionsSet(x, IntersectionXs):
	#   """
	#   Given the set of x values of intersections found so far.
	#   return whether the new x value of the intersection is about the same
	#   I know its just the x value but x values being this close has low percent happening
	#   """
	#	for i in IntersectionXs:
	#		if (abs(i - x) < 0.0000000001):
	#			return IntersectionXs
	#	IntersectionXs.add(x)
	#	return IntersectionXs

	def giveListOfLines(n):
		"""
		Given the number of lines create a list of tuples of tuples of floats
		This array represents pairs of points which define a line in my code
		a random angle on the circle is picked for each point and trig does the rest
		"""
		arrayOfLines = []
		for i in range(0, n):
		
			theta1 = random.random()*2*math.pi
			x1 = math.cos(theta1)
			y1 = math.sin(theta1)

			theta2 = random.random()*2*math.pi			
			x2 = math.cos(theta2)
			y2 = math.sin(theta2)

			arrayOfLines += [((x1, y1),(x2, y2))]
		return arrayOfLines

	def GiveListOfSlopes(arrayOfLines):
		
		"""
		Remember tuple values are accessed just like arrays
		Each tuple in arrayOfLines has two tuples that represent the two points that define the line
		The slope for each line is found and recorded
		The slope is the difference between the y values divided by difference of x values
		"""
		arrayOfSlopes = []
		for i in range(len(arrayOfLines)):
			dx = arrayOfLines[i][0][0] - arrayOfLines[i][1][0]
			dy = arrayOfLines[i][0][1] - arrayOfLines[i][1][1]
			m = dy / dx 
			arrayOfSlopes += [m]
		return arrayOfSlopes

	
	def giveIntersectionPointBetweenLines_i_and_j(i, j, arrayOfSlopes, arrayOfLines):
		"""
		This finds the intersection between lines in arrayOfLines at indices i and j
		arrayOfSlopes stores the corresponding slopes at i and j
		remember arrayOfLines is a tuple of tuples of floats and values in tuples are accessed like arrays
		I read the coord values of the first and second point then feed into intersection coord finder functions
		"""
		m1 = arrayOfSlopes[i]
		m2 = arrayOfSlopes[j]

		x1 = arrayOfLines[i][0][0]
		x2 = arrayOfLines[j][0][0]

		y1 = arrayOfLines[i][0][1]
		y2 = arrayOfLines[j][0][1]

		x = Pizza.findIntersectionXValueBetweenFunc_iAndFunc_j(m1, m2, x1, x2, y1, y2)
		y = Pizza.findYValueFromXValueAndEquation(x, m1, x1, y1)

		return (x, y)
				
	def main():
		n = 3

		#IntersectionXs = set()
		arrayOfLines = []	
		arrayOfSlopes = []

		vertices = 0
		edges = 0

		#find all the lines and their slopes based on number of lines
		arrayOfLines = Pizza.giveListOfLines(n)		
		arrayOfSlopes = Pizza.GiveListOfSlopes(arrayOfLines)

		#For each line I will check every other line whether it intersects
		#for inner loop i start at i so that each pair of lines is checked once
		for i in range(0, len(arrayOfLines)):
			for j in range(i, len(arrayOfLines)):
				#do not find intersection of line with itself
				if (arrayOfLines[i] == arrayOfLines[j]):
					continue
				else:
					#Call intersection finding function
					p = Pizza.giveIntersectionPointBetweenLines_i_and_j(i, j, arrayOfSlopes, arrayOfLines)
					#If the intersection isn't in circle then it is useless
					if (Pizza.checkIfInUnitCircle(p)):
						pX = p[0]
						#originally update the number of intersections if it is a unique intersection
						#but realize redundant
						#IntersectionXs = Pizza.GiveCurrentIntersectionsSet(pX, IntersectionXs)

						#An intersection indicates one additional vertex and two more edges
						vertices += 1
						edges += 2

		#add six vertices for circle edges
		vertices += 6
		#add 6 edges for circle edges and 3 for original line edges
		# since intersections just add one per intersection
		Edges = edges + 9
		#euler alert
		Faces = 1 - vertices + Edges
		"""
		sys.stdout.write("Vertices: " + str(vertices) + "\n")
		sys.stdout.write("Edges: " + str(Edges) + "\n")
		sys.stdout.write("Faces: " + str(Faces) + "\n")

		print(arrayOfLines)

		fig, ax = plt.subplots()

		plt.xlim(-1, 1)
		plt.ylim(-1, 1)
		plt.gca().set_aspect('equal', adjustable='box')
		ax.add_artist(plt.Circle((0, 0), 1, fill=False, linewidth=.5))

		for l in arrayOfLines:
			plt.plot(*zip(*l))
		plt.show()
		"""
		return vertices


if __name__ == '__main__':
	Pizza.main()					
	


