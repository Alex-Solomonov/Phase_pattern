import numpy as np
import scipy.optimize
import scipy.special
import scipy.fftpack
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

	diverging_element = Parts.Field_equation.axicon(LSM_pars, cycle = -10)

	pattern = field \
		+ ((1-amplitude) - noise_like_signal) * diverging_element \
		+ noise_like_signal*np.exp(1j*phase)

	return pattern

def Gerchber_Saxton(target_field, input_field):
	# Error finding function
	def find_err(field_A):
		Check_intensity = Parts.Misc.get_amplitude(field_A)**2
		Sum = Check_intensity - np.mean(Check_intensity)
		err = (np.sum(Sum**2))**0.5 / np.sum(Check_intensity)
		return err

	# Preparation
	# Get target amplitude from target field
	target_amplitude = Parts.Misc.get_amplitude(target_field)
	# [0, 1] -> [0, 255]
	target_amplitude = (255/np.max(target_amplitude)) * target_amplitude

	# Get first step of the algorithm
	A = scipy.fftpack.fftshift(\
			scipy.fftpack.ifft2(\
				scipy.fftpack.fftshift(target_amplitude)))

	# Iterations will continue until the error is 0.5%
	while find_err(A) >= 5 * 1e-03:
		B = Parts.Misc.get_amplitude(input_field) * \
				np.exp(1j * np.angle(A))
		C = scipy.fftpack.fftshift(\
				scipy.fftpack.ifft2(\
					scipy.fftpack.fftshift(B)))
		D = target_amplitude * np.exp(1j * np.angle(C))
		A = scipy.fftpack.fftshift(\
				scipy.fftpack.ifft2(\
					scipy.fftpack.fftshift(D)))


	# return encoded field A
	return A