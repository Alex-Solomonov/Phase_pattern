import numpy as np
import scipy.optimize
import scipy.special


def Kotlyar(amplitude, phase):
	sizes = np.shape(phase)

	new_phase = np.empty([2*sizes[0], 2*sizes[1]], float)
	u = np.empty([sizes[0], sizes[1]], float)
	v = np.empty([sizes[0], sizes[1]], float)
	
	u = phase + np.arccos(amplitude/2)
	v = phase - np.arccos(amplitude/2)


	for i in range(sizes[0]):
		for j in range(sizes[1]):
			new_phase[2*i, 2*j] = new_phase[2*i+1, 2*j+1] = u[i,j]
			new_phase[2*i, 2*j+1] = new_phase[2*i+1, 2*j] = v[i,j]

	new_phase = np.angle(np.exp(1j*new_phase), deg=True)
	return new_phase

def sinc(x):
	return np.sin(np.pi*x)/(np.pi*x)



def Arrison_CGH1(amplitude, phase):
	sizes = np.shape(phase)
	encoded_amplitude = np.empty([sizes[0], sizes[1]], float)

	def fun_CGH1(x, amplitude):
		return sinc(1-x) - amplitude

	for i in range(sizes[0]):
		for  j in range(sizes[0]):
			sol = scipy.optimize.minimize(lambda x: fun_CGH1(x, amplitude[i,j]), x0 = 1e-03)
			encoded_amplitude[i, j] = sol.x[0]

	new_phase = encoded_amplitude*phase
	new_phase = np.angle(np.exp(1j*new_phase), deg=True)
	return new_phase


def Arrison_CGH2(amplitude, phase):
	sizes = np.shape(phase)
	encoded_amplitude = np.empty([sizes[0], sizes[1]], float)

	def fun_CGH2(x, amplitude):
		return scipy.special.jv(0, x) - amplitude


	for i in range(sizes[0]):
		for  j in range(sizes[0]):
			sol = scipy.optimize.minimize(lambda x: fun_CGH2(x, amplitude[i,j]), x0 = 1e-03)
			encoded_amplitude[i, j] = sol.x[0]

	new_phase = phase + encoded_amplitude*np.sin(phase)

	new_phase = np.angle(np.exp(1j*new_phase), deg=True)
	return new_phase

def Arrison_CGH3(amplitude, phase):
	sizes = np.shape(phase)
	encoded_amplitude = np.empty([sizes[0], sizes[1]], float)

	def fun_CGH3(x, amplitude):
		return scipy.special.jv(1, x) - amplitude


	for i in range(sizes[0]):
		for  j in range(sizes[0]):
			sol = scipy.optimize.minimize(lambda x: fun_CGH3(x, amplitude[i,j]), x0 = 1e-03)
			encoded_amplitude[i, j] = sol.x[0]

	new_phase = encoded_amplitude*np.sin(phase)

	new_phase = np.angle(np.exp(1j*new_phase), deg=True)
	return new_phase

def Arrison_Phase_carrier(amplitude, phase):
	new_phase = 0
	new_phase = np.angle(np.exp(1j*new_phase), deg=True)
	return new_phase
