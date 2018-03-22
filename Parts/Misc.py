import numpy as np
def move(array, x, y):
	'''
	Input ndarray
	x - move to the left
	y - move to the down

	Output ndarray
	'''
	array = np.roll(array, -x, axis = 1)
	array = np.roll(array, -y, axis = 0)

	return(array)

def prism_x(array, x):
	size = np.shape(array)

	prism = np.zeros_like(array)
	for i in range(size[0]):
		prism[i] = np.linspace(0,x*np.pi,size[1])

	array += prism
	array = np.angle(np.exp(1j*array), deg=True)

	return array

def get_amplitude(field):
	return np.abs(field)

def get_phase(field):
	return  np.arctan2(np.imag(field), np.real(field))