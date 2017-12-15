import numpy as np
import scipy.special



# # from wiki and thesis
def LG_modes(r, theta, z, l, p, wavelenth, w_0):
	z_R = np.pi*w_0**2 / wavelenth #Rayleigh range
	w_z = w_0 * (1 + (z/z_R)**2)**.5
	R_z = z**2 + z_R**2
	k = 2*np.pi/wavelenth
	phi = (2*p + l + 1) * np.arctan(z/z_R) #Gouy phase shift 

	
	Re = 1/w_z * (r * 2**.5 / w_z)**abs(l) * np.exp(-r**2 / w_z**2) * scipy.special.assoc_laguerre(2*r**2 / w_z**2, p, l) 
	Im = np.exp(-1j*l*theta) * np.exp(-1j*k* r**2 / (2*R_z)) * np.exp(1j*phi) * np.exp(-1j*k*z)

	#additional field
	Re1 = 1/w_z * (r * 2**.5 / w_z)**abs(l-1) * np.exp(-r**2 / w_z**2) * scipy.special.assoc_laguerre(2*r**2 / w_z**2, p, l-1) 
	Im1 = np.exp(-1j*k* r**2 / (2*R_z)) * np.exp(-1j*(l-1)*theta) * np.exp(-1j*k*z) * np.exp(1j*phi)

	Ampl = abs(Re*Im)
	Phase = np.arctan2(np.imag(Re*Im), np.real(Re*Im))
	return Ampl, Phase



# #Doesn't calculate the phase
# # From wiki
def HyGG(r, theta, z, l, p, wavelenth, w_0):
	rho = r/w_0

	z_R = np.pi*w_0**2 / wavelenth
	Z = z/z_R
	phi = (2*p + l + 1) * np.arctan(z/z_R)

	Re = ((2 ** (p + abs(l) +1))/(np.pi * scipy.special.gamma(p + abs(l) +1)))**.5 * (scipy.special.gamma(1+abs(l)+p/2)/scipy.special.gamma(abs(l)+1)) * Z**(p/2) * rho ** abs(l)
	Im = 1j**(abs(l)+1) * (Z + 1j)**(-p - abs(l) - 1) * np.exp(-1j*rho**2 / (Z+1j)) * np.exp(1j*l*phi) * scipy.special.hyp1f1(-p/2, abs(l)+1, r**2 / (Z**2+1j*Z))

	Ampl = abs(Re*Im)
	Phase = np.arctan2(np.imag(Re*Im), np.real(Re*Im))
	return Ampl, Phase



# # Doesn't work
# # from opt letters vol 40 eq (10)
def Bessel_fun(r, theta, l, w_0):
	Re = scipy.special.j1(2* r**2/ w_0**2) * np.exp(-r**2 / w_0**2)
	Im = np.exp(1j*theta*l)

	Ampl = abs(Re*Im)
	Phase = np.arctan2(np.imag(Re*Im), np.real(Re*Im))
	return Ampl, Phase


	
def F(r, theta, l, w_0):
	Re = np.exp(-r**2 / w_0**2) * r
	Im = np.exp(1j * l * theta)

	u = Re * Im

	Ampl = abs(u)
	Phase = np.arctan2(np.imag(u), np.real(u))
	return Ampl, Phase


def Bessel(r, theta, l):
	Ampl = scipy.special.jv(l, r)
	Ampl = Ampl/np.max(Ampl)


	Phase = l * theta
	
	return Ampl, Phase
