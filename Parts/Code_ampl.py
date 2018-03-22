import numpy as np
import scipy.optimize
import scipy.special
import Parts


def Kotlyar(field):
	# Init par's
	sizes = np.shape(field)
	amplitude = Parts.Misc.get_amplitude(field)
	phase = Parts.Misc.get_phase(field)

	pattern = np.empty([2*sizes[0], 2*sizes[1]], float)
	
	u = phase + np.arccos(amplitude/2)
	v = phase - np.arccos(amplitude/2)


	for i in range(sizes[0]):
		for j in range(sizes[1]):
			pattern[2*i, 2*j] = pattern[2*i+1, 2*j+1] = u[i,j]
			pattern[2*i, 2*j+1] = pattern[2*i+1, 2*j] = v[i,j]

	pattern = np.angle(np.exp(1j*pattern), deg=True)
	return pattern


def Fuentes(field, LSM_pars):
	# Init par's
	sizes = np.shape(field)
	amplitude = Parts.Misc.get_amplitude(field)
	phase = Parts.Misc.get_phase(field)

	random_mask = np.zeros_like(field)

	for i in range(sizes[0]):
		for j in range(sizes[1]):
			# rdn is selected as uniformly distributed in the range [0;1)
			rnd = np.random.rand(1,1)
			if amplitude[i,j] > rnd:
				random_mask[i,j] = 1

	noise_lvl = np.zeros_like(field)

	noise_like_signal = random_mask - amplitude

	diverging_element = Parts.eq.axicon(LSM_pars, cycle = 160)

	pattern = field \
		+ ((1-amplitude) - noise_like_signal) * diverging_element \
		+ noise_like_signal*np.exp(1j*phase)

	return pattern