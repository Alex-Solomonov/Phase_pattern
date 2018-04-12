import numpy as np

def get_amplitude(field):
	return np.abs(field)

def get_phase(field):
	return  np.arctan2(np.imag(field), np.real(field))