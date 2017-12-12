import numpy as np
import scipy.special

def LG_modes(r, theta, z, l, p, wavelenth, w_0):
	z_R = np.pi*w_0**2 / wavelenth #Rayleigh range
	w_z = w_0 * (1 + (z/z_R)**2)**.5
	R_z = z**2 + z_R**2
	k = 2*np.pi/wavelenth
	phi = (2*p + l + 1) * np.arctan(z/z_R) #Gouy phase shift 

	
	Re = 1/w_z * (r * 2**.5 / w_z)**abs(l) * np.exp(-r**2 / w_z**2) * scipy.special.assoc_laguerre(2*r**2 / w_z**2, p, l) 
	Im = np.exp(-1j*k* r**2 / (2*R_z)) * np.exp(-1j*l*theta) * np.exp(-1j*k*z) * np.exp(1j*phi)

	#additional field
	Re1 = 0# 1/w_z * (r * 2**.5 / w_z)**abs(l-1) * np.exp(-r**2 / w_z**2) * scipy.special.assoc_laguerre(2*r**2 / w_z**2, p, l-1) 
	Im1 = 0#np.exp(-1j*k* r**2 / (2*R_z)) * np.exp(-1j*(l-1)*theta) * np.exp(-1j*k*z) * np.exp(1j*phi)

	Ampl = abs(Re*Im + Re1*Im1)
	Phase = np.imag(Re*Im + Re1*Im1)
	return Ampl, Phase