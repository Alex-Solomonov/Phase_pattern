import numpy as np
import Approx_equation as eq
def Move(array, x, y):
	'''
	Input ndarray
	x - move to the left
	y - move to the down

	Output ndarray
	'''
	array = np.roll(array, -x, axis = 1)
	array = np.roll(array, -y, axis = 0)

	return(array)

def Prism_x(array, x):
	size = np.shape(array)

	prism = np.zeros_like(array)
	for i in range(size[0]):
		prism[i] = np.linspace(0,x*np.pi,size[1])

	array += prism
	array = np.angle(np.exp(1j*array), deg=True)

	return array

def interference(r, amplitude, phase):
	amplitude_G, phase = eq.Bessel(r, phase, 0)
	u = np.zeros_like(amplitude).astype('complex')
	u = amplitude_G + amplitude*np.exp(1j*phase)

	amplitude = abs(u)
	phase = np.arctan2(np.imag(u),np.real(u))

	return amplitude, phase