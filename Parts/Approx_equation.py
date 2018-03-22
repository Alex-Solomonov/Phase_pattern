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
	Ampl -= np.min(Ampl)
	factor = 1 / np.amax(Ampl)

	field = factor * Ampl \
		*np.exp(1j*l*theta)
	
	return field

def Bessel_max_at_2(r, theta, l):
	Ampl = scipy.special.jv(l, r)
	Phase = np.angle(np.exp(1j*l*theta))
	factor = 2 / np.amax(Ampl)

	return factor * Ampl, Phase


def Hollow_G(r, theta, l):
	Ampl = (r)**l * np.exp(-r**2)
	Phase = np.angle(np.exp(1j*l*theta))
	
	return Ampl, Phase

def Hollow_rectangle(r):
	size = np.shape(r)

	r[size[0]//3:2*size[0]//3,size[1]//3:2*size[1]//3] = 2
	r[size[0]//2 - size[0]//10:size[0]//2 + size[0]//10,size[1]//2 - size[1]//10:size[1]//2 + size[1]//10] = 0

	return r

def Square(r):
	size = np.shape(r)

	side = 10
	r = np.zeros_like(r)
	r[size[0]//2 - side/2:size[0]//2 + side/2,size[1]//2 - side/2:size[1]//2 + side/2] = 1

	return r


def axicon(LSM_pars, cycle):
	Width_x = LSM_pars[0]
	Width_y = LSM_pars[1]

	Resolution_x = LSM_pars[2]
	Resolution_y = LSM_pars[3]

	Side_resolution = np.min([Resolution_x, Resolution_y])
	if Side_resolution == Resolution_x:
		Side = Width_x/2
		Move = Resolution_y - Side_resolution
		axis = 1
	else:
		Side = Width_y/2
		Move = Resolution_x - Side_resolution
		axis = 0

	# Create square-like pattern
	Coordinates = Parts.Create_space.Generate([Side, Side, 
		Side_resolution, Side_resolution])

	phase = 2*np.pi * cycle *(1 - Coordinates[0]/Side)

	# Create rectangle-like pattern
	# Here pattern look like
	# 1 1 
	# 1 1 
	# And it should look like
	# 0 1 1 0
	# 0 1 1 0
	# Then an phase array is concatenate to zeros array
	# 1 1 0 0
	# 1 1 0 0
	if axis == 1:
		zero = np.empty([Side_resolution, Move], float)
		pattern = np.hstack((phase, zero))
	else:
		zero = np.empty([Move, Side_resolution], float)
		pattern = np.vstack((phase, zero))
	# Move to center
	# 0 1 1 0
	# 0 1 1 0 
	pattern = np.roll(pattern, Move//2, axis)
	return np.angle(np.exp(1j*pattern), deg=True)