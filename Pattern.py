import numpy as np
import scipy.special
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

w_0 = 1.*1e-03 #Gaussian beam size in m
wavelenth = 555*1e-09
Topological_charge = 1
Nodes_radial = 0 #Number of nodes in radial direction

def Wiki_LG(x,y,z, l, p):
	r = (x**2 + y**2)**.5
	theta = np.arctan2(y,x)
	z_R = np.pi*w_0**2 / wavelenth #Rayleigh range
	w_z = w_0 * (1 + (z/z_R)**2)**.5
	R_z = z**2 + z_R**2
	k = 2*np.pi/wavelenth
	phi = (2*p + l + 1) * np.arctan(z/z_R) #Gouy phase shift 

	
	Re = 1/w_z * (r * 2**.5 / w_z)**abs(l) * np.exp(-r**2 / w_z**2) * scipy.special.assoc_laguerre(2*r**2 / w_z**2, p, l) 
	Im = np.exp(-1j*k* r**2 / (2*R_z)) * np.exp(-1j*l*theta) * np.exp(-1j*k*z) * np.exp(1j*phi)

	Re1 = 0# 1/w_z * (r * 2**.5 / w_z)**abs(l-1) * np.exp(-r**2 / w_z**2) * scipy.special.assoc_laguerre(2*r**2 / w_z**2, p, l-1) 
	Im1 = 0#np.exp(-1j*k* r**2 / (2*R_z)) * np.exp(-1j*(l-1)*theta) * np.exp(-1j*k*z) * np.exp(1j*phi)
	Ampl = abs(Re*Im + Re1*Im1)
	Phase = np.imag(Re*Im + Re1*Im1)
	return Ampl, Phase

scale = 1200

x = np.linspace(-10.56*1e-03,10.56*1e-03,scale)
y = np.linspace(-10.56*1e-03,10.56*1e-03,scale)

amplitude = np.empty([int(scale), int(scale)], float)
phase = np.zeros_like(amplitude)
for i in range(int(scale)):
	for j in range(int(scale)):
		amplitude[i,j], phase[i,j] = Wiki_LG(x = x[i], 
			y = y[j], 
			z = 0,
			l = Topological_charge,
			p = Nodes_radial)


E_0 = 255/np.max(amplitude**2)
amplitude = E_0*amplitude
E_0 = 255/np.max(phase)
phase = E_0*phase

u = np.zeros_like(amplitude)
v = np.zeros_like(amplitude)
new_phase = np.zeros_like(amplitude)


for i in range(int(scale)):
	for j in range(int(scale)):
		if j+1//2 != 0:
			u[i,j] = phase[i,j] + np.arccos(amplitude[i,j]/2)
			v[i,j] = 0
		else:
			u[i,j] = 0
			v[i,j] = phase[i,j] - np.arccos(amplitude[i,j]/2)

newphase = u + v




fig, ax = plt.subplots(1,1)# ,subplot_kw=dict(projection='polar')
# # amplitude
# im = ax.imshow(amplitude**2, origin = 'lower', cmap=cm.gray)
# plt.colorbar(im, orientation='horizontal')

# # phase
# im = ax.imshow(phase, origin = 'lower', cmap=cm.gray)
# plt.axis('off')

# # new_phase
im = ax.imshow(new_phase, origin = 'lower', cmap=cm.gray)
plt.axis('off')

# plt.savefig('phase.png')
# plt.savefig('phase.tiff')
# plt.savefig('phase.jpg')
plt.show()
