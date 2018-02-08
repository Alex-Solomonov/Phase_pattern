import numpy as np

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