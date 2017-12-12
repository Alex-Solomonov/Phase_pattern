# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import os
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import Approx_equation as eq

# #
w_0 = 3.*1e-03 #Gaussian beam size in m
wavelenth = 555*1e-09 # in mb
Topological_charge = 1
Nodes_radial = 0 #Number of nodes in radial direction


# # LC R1080
Width = 10.56*1e-03 # im m
Resolution = 1200 #pixels



x = y = np.linspace(-Width/2,Width/2,Resolution)
r = np.empty([int(Resolution), int(Resolution)], float)
theta = np.zeros_like(r)

# # Coord2Cylinder
for i in range(int(Resolution)):
	for j in range(int(Resolution)):
		r[i,j] = (x[i]**2 + y[j]**2)**.5
theta = np.arctan2(y,x)

amplitude = np.empty([int(Resolution), int(Resolution)], float)
phase = np.zeros_like(amplitude)






amplitude, phase = eq.LG_modes(r = r, theta = theta, z = 0,
	l = Topological_charge,
	p = Nodes_radial,
	wavelenth = wavelenth, 
	w_0 = w_0)


E_0 = 255/np.max(amplitude**2)
amplitude = E_0*amplitude
E_0 = 255/np.max(phase)
phase = E_0*phase

u = np.zeros_like(amplitude)
v = np.zeros_like(amplitude)
new_phase = np.zeros_like(amplitude)


for i in range(int(Resolution)):
	for j in range(int(Resolution)):
		if j % 2 == 0:
			u[i,j] = phase[i,j] + np.arccos(amplitude[i,j]/2)
			v[i,j] = 0
		else:
			u[i,j] = 0
			v[i,j] = phase[i,j] - np.arccos(amplitude[i,j]/2)

new_phase = u +v



my_path = os.path.dirname(__file__)
print(my_path)

# # amplitude
fig, ax = plt.subplots(1,1)
im = ax.imshow(amplitude**2, origin = 'lower', cmap=cm.gray)
plt.colorbar(im, orientation='horizontal')

# # phase
fig, ax = plt.subplots(1,1)
im = ax.imshow(phase, origin = 'lower', cmap=cm.gray)
plt.axis('off')

# # new_phase
fig, ax = plt.subplots(1,1)
im = ax.imshow(new_phase, origin = 'lower', cmap=cm.gray)
plt.axis('off')

plt.show()
