import numpy as np

def Generate(x_max, y_max, points_at_x, points_at_y):
	x = np.linspace(-x_max, x_max, points_at_x)
	y = np.linspace(-y_max, y_max, points_at_y)

	return Coord2Cylinder(x, y)


def Coord2Cylinder(x, y):
	r = np.empty([len(x), len(y)], float)
	theta = np.zeros_like(r)

	for i in range(len(x)):
		for j in range(len(y)):
			r[i,j] = (x[i]**2 + y[j]**2)**.5
			theta[i,j] = np.arctan2(y[j], x[i])

	return r, theta+np.pi
