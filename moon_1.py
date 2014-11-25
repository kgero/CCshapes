# Generate a set of points that represent half of Moon's object, radius 1
import rhinoscriptsyntax as rs

print "Hello Python!"

# quads is a dictionary where the keys are the integer names of the quadrilaterals
# and the values are tuples of the points that define the quadtrilateral
# (points should be in order such that I can draw a line between adjacent points
# and generate the quad)

# polys is a dictionary where the keys are the integer names of the quadrilaterals
# and the values are the tuples of the associated polynomials
# a polynomial tuple is the coefficient of:
# (the 0th term, the x term, the x^2 term, the y term, the xy term, the y^2 term)

# a point is a tuple of 3 values: (x, y, z)

# a line is a tuple of 2 points: ((x1,y1,z1),(x2,y2,z2))

# ------------- DEFINITION OF SURFACE ATTRIBUTES

quads = {13: ((0,2/3.0,0),(-.5,.5,0),(0,1,0),(.5,1,0)),
14: ((-2/3.0,0,0),(-.5,.5,0),(0,2/3.0,0),(-.25,.25,0)),
15: ((-.5,-.25,0),(-2/3.0,0,0),(-.25,.25,0),(-.2,0,0)),
10: ((-.5,-.25,0),(-.2,0,0),(0,0,0),(-.2,-.2,0)),
24: ((-1,-.5,0),(-1,0,0),(-.5,.5,0),(-2/3.0,0,0)),
25: ((-1,-.5,0),(-2/3.0,0,0),(-.5,-.25,0),(-2/3.0,-2/3.0,0)),
20: ((-2/3.0,-2/3.0,0),(-.5,-.25,0),(-.2,-.2,0),(-.25,-.5,0)),
21: ((-.25,-.5,0),(-.2,-.2,0),(0,0,0),(0,-.2,0)),
35: ((-1,-1,0),(-1,-.5,0),(-2/3.0,-2/3.0,0),(-.5,-1,0)),
30: ((-.5,-1,0),(-2/3.0,-2/3.0,0),(-.25,-.5,0),(0,-2/3.0,0)),
31: ((-.25,-.5,0),(0,-.2,0),(.25,-.25,0),(0,-2/3.0,0)),
32: ((0,-.2,0),(0,0,0),(.2,0,0),(.25,-.25,0)),
40: ((-.5,-1,0),(0,-2/3.0,0),(.5,-.5,0),(0,-1,0)),
41: ((0,-2/3.0,0),(.25,-.25,0),(2/3.0,0,0),(.5,-.5,0)),
42: ((.2,0,0),(.5,.25,0),(2/3.0,0,0),(.25,-.25,0)),
43: ((0,0,0),(.2,.2,0),(.5,.25,0),(.2,0,0)),
51: ((.5,-.5,0),(2/3.0,0,0),(1,.5,0),(1,0,0)),
52: ((.5,.25,0),(2/3.0,2/3.0,0),(1,.5,0),(2/3.0,0,0)),
53: ((.2,.2,0),(.25,.5,0),(2/3.0,2/3.0,0),(.5,.25,0)),
54: ((0,0,0),(0,.2,0),(.25,.5,0),(.2,.2,0)),
62: ((2/3.0,2/3.0,0),(.5,1,0),(1,1,0),(1,.5,0)),
63: ((.25,.5,0),(0,2/3.0,0),(.5,1,0),(2/3.0,2/3.0,0)),
64: ((0,.2,0),(-.25,.25,0),(0,2/3.0,0),(.25,.5,0)),
65: ((0,0,0),(-.2,0,0),(-.25,.25,0),(0,.2,0))}

polys = {13: (-.5, -1, -.5, 2, 1.5, -1.5),
14: (0, -.5, -.375, .5, .75, -.375),
15: (1/14.0, -2/7.0, -3/14.0, 1/7.0, 3/14.0, 1/14.0),
10: (1/12.0, -1/6.0, 1/12.0, 0, -.5, .5),
24: (-.5, -2, -1.5, 1, 1.5, -.5),
25: (0,-.5, -3/8.0, 0, 0, 0),
20: (1/14.0, -1/7.0, 1/14.0, -1/7.0, -5/14.0, 1/14.0),
21: (1/12, 0, .5, -1/6.0, -.5, 1/12.0),
35: (-.5, -1, -.5, -1, -.5, -.5),
30: (0, 0, 0, -.5, 0, -3/8.0),
31: (1/14.0, 1/7.0, 1/14.0, -2/7.0, 3/14.0, -3/14.0),
32: (1/12.0, 1/6.0, 1/12.0, -1/6.0, 1/3.0, 1/12.0),
40: (-.5, 1, -.5, -2, 1.5, -1.5),
41: (0, .5, -3/8.0, -.5, .75, -3/8.0),
42: (1/14.0, 2/7.0, -3/14.0, -1/7.0, 3/14.0, 1/14.0),
43: (1/12.0, 1/6.0, 1/12.0, 0, -.5, .5),
51: (-.5, 2, -1.5, -1, 1.5, -.5),
52: (0, .5, -3/8.0, 0, 0, 0),
53: (1/14.0, 1/7.0, 1/14.0, 1/7.0, -5/14.0, 1/14.0),
54: (1/12.0, 0, .5, 1/6.0, -.5, 1/12.0),
62: (-.5, 1, -.5, 1, -.5, -.5),
63: (0, 0, 0, .5, 0, -3/8.0),
64: (1/14.0, -1/7.0, 1/14.0, 2/7.0, 3/14.0, -3/14.0),
65: (1/12, -1/6.0, 1/12.0, 1/6.0, 1/3.0, 1/12.0)}

# ------------------ MAIN FUNCTION -----------------------

def getQuadPoints(quad):
	"""
	Returns a list of points within the quadrilateral defined by the four points given. 
	All points are in the x-y plane.
	"""
	allpoints = getAllPoints(.1)
	insidepoints = []
	pt1 = quad[0]
	pt2 = quad[1]
	pt3 = quad[2]
	pt4 = quad[3]

	for point in allpoints:
		ray = getRay(point)
		intersects = 0

		if checkIntersection(ray,(pt1,pt2)):
			intersects+= 1
		if checkIntersection(ray,(pt2,pt3)):
			intersects+= 1
		if checkIntersection(ray,(pt3,pt4)):
			intersects+= 1
		if checkIntersection(ray,(pt4,pt1)):
			intersects+= 1

		if intersects == 1:
			insidepoints.append(point)

	return insidepoints

# ------------------- UTILITIES --------------------------

def equation(polynomial, point):
	"""
	Returns the value of the polynomial at the point.
	"""
	if len(polynomial) != 6:
		raise TypeError('polynomial does not have the right number of terms.')

	x = point[0]
	y = point[1]

	term1 = polynomial[0]
	term2 = polynomial[1]*x
	term3 = polynomial[2]*x*x
	term4 = polynomial[3]*y
	term5 = polynomial[4]*x*y
	term6 = polynomial[5]*y*y
	
	return term1 + term2 + term3 + term4 + term5 + term6 


def plotQuad(quad, pointlist = None):
	"""
	Plots the quad. If a list of points is given, also plot the points.
	Use for visually confirming the results of getAllPoints and getQuadPoints.
	"""
	rs.AddLine(quad[0],quad[1])
	rs.AddLine(quad[1],quad[2])
	rs.AddLine(quad[2],quad[3])
	rs.AddLine(quad[3],quad[0])

	if pointlist:
		for pt in pointlist:
			rs.AddPoint(pt)

def getAllPoints(density):
	"""
	Returns a list of all points within the square (-1,-1) (1,1) at the given density,
	where density is the x and y distances between points.
	"""
	points = []
	i = -1
	while i < 1:
		j = -1
		while j < 1:
			points.append((i,j,0))
			j += density
		i += density
	return points


def getRay(point):
	"""
	Returns a line from the point to a point outside of the hexagon.
	"""
	return (point,(2,0,0))


def checkCCW(point1,point2,point3):
	"""
	Returns True if the points are listed in counterclockwise order, else returns False.
	"""
	return (point3[1]-point1[1])*(point2[0]-point1[0]) > (point2[1]-point1[1])*(point3[0]-point1[0])

def checkIntersection(line1,line2):
	"""
	Returns True if the lines intersect, False if they do not.
	From http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
	"""
	A = line1[0]
	B = line1[1]
	C = line2[0]
	D = line2[1]
	return checkCCW(A,C,D) != checkCCW(B,C,D) and checkCCW(A,B,C) != checkCCW(A,B,D)

# ------------------ SCRIPT FUNTIONALITY --------------------------

curvepoints = []
for key in quads:
	points = getQuadPoints(quads[key])
	for point in points:
		x = point[0]
		y = point[1]
		curvepoints.append((x,y,equation(polys[key],point)))
	
for point in curvepoints:
	rs.AddPoint(point)

rs.Command("_Patch")
# Select all points, go with default options

#plot the hexagon
rs.AddLine((0,1,0),(1,1,0))
rs.AddLine((1,1,0),(1,0,0))
rs.AddLine((1,0,0),(0,-1,0))
rs.AddLine((0,-1,0),(-1,-1,0))
rs.AddLine((-1,-1,0),(-1,0,0))
rs.AddLine((-1,0,0),(0,1,0))

# ------------------ WHAT TO DO IN RHINO --------------------------

# Edit/Trim using the hexagon lines (can use Edit/Select Objects/Lines)
# Solid/Extrude Solid/Straight to create solid (I used .02 thickness)
# If scaling:
	# Transform/Scale/Non-Uniform Scale
	# Pick origin as scaling point, enter integer x,y,z scaling factors
# Export as .stl, 0.005cm





	