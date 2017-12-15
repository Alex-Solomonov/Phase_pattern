import numpy as np

def Kotlyar(amplitude, phase):
	sizes = np.shape(phase)

	new_phase = np.empty([2*sizes[0], 2*sizes[1]], float)

	for i in range(sizes[0]):
		for j in range(sizes[1]):
			new_phase[2*i, 2*j] = new_phase[2*i+1, 2*j+1] = phase[i,j] + np.arccos(amplitude[i,j]/2)
			new_phase[2*i, 2*j+1] = new_phase[2*i+1, 2*j] = phase[i,j] - np.arccos(amplitude[i,j]/2)

			for k in range(1):
				for n in range(1):
					if new_phase[2*i+k, 2*j+n] > np.pi:
						new_phase[2*i+k, 2*j+n] = new_phase[2*i+k, 2*j+n] - 2*np.pi
					if new_phase[2*i+k, 2*j+n] < -np.pi:
						new_phase[2*i+k, 2*j+n] = new_phase[2*i+k, 2*j+n] + 2*np.pi

	return new_phase