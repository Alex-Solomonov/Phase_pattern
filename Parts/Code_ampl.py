import numpy as np

def Kotlyar(amplitude, phase):
	u = np.zeros_like(amplitude)
	v = np.zeros_like(amplitude)
	new_phase = np.zeros_like(amplitude)

	for i in range(len(amplitude)):
		for j in range(len(amplitude)):
			if j % 2 == 0:
				u[i,j] = phase[i,j] + np.arccos(amplitude[i,j]/2)
				v[i,j] = 0

			else:
				u[i,j] = 0
				v[i,j] = phase[i,j] - np.arccos(amplitude[i,j]/2)

	new_phase = u + v

	return new_phase